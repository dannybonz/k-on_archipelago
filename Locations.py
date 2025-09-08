from typing import Dict, NamedTuple, Optional

from BaseClasses import Location
from .Data import EVENTS, SONG_CLEARS, CHARACTER_CLEARS, SONG_COMPLETIONIST_CLEARS, SONG_RANK_CLEARS, SONG_COMBO_CLEARS, CHARACTER_RANK_CLEARS, CHARACTER_COMBO_CLEARS, HARD_SONG_CLEARS, HARD_CHARACTER_CLEARS, HARD_SONG_COMPLETIONIST_CLEARS, HARD_CHARACTER_COMBO_CLEARS, HARD_SONG_COMBO_CLEARS, HARD_SONG_RANK_CLEARS, HARD_CHARACTER_RANK_CLEARS

class KONLocation(Location):
    game: str = "K-On! After School Live!!"

song_clear_location_ids: Dict[str, int] = {}
for song_clear_name in SONG_CLEARS:
    song_clear_location_ids[song_clear_name] = SONG_CLEARS[song_clear_name]["location_id"]

character_clear_location_ids: Dict[str, int] = {}
for character_clear_name in CHARACTER_CLEARS:
    character_clear_location_ids[character_clear_name] = CHARACTER_CLEARS[character_clear_name]["location_id"]

completionist_clear_location_ids:  Dict[str, int] = {}
for completionist_clear_name in SONG_COMPLETIONIST_CLEARS:
    completionist_clear_location_ids[completionist_clear_name] = SONG_COMPLETIONIST_CLEARS[completionist_clear_name]["location_id"]

rank_location_ids:  Dict[str, int] = {}
for rank_name in SONG_RANK_CLEARS:
    rank_location_ids[rank_name] = SONG_RANK_CLEARS[rank_name]["location_id"]

combo_location_ids:  Dict[str, int] = {}
for combo_name in SONG_COMBO_CLEARS:
    combo_location_ids[combo_name] = SONG_COMBO_CLEARS[combo_name]["location_id"]

character_rank_location_ids:  Dict[str, int] = {}
for character_rank_name in CHARACTER_RANK_CLEARS:
    character_rank_location_ids[character_rank_name] = CHARACTER_RANK_CLEARS[character_rank_name]["location_id"]

character_combo_location_ids:  Dict[str, int] = {}
for character_combo_name in CHARACTER_COMBO_CLEARS:
    character_combo_location_ids[character_combo_name] = CHARACTER_COMBO_CLEARS[character_combo_name]["location_id"]

hard_song_clear_location_ids: Dict[str, int] = {}
for hard_song_clear_name in HARD_SONG_CLEARS:
    hard_song_clear_location_ids[hard_song_clear_name] = HARD_SONG_CLEARS[hard_song_clear_name]["location_id"]

hard_character_clear_location_ids: Dict[str, int] = {}
for hard_character_clear_name in HARD_CHARACTER_CLEARS:
    hard_character_clear_location_ids[hard_character_clear_name] = HARD_CHARACTER_CLEARS[hard_character_clear_name]["location_id"]

hard_completionist_clear_location_ids:  Dict[str, int] = {}
for hard_completionist_clear_name in HARD_SONG_COMPLETIONIST_CLEARS:
    hard_completionist_clear_location_ids[hard_completionist_clear_name] = HARD_SONG_COMPLETIONIST_CLEARS[hard_completionist_clear_name]["location_id"]

hard_rank_location_ids:  Dict[str, int] = {}
for hard_rank_name in HARD_SONG_RANK_CLEARS:
    hard_rank_location_ids[hard_rank_name] = HARD_SONG_RANK_CLEARS[hard_rank_name]["location_id"]

hard_combo_location_ids:  Dict[str, int] = {}
for hard_combo_name in HARD_SONG_COMBO_CLEARS:
    hard_combo_location_ids[hard_combo_name] = HARD_SONG_COMBO_CLEARS[hard_combo_name]["location_id"]

hard_character_rank_location_ids:  Dict[str, int] = {}
for hard_character_rank_name in HARD_CHARACTER_RANK_CLEARS:
    hard_character_rank_location_ids[hard_character_rank_name] = HARD_CHARACTER_RANK_CLEARS[hard_character_rank_name]["location_id"]

hard_character_combo_location_ids:  Dict[str, int] = {}
for hard_character_combo_name in HARD_CHARACTER_COMBO_CLEARS:
    hard_character_combo_location_ids[hard_character_combo_name] = HARD_CHARACTER_COMBO_CLEARS[hard_character_combo_name]["location_id"]

event_location_ids: Dict[str, int] = {}
for event_name in EVENTS:
    event_location_ids[event_name] = EVENTS[event_name]["location_id"]

all_location_ids: Dict[str, int] = {}
for location_ids in [song_clear_location_ids, character_clear_location_ids, event_location_ids, completionist_clear_location_ids, rank_location_ids, combo_location_ids, character_rank_location_ids, character_combo_location_ids, hard_song_clear_location_ids, hard_completionist_clear_location_ids, hard_character_clear_location_ids, hard_rank_location_ids, hard_combo_location_ids, hard_character_combo_location_ids, hard_character_rank_location_ids]:
    all_location_ids.update(location_ids)