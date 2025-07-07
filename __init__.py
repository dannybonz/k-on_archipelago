from typing import Dict, List

from BaseClasses import Item, ItemClassification
from worlds.AutoWorld import WebWorld, World
from worlds.LauncherComponents import Component, components, launch_subprocess, Type
from .Items import KONItem, KONItemData, item_table
from .Locations import full_location_table
from .Options import KONOptions
from .Regions import create_regions
from .Rules import set_rules
from .Data import SONGS, PLAYABLE_CHARACTERS, SONG_CLEARS, SNACKS, PROPS, CHARACTERS, OUTFITS, PROGRESSION_PROPS, SONG_CLEARS, SONG_COMPLETIONIST_CLEARS, SONG_COMBO_CLEARS, CHARACTER_CLEARS, CHARACTER_COMBO_CLEARS, CHARACTER_RANK_CLEARS, SONG_RANK_CLEARS, EVENTS, HARD_SONG_CLEARS, HARD_SONG_COMPLETIONIST_CLEARS, HARD_SONG_COMBO_CLEARS, HARD_CHARACTER_CLEARS, HARD_CHARACTER_COMBO_CLEARS, HARD_CHARACTER_RANK_CLEARS, HARD_SONG_RANK_CLEARS, UNIQUE_OUTFIT_SETS
from Options import OptionError

#Identifier for Archipelago to recognize and run the client
def run_client() -> None:
    from .Client import launch
    launch_subprocess(launch, name="KONClient")

components.append(Component("K-On! After School Live!! Client", func=run_client, component_type=Type.CLIENT))

class KONWebWorld(WebWorld):
    theme = "partyTime"
    
    '''
    setup = Tutorial(
        tutorial_name = "Setup Guide",
        description = "A guide to setting up the K-On! After School Live!! Archipelago Multiworld",
        language = "English",
        file_name = "setup.md",
        link = "setup/en",
        authors = ["Bonzorio"]
    )
    tutorials = [setup]
    '''

class KONWorld(World):
    """
    K-On! After School Live!!
    """
    game = "K-On! After School Live!!"
    web = KONWebWorld()
    options_dataclass = KONOptions
    options: KONOptions

    junk_pool: Dict[str, int]
    topology_present = True

    item_name_to_id = {name: data.address for name, data in item_table.items()}
    location_name_to_id = {name: data.address for name, data in full_location_table.items()}

    def generate_early(self):
        self.possible_songs = list(SONGS.keys())
        self.random.shuffle(self.possible_songs)
        self.goal_song = self.possible_songs.pop(-1)

        self.starting_songs = [self.possible_songs.pop() for _ in range(self.options.starting_songs_amount.value)]
        for i in range(int(len(self.possible_songs) * 0.25)):
            self.multiworld.early_items[self.player][self.possible_songs[i]] = 1

        self.possible_characters = list(PLAYABLE_CHARACTERS.keys())
        self.random.shuffle(self.possible_characters)
        self.starting_characters = [self.possible_characters.pop(0) for _ in range(self.options.starting_characters_amount.value)]

        self.starting_outfits = []
        for character in CHARACTERS:
            matching_outfits = [outfit for outfit in OUTFITS if outfit.startswith(character)]
            self.starting_outfits.append(self.random.choice(matching_outfits))

        self.token_count = self.options.teatime_tokens.value
        self.tape_requirement = self.options.tape_requirement.value

        if self.token_count == 0 and self.tape_requirement == 0:
            self.tape_requirement = 18

        forced_item_count = len(self.possible_songs) + len(self.possible_characters) + self.options.snack_upgrades
        if self.options.event_locations.value:
            forced_item_count += len(PROGRESSION_PROPS)
        if self.options.matching_outfits_goal.value:
            forced_item_count += 5

        location_count = (len(SONG_COMPLETIONIST_CLEARS) - 1) + (len(CHARACTER_CLEARS) - 5)
        if self.tape_requirement == 0:
            location_count = len(SONG_CLEARS) - 1 #-1 for the goal clear
        if self.options.event_locations.value:
            location_count += len(EVENTS)
        if self.options.challenge_locations.value != 0:
            location_count += (len(SONG_COMBO_CLEARS) - 1) + (len(SONG_RANK_CLEARS) - 1)
        if self.options.challenge_locations.value == 2:
            location_count += (len(CHARACTER_COMBO_CLEARS) - 5) + (len(CHARACTER_RANK_CLEARS) - 5)
        if self.options.hard_clear_locations.value != 0:
            location_count += len(HARD_SONG_CLEARS) - 1
        if self.options.hard_clear_locations.value == 2:
            location_count += (len(HARD_SONG_COMPLETIONIST_CLEARS) - 1) + (len(HARD_CHARACTER_CLEARS) - 5)
        if self.options.hard_challenge_locations.value != 0:
            location_count += (len(HARD_SONG_COMBO_CLEARS) - 5) + (len(HARD_SONG_RANK_CLEARS) - 5)
        if self.options.hard_challenge_locations.value == 2:
            location_count += (len(HARD_CHARACTER_COMBO_CLEARS) - 5) + (len(HARD_CHARACTER_RANK_CLEARS) - 5)

        if self.token_count > 0:
            if self.token_count > location_count - forced_item_count: #Lowers the number of Tokens if enough locations do not exist
                self.token_count = location_count - forced_item_count
                if self.token_count < 1:
                    self.token_count = 1

            self.token_requirement = int(self.token_count * (self.options.token_percentage.value/100))
            if self.token_requirement == 0:
                self.token_requirement = 1
        else:
            self.token_requirement = 0

        if (location_count - (forced_item_count + self.token_count) < 0):
            raise OptionError("Not enough locations are available. Adjust your options to include more locations, then generate again.")
    
    def fill_slot_data(self) -> dict:
        if self.options.snack_upgrades.value > 0:
            snack_upgrades_enabled = True
            allowed_starting_duration = 30 - (self.options.snack_upgrades.value * 1)
            default_food_duration = max(min(15, allowed_starting_duration), 4)
        else:
            snack_upgrades_enabled = False
            default_food_duration = 15

        slot_data_dict = {"full_band_goal": self.options.full_band_goal.value, "matching_outfits_goal": self.options.matching_outfits_goal.value, "challenge_locations": self.options.challenge_locations.value, "hard_challenge_locations": self.options.hard_challenge_locations.value, "hard_clear_locations": self.options.hard_clear_locations.value, "event_locations": self.options.event_locations.value, "goal_song": self.goal_song, "token_requirement": self.token_requirement, "tape_requirement": self.options.tape_requirement.value, "default_food_duration": default_food_duration, "snack_cache": {}, "snack_upgrades_enabled": snack_upgrades_enabled}
        return slot_data_dict

    def create_items(self) -> None:
        item_pool: List[KONItem] = []
        junk_pool: List[KONItem] = []

        for starting_song in self.starting_songs:
            self.multiworld.push_precollected(self.create_item(starting_song))

        for starting_char in self.starting_characters:
            self.multiworld.push_precollected(self.create_item(starting_char))

        for starting_outfit in self.starting_outfits:
            self.multiworld.push_precollected(self.create_item(starting_outfit))

        if self.options.full_band_goal.value:
            goal_region = self.multiworld.get_region(self.goal_song, self.player)
            self.multiworld.get_location(f"{self.goal_song}: Full Band Clear", self.player).place_locked_item(self.create_item("Happy End")) 
        else:
            self.multiworld.get_location(f"{self.goal_song}: Clear", self.player).place_locked_item(self.create_item("Happy End")) 

        if self.tape_requirement > 0:
            for song in SONGS:
                if not song == self.goal_song:
                    self.multiworld.get_location(f"{song}: Clear", self.player).place_locked_item(self.create_item("Cassette Tape"))

        if self.options.matching_outfits_goal.value: #If using the matching outfits goal, we need to ensure that at least one complete outfit set is available in the pool
            possible_guaranteed_outfits = []
            for outfit in UNIQUE_OUTFIT_SETS:
                permitted = True
                for starting_outfit in self.starting_outfits:
                    if outfit in starting_outfit:
                        permitted = False
                if permitted:
                    possible_guaranteed_outfits.append(outfit)
            guaranteed_outfit_type = self.random.choice(possible_guaranteed_outfits) #This outfit type is guaranteed to be available for all characters

        total_locations = len(self.multiworld.get_unfilled_locations(self.player))

        for x in range(0, self.options.snack_upgrades.value):
            item_pool.append(self.create_item("Snack Upgrade"))

        for x in range(0, self.token_count):
            item_pool.append(self.create_item("Teatime Token"))

        for name, data in item_table.items():
            if (data.category == "Characters" and name in self.possible_characters) or (data.category == "Songs" and name in self.possible_songs) or (data.category == "Outfits" and self.options.matching_outfits_goal.value and guaranteed_outfit_type in name):
                item_pool.append(self.create_item(name))
            elif data.category == "Props":
                if self.options.event_locations.value:
                    if data.classification == ItemClassification.filler:
                        junk_pool.append(name)
                    else:
                        item_pool.append(self.create_item(name))
                else:
                    item_table[name] = KONItemData("Props", PROPS[name]["item_id"], ItemClassification.filler)
                    junk_pool.append(name)
            elif data.category == "Outfits" and self.options.matching_outfits_goal.value and not name in ["Azusa's Old Uniform Outfit", "Yui's School Swimsuit Outfit"]:
                item_table[name] = KONItemData("Outfits", OUTFITS[name]["item_id"], ItemClassification.progression)
                junk_pool.append(name) #Even though we mark these progression items, they are not *necessarily* required as long as there is one complete set in the pool. It's fine if they don't get included in the generation.
            elif data.category in ["Outfits", "Accessories"] and not name in self.starting_outfits:
                junk_pool.append(name)

        #Progression snacks if Event locations are enabled
        if self.options.event_locations.value:
            item_table["Sweets"] = KONItemData("Snacks", SNACKS["Sweets"]["item_id"], ItemClassification.progression)
            item_table["Taiyaki"] = KONItemData("Snacks", SNACKS["Taiyaki"]["item_id"], ItemClassification.progression)
            item_pool.append(self.create_item("Sweets"))
            item_pool.append(self.create_item("Taiyaki"))

        #Approximately a third of the junk pool is snacks 
        number_of_snacks = (total_locations - len(item_pool)) / 3
        amount_per_snack = int(number_of_snacks / len(SNACKS))
        for snack in SNACKS:
            for x in range (0, amount_per_snack):
                item_pool.append(self.create_item(snack))

        #Fill remaining spots with outfits and useless collectibles
        self.random.shuffle(junk_pool)        
        while len(item_pool) < total_locations - 1 and len(junk_pool) > 0:
            item_pool.append(self.create_item(junk_pool.pop()))

        #If we ran out of outfits and collectibles, fill the remaining spots with even more random snacks
        while len(item_pool) < total_locations:
            item_pool.append(self.create_item(self.random.choice(list(SNACKS.keys()))))

        self.multiworld.itempool += item_pool

    def get_filler_item_name(self) -> str:
        return self.random.choice(list(SNACKS.keys()))
    
    def create_item(self, name: str) -> KONItem:
        return KONItem(name, item_table[name].classification, item_table[name].address, self.player)

    def set_rules(self) -> None:
        set_rules(self)

    def create_regions(self) -> None:
        create_regions(self)