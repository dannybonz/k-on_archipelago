import websockets, json, requests, struct, base64, asyncio, traceback, ipaddress

from .Data import EVENT_FLAGS_FROM_ADDRESS, SNACKS, SONGS, SNACK_NAME_FROM_ADDRESS, SONG_FLAGS_FROM_ADDRESS, PROP_FLAGS_FROM_ADDRESS, PROPS, CHARACTERS, OUTFITS, EVENT_TITLES_FROM_INGAME_ID, EVENTS, OUTFIT_MAPPING, HARD_SONGS

MATCH_API_URL = "https://report.ppsspp.org/match/list"

class KONInterface:
    #Memory addresses
    #Gameplay
    CHARACTER_ADDRESS = 0x90aece0
    CHARACTER_MAPPING = {0: "Yui", 1: "Mio", 2: "Ritsu", 3: "Mugi", 4: "Azusa"}
    CURRENT_SONG_ADDRESS = 0x90aecd4
    SONG_MAPPING = {
        0: "Cagayake!GIRLS", 1: "Don't Say Lazy", 2: "Fuwa Fuwa Time", 3: "My Love is a Stapler",
        4: "Calligraphy Pen ~Ballpoint Pen~", 5: "Curry, Then Rice", 6: "Let's Go", 7: "Happy!? Sorry!!",
        8: "Sweet Bitter Beauty Song", 9: "Head Over Heels for Giita", 10: "Sunday Siesta", 11: "Heart Goes Boom!!",
        12: "Hello Little Girl", 13: "Jajauma Way To Go", 14: "I Go My Own Road", 15: "Dear My Keys",
        16: "Humming Bird", 17: "Girly Storm Sprint Stick", 18: "Aim for Happy 100%"
    }
    DIFFICULTY_ADDRESS = 0x90aee28 #Difficulty being played 0 = Normal 1 = Hard
    MEASURE_ADDRESS = 0x90aee3c #Progress through the song
    CURSOR_ADDRESS = 0x90aee38 #Cursor position
    SCORE_ADDRESS = 0x90aee40
    HEALTH_ADDRESS = 0x90aee4c
    ITEM_ACTIVE_ADDRESS = 0x90aee58 #Whether an item is being used or not
    ITEM_START_ADDRESS = 0x90aee60 #The measure where the item effect begins
    ITEM_END_ADDRESS = 0x90aee64 #The measure where the item effect ends

    #Results
    SONG_OUTCOME_ADDRESS = 0x90aee74
    SONG_OUTCOME_MAPPING = {0: "Cleared", 1: "Failed", 2: "Exited", 3: "Restarted"}
    COMBO_ADDRESS = 0x90aee8c #Max combo
    GRADE_ADDRESS = 0x490afdfc #Your rank

    #Unlockables
    TITLE_FLAGS_ADDRESSES = [0x90b0aa4, 0x90b0aa5, 0x90b0aa6, 0x90b0aa7, 0x90b0aa8, 0x90b0aa9, 0x90b0aaa, 0x90b0aab, 0x90b0aac] #Unlocked titles
    SONG_COUNT_ADDRESS = 0x48ee5a78 #Number of songs that can be selected from on the selection screen
    CURRENT_EVENT_ADDRESS = 0x491aec9c #Event being viewed
    OUTFIT_ADDRESS_FROM_CHAR = {"Yui": 0x490b1b30, "Mio": 0x490b1b48, "Ritsu": 0x490b1b60, "Mugi": 0x490b1b78, "Azusa": 0x490b1b90} #Contains the current equipped outfit for each character
    CHAR_FROM_OUTFIT_ADDRESS = {address: character for character, address in OUTFIT_ADDRESS_FROM_CHAR.items()}

    #PC addresses
    #Gameplay
    BEGIN_SONG_FUNC_ADDRESS = 0x88e0190 #Triggers during the MC portion
    GAMEPLAY_START_FUNC_ADDRESS = 0x882dca0 #Triggers when gameplay begins
    RESULTS_FUNC_ADDRESS = 0x88e0330 #Triggers when results screen opens
    ACTIVATE_ITEM_FUNC_ADDRESS = 0x0882ec64 #Triggers when a snack has been activated

    #Unlockables
    LOAD_SONG_LIST_FUNC_ADDRESS = 0x886d5a4 #Triggers when selecting the song list
    LOAD_UNLOCKED_SONGS_FUNC_ADDRESS = 0x885d8f4 #Triggers when loading which specific songs have been unlocked
    INVENTORY_OPEN_FUNC_ADDRESS = 0x88ad4f4 #Triggers when opening the inventory
    OUTFIT_OPEN_FUNC_ADDRESS = 0x885430c #Triggers when visiting the outfit screen
    START_EVENT_FUNC_ADDRESS = 0x0896d974 #Triggers when an event is started

    def __init__(self, logger) -> None:
        self.logger = logger
        self.ws = None  #WebSocket connection
        self.memory_request_log = []  #Track memory requests
        self.ws_url = None
        self.songs_received: list[str] = []
        self.hard_songs_received: list[str] = []
        self.props_received: list[str] = ["Yui's Phone Number", "Mio's Phone Number", "Ritsu's Phone Number", "Mugi's Phone Number", "Azusa's Phone Number", "Clubroom Sign", "Chocolate", "Popsicle", "Taiyaki", "Cake", "Cookie", "Tart", "Sweets", "Strawberry Milk", "Performance Scroll", "Item Scroll"] #Items that are pre-placed in your inventory
        self.song_clears: list[str] = []
        self.hard_song_clears: list[str] = []
        self.character_clears: list[str] = []
        self.hard_character_clears: list[str] = []
        self.combo_clears: list[str] = []
        self.hard_combo_clears: list[str] = []
        self.character_combo_clears: list[str] = []
        self.hard_character_combo_clears: list[str] = []
        self.rank_clears: list[str] = []
        self.character_rank_clears: list[str] = []
        self.hard_rank_clears: list[str] = []
        self.hard_character_rank_clears: list[str] = []
        self.event_clears: list[str] = []
        self.completionist_clears: list[str] = []
        self.hard_completionist_clears: list[str] = []
        self.characters_received: list[str] = []
        self.outfits_received: list[str] = []
        self.active_outfits = {"Yui": None, "Mio": None, "Ritsu": None, "Mugi": None, "Azusa": None}
        self.song_screen = None
        self.queued_memory_writes = []
        self.current_character = None
        self.song_outcome = None
        self.current_song = None
        self.combo = 0
        self.grade = 4
        self.goal_song = None
        self.game_frozen = False
        self.outfit_inventory_matches_archi_items = False
        self.snacks_to_add = {}
        self.snack_write = {}
        self.tension_upgrade: int = 0 #Unused
        self.food_duration: int = 15
        self.token_count: int = 0
        self.token_requirement: int = 999
        self.tape_count: int = 0
        self.tape_requirement: int = 999
        self.matching_outfits_goal = True
        self.loaded_kon = False

    def get_ppsspp_endpoint(self): #Fetch the PPSSPP communication URL from the API
        try:
            response = requests.get(MATCH_API_URL)
            response.raise_for_status()
            data = response.json()

            if not data:
                print("Couldn't fetch from API.")
                return None

            #Look for the first IPv4 address
            for instance in data:
                ip = instance.get("ip")
                port = instance.get("p")
                if ip and port:
                    try:
                        if ipaddress.ip_address(ip).version == 4:
                            ws_url = f"ws://{ip}:{port}/debugger"
                            print("Found PPSSPP WebSocket.")
                            return ws_url
                    except ValueError:
                        continue  #Skip invalid IP formats
            
            print("No IPv4 addresses found.")
            return None
        except requests.RequestException as e:
            print(f"Error fetching PPSSPP instances: {e}")
            return None

    async def set_breakpoints(self) -> None:
        #Set breakpoints to watch for specific cpu function calls
        await self.set_cpu_breakpoint(self.LOAD_SONG_LIST_FUNC_ADDRESS) #Used to display all the buttons on the song select
        await self.set_cpu_breakpoint(self.INVENTORY_OPEN_FUNC_ADDRESS) #Used to update inventory to only the items you should have, whenever you open it
        await self.set_cpu_breakpoint(self.LOAD_UNLOCKED_SONGS_FUNC_ADDRESS) #Used to adjust the unlocked songs, whenever you open it
        await self.set_cpu_breakpoint(self.RESULTS_FUNC_ADDRESS) #Used to check the results screen
        await self.set_cpu_breakpoint(self.BEGIN_SONG_FUNC_ADDRESS) #Function called when song begins - used to kill you if you shouldn't be playing this one
        await self.set_cpu_breakpoint(self.OUTFIT_OPEN_FUNC_ADDRESS) #Used to update outfit collection to only the outfits you should have, whenever you open it
        await self.set_cpu_breakpoint(self.START_EVENT_FUNC_ADDRESS) #Used when triggering an event
#            await self.set_cpu_breakpoint(self.GAMEPLAY_START_FUNC_ADDRESS) #Function called when song gameplay starts - currently unused, could work with future Tension Upgrade item
        await self.set_cpu_breakpoint(self.ACTIVATE_ITEM_FUNC_ADDRESS) #Function called when using an item - allows us to apply the duration upgrade

    async def get_loaded_game_status(self):
        request = {"event": "game.status"} #Check for game
        await self.ws.send(json.dumps(request))

    async def connect_to_ppsspp(self) -> bool:
        if self.ws_url is None:
            self.ws_url = self.get_ppsspp_endpoint()
            if self.ws_url is None:
                return False

        try:
            self.ws = await websockets.connect(self.ws_url)
            asyncio.create_task(self.websocket_listener())
            await self.get_loaded_game_status()
            return True
        except Exception as e:
            print(f"PPSSPP connection failed with error: {e}")
            return False

    async def disconnect(self) -> None:
        if self.ws:
            await self.ws.close()
            self.ws = None

    async def websocket_listener(self) -> None:
        try:
            async for message in self.ws:
                if message:
                    response = json.loads(message)
                    event_type = response.get("event")

                    if event_type == "memory.read":
                        await self.handle_memory(response)
                    elif event_type == "cpu.stepping":
                        await self.handle_breakpoint(response)
                    elif event_type == "memory.write":
                        await self.handle_write(response)
                    elif event_type == "game.status":
                        game = response.get("game")
                        if game and game.get("id") in ["ULJM05709", "ULJM08048"]:
                            self.loaded_kon = True
                            await self.set_breakpoints()
                    elif event_type in ["log", "error"]:
                        print(response)
                    else:
                        print(f"Unexpected event: {event_type}")
        except Exception as e:
            print(f"WebSocket error: {e}")
            traceback.print_exc()
        print("WebSocket listener stopped.")

    async def handle_breakpoint(self, response) -> None:
        self.game_frozen = True
        pc_address = response['pc']

        if pc_address == self.LOAD_SONG_LIST_FUNC_ADDRESS: #When loading the song lists, we first check character outfits. Once those are all checked, we then set the unlocked songs.
            self.active_outfits = {"Yui": None, "Mio": None, "Ritsu": None, "Mugi": None, "Azusa": None}
            for character in CHARACTERS:
                await self.request_memory(self.OUTFIT_ADDRESS_FROM_CHAR[character])
        elif pc_address == self.LOAD_UNLOCKED_SONGS_FUNC_ADDRESS:
            await self.write_memory(self.set_unlocked_songs(self.songs_received) | self.set_unlocked_hard_songs(self.hard_songs_received)) #Set the unlocked songs
        elif pc_address == self.START_EVENT_FUNC_ADDRESS:
            await self.request_memory(self.CURRENT_EVENT_ADDRESS)
        elif pc_address == self.OUTFIT_OPEN_FUNC_ADDRESS:
            if not self.outfit_inventory_matches_archi_items:
                await self.write_memory(self.set_unlocked_outfits(self.outfits_received))
                self.outfit_inventory_matches_archi_items = True
            else:
                await self.resume_emulation()
        elif pc_address == self.INVENTORY_OPEN_FUNC_ADDRESS:
            #Check for secret phones
            self.secret_phones = {"Sawako": "Sawako's Phone Number" in self.props_received, "Ui": "Ui's Phone Number" in self.props_received, "Nodoka": "Nodoka's Phone Number" in self.props_received}
            if not False in self.secret_phones.values(): #Secret phones all obtained
                await self.write_memory(self.set_unlocked_props(self.props_received))
            else: #Secret phones not all obtained; check if we need to add them
                for character in self.secret_phones:
                    if self.secret_phones[character] == False:
                        await self.request_memory({"Sawako": EVENTS["Event: Dress Tutorial"]["address"], "Ui": EVENTS["Event: Little Sister!"]["address"], "Nodoka": EVENTS["Event: Childhood Friend!"]["address"]}[character])
        elif pc_address == self.RESULTS_FUNC_ADDRESS:
            self.song_screen = "Results"
            await self.request_memory(self.SONG_OUTCOME_ADDRESS)
        elif pc_address == self.BEGIN_SONG_FUNC_ADDRESS:
            self.song_screen = "Starting Song"
            await self.request_memory(self.CHARACTER_ADDRESS)
        elif pc_address == self.ACTIVATE_ITEM_FUNC_ADDRESS:
            await self.request_memory(self.ITEM_START_ADDRESS)
        else: #No criteria to actually do anything has been met from this breakpoint, so let's just continue
            await self.resume_emulation()

    async def request_memory(self, address, size: int = 4) -> None:
        request = {"event": "memory.read", "address": address, "size": size}
        await self.ws.send(json.dumps(request))
        self.memory_request_log.append(address)

    async def write_memory(self, changes, size: int = 4):
        for address in changes:
            self.queued_memory_writes.append({"address": address, "value": changes[address]})

        for address in changes:
            value = changes[address]
            if size == 1:
                packed_value = struct.pack("<B", value)
            elif size == 2:
                packed_value = struct.pack("<H", value)
            elif size == 4:
                packed_value = struct.pack("<I", value)
            else:
                raise ValueError("Unsupported memory write size")

            write_request = {
                "event": "memory.write",
                "address": address,
                "size": size,
                "base64": base64.b64encode(packed_value).decode("utf-8")
            }

            await self.ws.send(json.dumps(write_request))

    async def handle_write(self, response) -> None:
        if len(self.queued_memory_writes) > 0:
            del self.queued_memory_writes[0]
    
        if len(self.queued_memory_writes) == 0: #All queued memory writes are complete, let's resume emulation
            if len(self.snacks_to_add) > 0: #...unless we have received snack items that are waiting to be added! Let's just add them now quickly.
                await self.update_snacks()
            else:
                await self.resume_emulation()

    async def set_cpu_breakpoint(self, address) -> None:
        request = {"event": "cpu.breakpoint.add", "address": address}
        await self.ws.send(json.dumps(request))

    async def set_memory_breakpoint(self, address, size: int) -> None:
        request = {
            "event": "memory.breakpoint.add",
            "address": address,
            "size": size,
            "write": True,
            "change": True
        }
        await self.ws.send(json.dumps(request))

    async def resume_emulation(self) -> None:
        if self.game_frozen:
            self.game_frozen = False
            request = {"event": "cpu.resume"}
            await self.ws.send(json.dumps(request))

    async def get_connection_state(self) -> bool:
        if not self.ws or not self.ws.open:
            return False
        try:
            pong_waiter = await self.ws.ping()
            await asyncio.wait_for(pong_waiter, timeout=5)  # Wait for pong reply, timeout after 5 seconds
            return True
        except Exception:
            return False  # Ping failed or timed out, connection likely dead

    async def handle_memory(self, response) -> None:
        raw_bytes = base64.b64decode(response["base64"])
        if len(self.memory_request_log) > 0:
            last_request = self.memory_request_log.pop(0)
        address = last_request
        value = struct.unpack("<I", raw_bytes)[0]  #Convert bytes to int

        if address == self.CHARACTER_ADDRESS:
            if (self.song_screen == "Results"):
                self.current_character = self.CHARACTER_MAPPING[value]
                if (f"Playable {self.current_character}" in self.characters_received):
                    await self.request_memory(self.COMBO_ADDRESS)
                else:
                    await self.resume_emulation() #No check - you shouldn't have this character!
            elif (self.song_screen == "Starting Song"):
                self.current_character = self.CHARACTER_MAPPING[value]
                if not (f"Playable {self.current_character}" in self.characters_received):
                    self.logger.info("You don't have this character unlocked! Use /characters to see your current unlocked characters.")
                    await self.write_memory({self.CURSOR_ADDRESS: 4000}) #Move cursor past all the notes, triggering Game Over
                else:
                    await self.write_memory(self.set_unlocked_hard_songs(list(HARD_SONGS.keys()))) #Sets all Hard songs to unlocked, preventing popups at the end of the song

        elif address == self.CURRENT_EVENT_ADDRESS:
            if not EVENT_TITLES_FROM_INGAME_ID[value] in self.event_clears:
                self.event_clears.append(EVENT_TITLES_FROM_INGAME_ID[value])
            if EVENT_TITLES_FROM_INGAME_ID[value] == "Event: Item Tutorial":
                self.receive_snack("Cake", 1) #Adds a Cake - you need to it to complete the tutorial
                await self.update_snacks()
            await self.resume_emulation()

        elif address == self.DIFFICULTY_ADDRESS:
            self.song_clears.append(f"{self.current_song}: Clear")
            self.character_clears.append(f"{self.current_song}: Clear with {self.current_character}")

            if value == 1:
                self.hard_song_clears.append(f"{self.current_song}: Clear on Hard")
                self.hard_character_clears.append(f"{self.current_song}: Clear with {self.current_character} on Hard")

            combo_target = SONGS[self.current_song]["combo"]
            if self.combo >= combo_target:
                self.combo_clears.append(f"{self.current_song}: {combo_target} Combo")
                self.character_combo_clears.append(f"{self.current_song}: {combo_target} Combo with {self.current_character}")
                if value == 1:
                    self.hard_combo_clears.append(f"{self.current_song}: {combo_target} Combo on Hard")
                    self.hard_character_combo_clears.append(f"{self.current_song}: {combo_target} Combo with {self.current_character} on Hard")

            if self.grade <= 1: #A rank
                self.rank_clears.append(f"{self.current_song}: A Rank")
                self.character_rank_clears.append(f"{self.current_song}: A Rank with {self.current_character}")
                if value == 1:
                    self.hard_rank_clears.append(f"{self.current_song}: A Rank on Hard")
                    self.hard_character_rank_clears.append(f"{self.current_song}: A Rank with {self.current_character} on Hard")

            completionist_check = True
            for character in CHARACTERS:
                if value == 0:
                    if not (f"{self.current_song}: Clear with {character}") in self.character_clears:
                        completionist_check = False
                else:
                    if not (f"{self.current_song}: Clear with {character} on Hard") in self.character_clears:
                        completionist_check = False
            
            if completionist_check:
                if value == 0:
                    self.completionist_clears.append(f"{self.current_song}: Full Band Clear")
                else:
                    self.hard_completionist_clears.append(f"{self.current_song}: Full Band Clear on Hard")

            await self.resume_emulation()

        elif address == self.COMBO_ADDRESS:
            self.combo = value
            await self.request_memory(self.GRADE_ADDRESS)

        elif address == self.GRADE_ADDRESS:
            self.grade = value
            await self.request_memory(self.DIFFICULTY_ADDRESS)
            
        elif address == self.SONG_OUTCOME_ADDRESS:
            self.song_outcome = self.SONG_OUTCOME_MAPPING[value]
            if self.song_outcome == "Cleared":
                await self.request_memory(self.CURRENT_SONG_ADDRESS)
            else:
                await self.resume_emulation() #No check - you failed the song!

        elif address == self.CURRENT_SONG_ADDRESS:
            self.current_song = self.SONG_MAPPING[value]
            if self.current_song in self.songs_received:
                await self.request_memory(self.CHARACTER_ADDRESS)
            else:
                await self.resume_emulation() #No check - you shouldn't even HAVE this song!

        elif address in SNACK_NAME_FROM_ADDRESS:
            snack_name = SNACK_NAME_FROM_ADDRESS[address]

            if snack_name in self.snacks_to_add:
                new_snack_count = value + self.snacks_to_add[snack_name]
                self.snack_write[address] = new_snack_count
                del self.snacks_to_add[snack_name]

            if len(self.snacks_to_add) > 0:
                next_snack = list(self.snacks_to_add.keys())[0]
                await self.request_memory(SNACKS[next_snack]["address"])
            else:
                await self.write_memory(self.snack_write)
                self.snack_write = {}

        elif address == self.ITEM_START_ADDRESS:
            new_end = value + self.food_duration
            await self.write_memory({self.ITEM_END_ADDRESS: new_end})

        elif address in self.CHAR_FROM_OUTFIT_ADDRESS:
            character = self.CHAR_FROM_OUTFIT_ADDRESS[address]
            self.active_outfits[character] = OUTFIT_MAPPING[value]
            if character == "Azusa" and self.active_outfits[character] == "Winter Outfit":
                self.active_outfits[character] = "Old Uniform Outfit"

            if not None in list(self.active_outfits.values()): #If we know what all current outfits are
                outfits_to_write = {}
                for character in self.active_outfits: #Look through them all to check that they are ones we have the item for - if not, change to one we do own
                    if len(self.outfits_received) > 0 and not (f"{character}'s {self.active_outfits[character]}") in self.outfits_received:
                        replacement_outfit = next(outfit for outfit in self.outfits_received if outfit.startswith(character))
                        outfits_to_write[self.OUTFIT_ADDRESS_FROM_CHAR[character]] = OUTFITS[replacement_outfit]["ingame_id"]

                memory_to_write = self.set_unlocked_songs(self.songs_received) | self.set_unlocked_hard_songs(self.hard_songs_received) | self.unlock_all_titles() | outfits_to_write | {self.SONG_COUNT_ADDRESS: 20} | (self.set_unlocked_props(list(PROPS.keys()))) | (self.set_unlocked_outfits(list(OUTFITS.keys()))) #Unlocks EVERYTHING - means you won't get popups at the end! (hopefully?)
                await self.write_memory(memory_to_write)
                self.outfit_inventory_matches_archi_items = False #When you open the outfits again, it'll match them to your received outfits

        elif address == EVENTS["Event: Dress Tutorial"]["address"]: #Check if Sawa-chan is unlocked.
            if value & (1 << 3):
                self.props_received.append("Sawako's Phone Number")

            self.secret_phones["Sawako"] = "Checked"
            if not False in self.secret_phones.values(): #Finished checking all characters
                await self.write_memory(self.set_unlocked_props(self.props_received))

        elif address == EVENTS["Event: Little Sister!"]["address"]: #Same for Ui.
            if value & (1 << 0):
                self.props_received.append("Ui's Phone Number")

            self.secret_phones["Ui"] = "Checked"
            if not False in self.secret_phones.values():
                await self.write_memory(self.set_unlocked_props(self.props_received))

        elif address == EVENTS["Event: Childhood Friend!"]["address"]: #Same for Nodoka.
            if value & (1 << 5):
                self.props_received.append("Nodoka's Phone Number")

            self.secret_phones["Nodoka"] = "Checked"
            if not False in self.secret_phones.values():
                await self.write_memory(self.set_unlocked_props(self.props_received))

    def unlock_song(self, song_title) -> None:
        self.songs_received.append(song_title)
        self.hard_songs_received.append(song_title + " (Hard)")

    def unlock_prop(self, prop) -> None:
        self.props_received.append(prop)

    def unlock_outfit(self, outfit) -> None:
        self.outfit_inventory_matches_archi_items = False
        self.outfits_received.append(outfit)

    def set_unlocked_songs(self, unlocked_songs):
        if self.tape_count >= self.tape_requirement and self.token_count >= self.token_requirement:
            if not (self.matching_outfits_goal == True and len(set(self.active_outfits.values())) > 1):
                if not self.goal_song in unlocked_songs:
                    unlocked_songs.append(self.goal_song) #Goal song unlocked!

        song_unlock_data = {}
        for song in SONGS:
            address = SONGS[song]["address"]
            if address not in song_unlock_data:
                song_unlock_data[address] = 0  #Start with all bits cleared

        for song in unlocked_songs:
            song_unlock_data[SONGS[song]["address"]] |= (1 << SONGS[song]["bit"])  #Set the bit for the song

        return song_unlock_data

    def set_unlocked_hard_songs(self, unlocked_hard_songs):
        hard_song_unlock_data = {}
        for song in HARD_SONGS:
            address = HARD_SONGS[song]["address"]
            if address not in hard_song_unlock_data:
                hard_song_unlock_data[address] = 0  #Start with all bits cleared

        for song in unlocked_hard_songs:
            hard_song_unlock_data[HARD_SONGS[song]["address"]] |= (1 << HARD_SONGS[song]["bit"])  #Set the bit for the song

        return hard_song_unlock_data        

    def set_unlocked_props(self, unlocked_props):
        prop_unlock_data = {}
        for prop in PROPS:
            address = PROPS[prop]["address"]
            if address not in prop_unlock_data:
                prop_unlock_data[address] = 0  #Start with all bits cleared

        for prop in unlocked_props:
            if not (prop == "Secret Score" and not "Secret Score" in self.props_received): #Only enable Secret Score if you have received it - prevents it from showing up when all items are temporarily activated during song selection
                prop_unlock_data[PROPS[prop]["address"]] |= (1 << PROPS[prop]["bit"])  #Set the bit for the prop

        return prop_unlock_data

    def set_unlocked_outfits(self, unlocked_outfits):
        outfit_unlock_data = {}
        for outfit in OUTFITS:
            address = OUTFITS[outfit]["address"]
            if address not in outfit_unlock_data:
                outfit_unlock_data[address] = 0  #Start with all bits cleared

        for outfit in unlocked_outfits:
            outfit_unlock_data[OUTFITS[outfit]["address"]] |= (1 << OUTFITS[outfit]["bit"])  #Set the bit for the outfit

        return outfit_unlock_data

    def unlock_all_titles(self):
        title_unlock_data = {}

        for address in self.TITLE_FLAGS_ADDRESSES:
            title_unlock_data[address] = 255

        return title_unlock_data

    def receive_snack(self, snack_name: str, snack_count: int) -> None:
        if snack_name in self.snacks_to_add:
            self.snacks_to_add[snack_name] += snack_count
        else:
            self.snacks_to_add[snack_name] = snack_count

    async def update_snacks(self) -> None:
        if len(self.snacks_to_add) > 0:
            snack_name = list(self.snacks_to_add.keys())[0]
            await self.request_memory(SNACKS[snack_name]["address"])