from typing import Optional, Set, Dict, Any
import asyncio, multiprocessing, traceback

from CommonClient import ClientCommandProcessor, CommonContext, get_base_parser, logger, server_loop, gui_enabled
from NetUtils import ClientStatus
import Utils

from .Interface import KONInterface
from .Data import EVENTS, SONGS, SNACKS, SNACK_NAME_FROM_ID, SONG_NAME_FROM_ID, PROP_NAME_FROM_ID, SONG_CLEARS, CHARACTER_CLEARS, PLAYABLE_CHARACTER_NAME_FROM_ID, PROPS, SONG_COMPLETIONIST_CLEARS, CHARACTER_CLEAR_NAME_FROM_ID, OUTFIT_NAME_FROM_ID, SONG_RANK_CLEARS, SONG_COMBO_CLEARS, CHARACTER_RANK_CLEARS, CHARACTER_COMBO_CLEARS, HARD_SONG_RANK_CLEARS, HARD_SONG_COMBO_CLEARS, HARD_CHARACTER_RANK_CLEARS, HARD_CHARACTER_COMBO_CLEARS, HARD_SONG_COMPLETIONIST_CLEARS, HARD_SONG_CLEARS, HARD_CHARACTER_CLEARS, HARD_CHARACTER_CLEAR_NAME_FROM_ID, CHARACTERS

class KONCommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx: CommonContext) -> None:
        super().__init__(ctx)

    def _cmd_characters(self) -> None:
        if isinstance(self.ctx, KONContext):
            log_characters(self.ctx)

    def _cmd_progress(self) -> None:
        if isinstance(self.ctx, KONContext):
            log_tokens(self.ctx)

class KONContext(CommonContext):
    client_version: str = "v1.0.4"

    game: str = "K-On! After School Live!!"

    command_processor = KONCommandProcessor
    items_handling = 0b111

    is_connected = False
    interface_sync_task : asyncio.tasks = None
    last_error_message : Optional[str] = None

    cached_received_items : Set[int]

    slot_data: Dict[str, Any]

    def __init__(self, address, password: str) -> None:
        super().__init__(address, password)
        Utils.init_logging(f"K-On! After School Live!! Archipelago Client {self.client_version}")

        self.interface = KONInterface(logger)
        self.tokens_reported = False
        self.cached_received_items = set()
        self.slot_data: Dict[str, Any] = {}
        self.sent_deaths = 0
        self.snack_cache_retrieved = False
        self.most_recent_instruction = None

    def on_package(self, cmd: str, args: Dict[str, Any]) -> None:
        if cmd == "Connected":
            self.slot_data = args["slot_data"]
            self.interface.food_duration = self.slot_data["default_food_duration"]
            self.previously_checked_locations = args["checked_locations"]
            self.interface.goal_song = self.slot_data["goal_song"]
            self.interface.token_requirement = self.slot_data["token_requirement"]
            self.interface.tape_requirement = self.slot_data["tape_requirement"]
            self.interface.matching_outfits_goal = self.slot_data["matching_outfits_goal"]       
            self.deathlink_pending = False
            self.played_songs = []
            self.snack_cache = {}

            if "snack_upgrades_enabled" in self.slot_data and self.slot_data["snack_upgrades_enabled"] == True:
                self.interface.snack_upgrades_enabled = True

        if cmd == "Retrieved":
            if "keys" in args:
                if f"k-on_played_songs_{self.team}_{self.slot}" in args["keys"]:
                    self.played_songs = args["keys"].get(f"k-on_played_songs_{self.team}_{self.slot}", [])
                    if self.played_songs == None:
                        self.played_songs = []
                if f"k-on_snack_cache_{self.team}_{self.slot}" in args["keys"]:
                    self.snack_cache = args["keys"].get(f"k-on_snack_cache_{self.team}_{self.slot}", {})
                    if self.snack_cache == None:
                        self.snack_cache = {}

                    self.snack_cache_retrieved = True

    async def server_auth(self, password_requested : bool = False) -> None:
        if password_requested and not self.password:
            await super().server_auth(password_requested)

        await self.get_username()
        await self.send_connect()

    def on_deathlink(self, data: dict):
        if "deathlink_enabled" in self.slot_data and self.slot_data["deathlink_enabled"] == True:
            self.deathlink_pending = True
            text = data.get("cause", "")
            if text:
                logger.info(f"DeathLink: {text}")
            else:
                logger.info(f"DeathLink: Received from {data['source']}")

    def run_gui(self) -> None:
        from kvui import GameManager

        class KONManager(GameManager):
            logging_pairs = [("Client", "Archipelago")]
            base_title = "K-On! After School Live!! Archipelago"

        self.ui = KONManager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name = "ui")

def update_connection_status(ctx, status) -> None:
    if ctx.is_connected == status:
        return

    if status:
        logger.info("Communications with PPSSPP began successfully.")
    else:
        logger.info("Not connected to PPSSPP.")

    ctx.is_connected = status

async def interface_sync_task(ctx) -> None:
    logger.info("Beginning communication with PPSSPP...")
    await ctx.interface.connect_to_ppsspp()
    await asyncio.sleep(4)

    while not ctx.exit_event.is_set():
        try:
            is_connected = await ctx.interface.get_connection_state()
            update_connection_status(ctx, is_connected)
            if is_connected:
                await asyncio.sleep(1)
                if ctx.interface.loaded_kon:
                    await check_game(ctx)
                else:
                    logger.info("K-On! After School Live!! is not currently running. Please load the game in PPSSPP.")
                    await asyncio.sleep(3)
                    await ctx.interface.get_loaded_game_status()
            else:
                await reconnect_game(ctx)
        except ConnectionError:
            await ctx.interface.disconnect()
        except Exception as e:
            if isinstance(e, RuntimeError):
                logger.error(str(e))
            else:
                logger.error(traceback.format_exc())

            await asyncio.sleep(3)
            continue

async def check_game(ctx) -> None:
    if ctx.server:
        if not ctx.slot:
            await asyncio.sleep(1)
            return
        elif not ctx.most_recent_instruction == "welcome":
            #Enable deathlink once connected
            if "deathlink_enabled" in ctx.slot_data and ctx.slot_data["deathlink_enabled"] == True:
                await ctx.update_death_link(True)

            await ctx.send_msgs([{"cmd": "Get", "keys": [f"k-on_played_songs_{ctx.team}_{ctx.slot}", f"k-on_snack_cache_{ctx.team}_{ctx.slot}"]}]) #Retrieve previously played songs and update snack cache once connected

            logger.info("You are now connected and ready to play. Let's rock!")
            logger.info("Use /progress to see your progress towards unlocking your Goal Song. Use /characters to see your currently unlocked characters.")
            ctx.most_recent_instruction = "welcome"

        checked_locations : Set[int] = set()

        #Check for events
        for event in ctx.interface.event_clears:
            checked_locations.add(EVENTS[event]["location_id"])

        #Check for basic clears
        for song_clear in ctx.interface.song_clears:
            checked_locations.add(SONG_CLEARS[song_clear]["location_id"])
        for character_clear in ctx.interface.character_clears:
            checked_locations.add(CHARACTER_CLEARS[character_clear]["location_id"])

        #Check for combo clears
        for combo_clear in ctx.interface.combo_clears:
            checked_locations.add(SONG_COMBO_CLEARS[combo_clear]["location_id"])
        for character_combo_clear in ctx.interface.character_combo_clears:
            checked_locations.add(CHARACTER_COMBO_CLEARS[character_combo_clear]["location_id"])

        #Check for A rank clears
        for rank_clear in ctx.interface.rank_clears:
            checked_locations.add(SONG_RANK_CLEARS[rank_clear]["location_id"])
        for character_rank_clear in ctx.interface.character_rank_clears:
            checked_locations.add(CHARACTER_RANK_CLEARS[character_rank_clear]["location_id"])

        #Check for basic clears on Hard difficulty
        for hard_song_clear in ctx.interface.hard_song_clears:
            checked_locations.add(HARD_SONG_CLEARS[hard_song_clear]["location_id"])
        for hard_character_clear in ctx.interface.hard_character_clears:
            checked_locations.add(HARD_CHARACTER_CLEARS[hard_character_clear]["location_id"])

        #Check for combo clears on Hard difficulty
        for hard_combo_clear in ctx.interface.hard_combo_clears:
            checked_locations.add(HARD_SONG_COMBO_CLEARS[hard_combo_clear]["location_id"])
        for hard_character_combo_clear in ctx.interface.hard_character_combo_clears:
            checked_locations.add(HARD_CHARACTER_COMBO_CLEARS[hard_character_combo_clear]["location_id"])

        #Check for A rank clears on Hard difficulty
        for hard_rank_clear in ctx.interface.hard_rank_clears:
            checked_locations.add(HARD_SONG_RANK_CLEARS[hard_rank_clear]["location_id"])
        for hard_character_rank_clear in ctx.interface.hard_character_rank_clears:
            checked_locations.add(HARD_CHARACTER_RANK_CLEARS[hard_character_rank_clear]["location_id"])

        #Full Band Clear
        if len(set(ctx.interface.characters_received)) >= 5: #Must have obtained all characters in order to start sending Full Band Clear checks
            for song in ctx.played_songs: #Must have at least played the song once in order to send Full Band Clear check
                if SONG_CLEARS[f"{song}: Clear"]["location_id"] in ctx.checked_locations and not SONG_COMPLETIONIST_CLEARS[f"{song}: Full Band Clear"]["location_id"] in ctx.checked_locations:
                    full_band_cleared = True
                    for character in CHARACTERS:
                        if full_band_cleared and not CHARACTER_CLEARS[f"{song}: Clear with {character}"]["location_id"] in ctx.checked_locations:
                            full_band_cleared = False

                    if full_band_cleared:
                        checked_locations.add(SONG_COMPLETIONIST_CLEARS[f"{song}: Full Band Clear"]["location_id"])
                
                if ctx.slot_data["hard_clear_locations"] > 1 and HARD_SONG_CLEARS[f"{song}: Clear on Hard"]["location_id"] in ctx.checked_locations and not HARD_SONG_COMPLETIONIST_CLEARS[f"{song}: Full Band Clear on Hard"]["location_id"] in ctx.checked_locations:
                    full_band_cleared = True
                    for character in CHARACTERS:
                        if full_band_cleared and not HARD_CHARACTER_CLEARS[f"{song}: Clear with {character} on Hard"]["location_id"] in ctx.checked_locations:
                            full_band_cleared = False

                    if full_band_cleared:
                        checked_locations.add(HARD_SONG_COMPLETIONIST_CLEARS[f"{song}: Full Band Clear on Hard"]["location_id"])

        new_songs = [song for song in ctx.interface.played_songs if song not in ctx.played_songs]
        if new_songs:
            ctx.played_songs.extend(new_songs)
            await ctx.send_msgs([{"cmd": "Set", "key": f"k-on_played_songs_{ctx.team}_{ctx.slot}", "default": [], "want_reply": False, "operations": [{"operation": "replace", "value": ctx.played_songs}]}])

        checked_locations = checked_locations.difference(ctx.checked_locations)

        #If there are unsent locations, send them now
        if checked_locations:
            await ctx.send_msgs([{"cmd" : "LocationChecks", "locations" : checked_locations}])

        #Init vars for receiving items
        collected_tokens = 0
        food_upgrades = 0
        collected_tapes = 0
        tension_upgrades = 0
        new_characters = False
        new_snacks = {}

        #Receive items from server
        for server_item in ctx.items_received:
            if not server_item.item in ctx.cached_received_items:
                if server_item.item in SNACK_NAME_FROM_ID:
                    snack_name = SNACK_NAME_FROM_ID[server_item.item]
                    if not snack_name in new_snacks:
                        new_snacks[snack_name] = 1                        
                    else:
                        new_snacks[snack_name] += 1
                elif server_item.item in SONG_NAME_FROM_ID:
                    ctx.interface.unlock_song(SONG_NAME_FROM_ID[server_item.item])
                    ctx.cached_received_items.add(server_item.item)
                elif server_item.item in PROP_NAME_FROM_ID:
                    ctx.interface.unlock_prop(PROP_NAME_FROM_ID[server_item.item])
                    ctx.cached_received_items.add(server_item.item)
                elif server_item.item in OUTFIT_NAME_FROM_ID:
                    ctx.interface.unlock_outfit(OUTFIT_NAME_FROM_ID[server_item.item])
                    ctx.cached_received_items.add(server_item.item)
                elif server_item.item in PLAYABLE_CHARACTER_NAME_FROM_ID:
                    ctx.interface.characters_received.append(PLAYABLE_CHARACTER_NAME_FROM_ID[server_item.item])
                    ctx.cached_received_items.add(server_item.item)
                    new_characters = True
                elif server_item.item == 301: #Happy End item
                    await ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
                    ctx.cached_received_items.add(server_item.item)   
                elif server_item.item == 700: #Teatime Token item
                    collected_tokens += 1
                elif server_item.item == 701: #Cassette Tape item
                    collected_tapes += 1
                elif server_item.item == 800: #Snack Upgrade item
                    food_upgrades += 1
                elif server_item.item == 302: #Hard Difficulty
                    ctx.interface.hard_unlocked = True
                else: #Unknown item received
                    ctx.cached_received_items.add(server_item.item)

        if collected_tokens > ctx.interface.token_count or collected_tapes > ctx.interface.tape_count: #Amount of Tokens or Tapes is higher than before
            ctx.interface.token_count = collected_tokens
            ctx.interface.tape_count = collected_tapes
            if collected_tokens >= ctx.slot_data["token_requirement"] and collected_tapes >= ctx.slot_data["tape_requirement"]: #Goal hit
                log_tokens(ctx)
        elif ctx.slot_data["token_requirement"] > 0 and ctx.slot_data["tape_requirement"] > 0 and not ctx.tokens_reported: #If Token count hasn't been reported yet (i.e. the client only just connected for the first time in the play session)
            log_tokens(ctx)
            ctx.tokens_reported = True
        
        ctx.interface.food_duration = ctx.slot_data["default_food_duration"] + (food_upgrades * 1)
        ctx.interface.tension_upgrade = tension_upgrades #Currently unused

        #Figure out which snacks have already been applied before giving them again
        if ctx.snack_cache_retrieved:
            for snack_name in new_snacks:
                updated_snack_cache = False
                if (not new_snacks[snack_name] in ctx.snack_cache) or (ctx.snack_cache[snack_name] < new_snacks[snack_name]):
                    if snack_name in ctx.snack_cache:
                        snacks_to_add = new_snacks[snack_name] - ctx.snack_cache[snack_name]
                    else:
                        snacks_to_add = new_snacks[snack_name]
                    ctx.interface.receive_snack(snack_name, snacks_to_add)
                    ctx.snack_cache[snack_name] = new_snacks[snack_name]
                    updated_snack_cache = True
                
                if updated_snack_cache:
                    await ctx.send_msgs([{"cmd": "Set", "key": f"k-on_snack_cache_{ctx.team}_{ctx.slot}", "default": {}, "want_reply": False, "operations": [{"operation": "replace", "value": ctx.snack_cache}]}])
                
        if new_characters: #If a new character has been unlocked
            log_characters(ctx) #Let the player know their current list of characters

        if ctx.deathlink_pending == True:
            await ctx.interface.deathlink_received()
            ctx.deathlink_pending = False
        elif "deathlink_enabled" in ctx.slot_data and ctx.slot_data["deathlink_enabled"] == True and ctx.interface.deaths > ctx.sent_deaths:
            ctx.sent_deaths = ctx.interface.deaths
            await ctx.send_death()
        
    elif not ctx.most_recent_instruction == "connect":
        ctx.most_recent_instruction = "connect"
        logger.info("You are not currently connected to an Archipelago server. Connect to an Archipelago server now!")

async def reconnect_game(ctx) -> None:
    if not ctx.most_recent_instruction == "ppsspp":
        ctx.most_recent_instruction = "ppsspp"
        logger.info("Communication with PPSSPP failed. Please ensure that PPSSPP is open and K-On! After School Live!! is loaded.")
    await asyncio.sleep(5)
    await ctx.interface.connect_to_ppsspp()

def log_characters(ctx) -> None:
    chars = [name.split(" ")[-1] for name in ctx.interface.characters_received]
    if not chars:
        return
    if len(chars) == 1:
        name_str = f"{chars[0]}."
    else:
        name_str = ", ".join(chars[:-1]) + f" and {chars[-1]}."
    logger.info(f"You can now play as {name_str}")

def log_tokens(ctx) -> None:
    tokens_needed = max(ctx.slot_data["token_requirement"] - ctx.interface.token_count, 0)
    tapes_needed = max(ctx.slot_data["tape_requirement"] - ctx.interface.tape_count, 0)

    token_count = ctx.interface.token_count
    tape_count = ctx.interface.tape_count
    token_req = ctx.slot_data["token_requirement"]
    tape_req = ctx.slot_data["tape_requirement"]
    outfits_required = ctx.slot_data["matching_outfits_goal"]

    inventory_items = []
    requirement_items = []

    if token_req > 0:
        inventory_items.append(f"{token_count} Teatime Tokens")
        requirement_items.append(f"{token_req} Teatime Tokens")
    if tape_req > 0:
        inventory_items.append(f"{tape_count} Cassette Tapes")
        requirement_items.append(f"{tape_req} Cassette Tapes")

    inventory_text = " and ".join(inventory_items)
    requirement_text = " and ".join(requirement_items)

    if outfits_required:
        requirement_text += " along with matching outfits equipped"

    if tokens_needed + tapes_needed == 0:
        advice_text = f"You can play {ctx.slot_data['goal_song']}"
        if outfits_required:
            advice_text += " after equipping matching outfits"
    else:
        needs = []
        if tokens_needed:
            needs.append(f"{tokens_needed} Teatime Tokens")
        if tapes_needed:
            needs.append(f"{tapes_needed} Cassette Tapes")
        advice_text = f"You still need {' and '.join(needs)}"

    logger.info(f"You currently have {inventory_text}. You need a total of {requirement_text} to unlock your goal song. {advice_text}!")

def launch() -> None:
    async def main() -> None:
        multiprocessing.freeze_support()

        parser = get_base_parser()
        args = parser.parse_args()

        ctx = KONContext(args.connect, args.password)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="Server Loop")

        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()

        ctx.interface_sync_task = asyncio.create_task(interface_sync_task(ctx), name="PPSSPP Sync")

        await ctx.exit_event.wait()
        ctx.server_address = None
        await ctx.interface.disconnect()
        await ctx.shutdown()

        if ctx.interface_sync_task:
            await ctx.interface_sync_task

    #Run Client
    import colorama

    colorama.init()
    asyncio.run(main())
    colorama.deinit()


if __name__ == '__main__':
    launch()