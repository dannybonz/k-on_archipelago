from typing import Dict, NamedTuple, Optional

from BaseClasses import Location
from .Data import TUTORIAL_EVENTS, EVENTS, SONG_CLEARS, CHARACTER_CLEARS, SONG_COMPLETIONIST_CLEARS, SONG_RANK_CLEARS, SONG_COMBO_CLEARS, CHARACTER_RANK_CLEARS, CHARACTER_COMBO_CLEARS, HARD_SONG_CLEARS, HARD_CHARACTER_CLEARS, HARD_SONG_COMPLETIONIST_CLEARS, HARD_CHARACTER_COMBO_CLEARS, HARD_SONG_COMBO_CLEARS, HARD_SONG_RANK_CLEARS, HARD_CHARACTER_RANK_CLEARS

class KONLocation(Location):
    game: str = "K-On! After School Live!!"

class KONLocationData(NamedTuple):
    category: str
    address: Optional[int] = None

song_clear_location_table: Dict[str, KONLocationData] = {}
for song_clear_name in SONG_CLEARS:
    song_clear_location_table[song_clear_name] = KONLocationData("Song Clears", SONG_CLEARS[song_clear_name]["location_id"])

character_clear_location_table: Dict[str, KONLocationData] = {}
for character_clear_name in CHARACTER_CLEARS:
    character_clear_location_table[character_clear_name] = KONLocationData("Character Clears", CHARACTER_CLEARS[character_clear_name]["location_id"])

completionist_clear_location_table:  Dict[str, KONLocationData] = {}
for completionist_clear_name in SONG_COMPLETIONIST_CLEARS:
    completionist_clear_location_table[completionist_clear_name] = KONLocationData("Completionist Clears", SONG_COMPLETIONIST_CLEARS[completionist_clear_name]["location_id"])

rank_location_table:  Dict[str, KONLocationData] = {}
for rank_name in SONG_RANK_CLEARS:
    rank_location_table[rank_name] = KONLocationData("A Ranks", SONG_RANK_CLEARS[rank_name]["location_id"])

combo_location_table:  Dict[str, KONLocationData] = {}
for combo_name in SONG_COMBO_CLEARS:
    combo_location_table[combo_name] = KONLocationData("Combos", SONG_COMBO_CLEARS[combo_name]["location_id"])

character_rank_location_table:  Dict[str, KONLocationData] = {}
for character_rank_name in CHARACTER_RANK_CLEARS:
    character_rank_location_table[character_rank_name] = KONLocationData("Character A Ranks", CHARACTER_RANK_CLEARS[character_rank_name]["location_id"])

character_combo_location_table:  Dict[str, KONLocationData] = {}
for character_combo_name in CHARACTER_COMBO_CLEARS:
    character_combo_location_table[character_combo_name] = KONLocationData("Character Combos", CHARACTER_COMBO_CLEARS[character_combo_name]["location_id"])

hard_song_clear_location_table: Dict[str, KONLocationData] = {}
for hard_song_clear_name in HARD_SONG_CLEARS:
    hard_song_clear_location_table[hard_song_clear_name] = KONLocationData("Hard Song Clears", HARD_SONG_CLEARS[hard_song_clear_name]["location_id"])

hard_character_clear_location_table: Dict[str, KONLocationData] = {}
for hard_character_clear_name in HARD_CHARACTER_CLEARS:
    hard_character_clear_location_table[hard_character_clear_name] = KONLocationData("Hard Character Clears", HARD_CHARACTER_CLEARS[hard_character_clear_name]["location_id"])

hard_completionist_clear_location_table:  Dict[str, KONLocationData] = {}
for hard_completionist_clear_name in HARD_SONG_COMPLETIONIST_CLEARS:
    hard_completionist_clear_location_table[hard_completionist_clear_name] = KONLocationData("Hard Completionist Clears", HARD_SONG_COMPLETIONIST_CLEARS[hard_completionist_clear_name]["location_id"])

hard_rank_location_table:  Dict[str, KONLocationData] = {}
for hard_rank_name in HARD_SONG_RANK_CLEARS:
    hard_rank_location_table[hard_rank_name] = KONLocationData("Hard A Ranks", HARD_SONG_RANK_CLEARS[hard_rank_name]["location_id"])

hard_combo_location_table:  Dict[str, KONLocationData] = {}
for hard_combo_name in HARD_SONG_COMBO_CLEARS:
    hard_combo_location_table[hard_combo_name] = KONLocationData("Hard Combos", HARD_SONG_COMBO_CLEARS[hard_combo_name]["location_id"])

hard_character_rank_location_table:  Dict[str, KONLocationData] = {}
for hard_character_rank_name in HARD_CHARACTER_RANK_CLEARS:
    hard_character_rank_location_table[hard_character_rank_name] = KONLocationData("Hard Character A Ranks", HARD_CHARACTER_RANK_CLEARS[hard_character_rank_name]["location_id"])

hard_character_combo_location_table:  Dict[str, KONLocationData] = {}
for hard_character_combo_name in HARD_CHARACTER_COMBO_CLEARS:
    hard_character_combo_location_table[hard_character_combo_name] = KONLocationData("Hard Character Combos", HARD_CHARACTER_COMBO_CLEARS[hard_character_combo_name]["location_id"])

event_location_table: Dict[str, KONLocationData] = {}
easy_event_location_table: Dict[str, KONLocationData] = {}
for event_name in EVENTS:
    event_location_table[event_name] = KONLocationData("Event Clears", EVENTS[event_name]["location_id"])
    if event_name in TUTORIAL_EVENTS:
        easy_event_location_table[event_name] = KONLocationData("Event Clears", EVENTS[event_name]["location_id"])

full_location_table: Dict[str, KONLocationData] = {}
for table in [song_clear_location_table, character_clear_location_table, event_location_table, completionist_clear_location_table, rank_location_table, combo_location_table, character_rank_location_table, character_combo_location_table, hard_song_clear_location_table, hard_completionist_clear_location_table, hard_character_clear_location_table, hard_rank_location_table, hard_combo_location_table, hard_character_combo_location_table, hard_character_rank_location_table]:
    full_location_table.update(table)