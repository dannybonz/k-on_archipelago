from typing import Dict, List, Any

from BaseClasses import Item, ItemClassification
from worlds.AutoWorld import WebWorld, World
from worlds.LauncherComponents import Component, components, launch_subprocess, Type
from .Items import KONItem, item_ids
from .Locations import all_location_ids
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

    item_name_to_id = item_ids
    location_name_to_id = all_location_ids

    ut_can_gen_without_yaml = True

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

        if self.options.token_percentage.value == 0 or self.options.teatime_tokens.value == 0:
            self.token_count = 0
            self.token_requirement = 0
        else:
            self.token_count = self.options.teatime_tokens.value
            self.token_requirement = int(self.token_count * (self.options.token_percentage.value/100))
            if self.token_requirement == 0:
                self.token_requirement = 1

        self.tape_requirement = self.options.tape_requirement.value
        if self.token_count == 0 and self.tape_requirement == 0 and not self.options.matching_outfits_goal.value:
            self.tape_requirement = 18 

        if self.options.matching_outfits_goal.value:
            possible_goal_outfits = [outfit for outfit in UNIQUE_OUTFIT_SETS if all(outfit not in starting_outfit for starting_outfit in self.starting_outfits)]
            self.goal_outfit = self.random.choice(possible_goal_outfits)
        else:
            self.goal_outfit = None

        if hasattr(self.multiworld, "re_gen_passthrough"): #If generated through Universal Tracker passthrough
            slot_data: dict = self.multiworld.re_gen_passthrough[self.game]
            self.goal_song = slot_data["goal_song"]
            self.options.full_band_goal.value = slot_data["full_band_goal"]
            self.options.matching_outfits_goal.value = slot_data["matching_outfits_goal"]
            self.options.challenge_locations.value = slot_data["challenge_locations"]
            self.options.hard_challenge_locations.value = slot_data["hard_challenge_locations"]
            self.options.hard_clear_locations.value = slot_data["hard_clear_locations"]
            self.options.event_locations.value = slot_data["event_locations"]
            self.tape_requirement = slot_data["tape_requirement"]
            self.token_requirement = slot_data["token_requirement"]
            self.goal_outfit = slot_data["goal_outfit"]

    def fill_slot_data(self) -> dict:
        if self.options.snack_upgrades.value > 0:
            snack_upgrades_enabled = True
            allowed_starting_duration = 30 - (self.options.snack_upgrades.value * 1)
            default_food_duration = max(min(15, allowed_starting_duration), 4)
        else:
            snack_upgrades_enabled = False
            default_food_duration = 15

        slot_data_dict = {"goal_outfit": self.goal_outfit, "full_band_goal": self.options.full_band_goal.value, "matching_outfits_goal": self.options.matching_outfits_goal.value, "challenge_locations": self.options.challenge_locations.value, "hard_challenge_locations": self.options.hard_challenge_locations.value, "hard_clear_locations": self.options.hard_clear_locations.value, "event_locations": self.options.event_locations.value, "goal_song": self.goal_song, "token_requirement": self.token_requirement, "tape_requirement": self.options.tape_requirement.value, "default_food_duration": default_food_duration, "snack_upgrades_enabled": snack_upgrades_enabled, "deathlink_enabled": self.options.death_link.value}
        return slot_data_dict

    @staticmethod
    def interpret_slot_data(slot_data: dict[str:Any]) -> dict[str:Any]:
        return slot_data

    def pick_progression_items(self):
        progression_item_names = []

        if self.options.shuffle_hard_difficulty.value and not (self.options.hard_challenge_locations.value == 0 and self.options.hard_clear_locations.value == 0):
            progression_item_names.append("Hard Difficulty")

        progression_item_names += [song for song in SONGS if song not in self.starting_songs and song != self.goal_song]
        progression_item_names += [playable_character for playable_character in PLAYABLE_CHARACTERS if playable_character not in self.starting_characters]

        if self.options.matching_outfits_goal.value:
            progression_item_names += [f"{character}'s {self.goal_outfit}" for character in CHARACTERS]

        if self.options.event_locations.value:
            progression_item_names += PROGRESSION_PROPS

        if self.token_count > 0:
            progression_item_names += ["Teatime Token"] * self.token_count

        return progression_item_names

    def pick_useful_items(self):
        useful_item_names = []

        if self.options.shuffle_hard_difficulty.value and (self.options.hard_challenge_locations.value == 0 and self.options.hard_clear_locations.value == 0):
            useful_item_names.append("Hard Difficulty")

        useful_item_names += ["Snack Upgrade"] * self.options.snack_upgrades.value

        return useful_item_names

    def pick_filler_items(self, number_of_fillers):
        filler_item_names = []

        number_of_snacks = (number_of_fillers) / 3
        amount_per_snack = int(number_of_snacks / len(SNACKS))
        for snack in SNACKS:
            for x in range (0, amount_per_snack):
                filler_item_names.append(snack)

        if not self.options.event_locations.value:
            filler_props = [prop for prop in PROPS.keys() if "item_id" in PROPS[prop]]
        else:
            filler_props = [prop for prop in PROPS.keys() if ("item_id" in PROPS[prop] and prop not in PROGRESSION_PROPS)]
                
        if not self.options.matching_outfits_goal:
            filler_outfits = list(OUTFITS.keys())
        else:
            excluded_outfits = [f"{self.random.choice(['Yui', 'Mio', 'Ritsu', 'Mugi', 'Azusa'])}'s {outfit}" for outfit in UNIQUE_OUTFIT_SETS]                
            filler_outfits = [outfit for outfit in OUTFITS if (not self.goal_outfit in outfit) and (not outfit in excluded_outfits)]          

        potential_filler = filler_props + filler_outfits
        self.random.shuffle(potential_filler)
        while len(filler_item_names) < number_of_fillers and len(potential_filler) > 0:
            filler_item_names.append(potential_filler.pop())

        while len(filler_item_names) < number_of_fillers:
            filler_item_names.append(self.random.choice(list(SNACKS.keys())))

        return filler_item_names

    def create_items(self) -> None:
        item_pool: List[KONItem] = []
        self.progression_item_names: List[str] = []
        self.useful_item_names: List[str] = []
        self.filler_item_names: List[str] = []
        self.preplaced_progression = ["Happy End", "Cassette Tape"] + self.starting_characters + self.starting_songs

        #Precollected items
        for starting_song in self.starting_songs:
            self.multiworld.push_precollected(self.create_item(starting_song))
        for playable_character in self.starting_characters:
            self.multiworld.push_precollected(self.create_item(playable_character))
        for starting_outfit in self.starting_outfits:
            self.multiworld.push_precollected(self.create_item(starting_outfit))
        if not self.options.shuffle_hard_difficulty.value:
            self.preplaced_progression.append("Hard Difficulty")
            self.multiworld.push_precollected(self.create_item("Hard Difficulty"))

        #Locked items
        if self.options.full_band_goal.value:
            goal_region = self.multiworld.get_region(self.goal_song, self.player)
            self.multiworld.get_location(f"{self.goal_song}: Full Band Clear", self.player).place_locked_item(self.create_item("Happy End")) 
        else:
            self.multiworld.get_location(f"{self.goal_song}: Clear", self.player).place_locked_item(self.create_item("Happy End")) 

        if self.tape_requirement > 0:
            for song in SONGS:
                if not song == self.goal_song:
                    self.multiworld.get_location(f"{song}: Clear", self.player).place_locked_item(self.create_item("Cassette Tape"))

        self.progression_item_names = self.pick_progression_items()
        self.useful_item_names = self.pick_useful_items()

        total_locations = len(self.multiworld.get_unfilled_locations(self.player))
        if len(self.progression_item_names + self.useful_item_names) > total_locations:
            raise OptionError(f"Not enough locations are available. Adjust your options to include more locations, then generate again.")
        
        self.filler_item_names = self.pick_filler_items(total_locations - len(self.progression_item_names + self.useful_item_names))

        for item in self.progression_item_names + self.useful_item_names + self.filler_item_names:
            item_pool.append(self.create_item(item))

        self.multiworld.itempool += item_pool

    def get_filler_item_name(self) -> str:
        return self.random.choice(list(SNACKS.keys()))
    
    def create_item(self, name: str) -> KONItem:
        if name in self.progression_item_names + self.preplaced_progression:
            item_classification = ItemClassification.progression
        elif name in self.useful_item_names:
            item_classification = ItemClassification.useful
        else:
            item_classification = ItemClassification.filler

        return KONItem(name, item_classification, item_ids[name], self.player)

    def set_rules(self) -> None:
        set_rules(self)

    def create_regions(self) -> None:
        create_regions(self)