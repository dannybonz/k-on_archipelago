from typing import Dict, List, NamedTuple, Optional

from BaseClasses import Region
from worlds.AutoWorld import World
from .Locations import KONLocation, easy_event_location_table, song_clear_location_table, character_clear_location_table, event_location_table, completionist_clear_location_table, rank_location_table, combo_location_table, character_rank_location_table, character_combo_location_table, hard_song_clear_location_table, hard_combo_location_table, hard_rank_location_table, hard_character_clear_location_table, hard_completionist_clear_location_table, hard_character_combo_location_table, hard_character_rank_location_table
from .Data import SONGS

class KONRegionData(NamedTuple):
	locations: Optional[List[str]]
	region_exits: Optional[List[str]]

class KONLocationData(NamedTuple):
    category: str
    address: Optional[int] = None

def create_regions(world: World) -> None:
	player = world.player
	multiworld = world.multiworld
	
	location_table: Dict[str, KONLocationData] = {}

	location_table.update(song_clear_location_table)
	location_table.update(character_clear_location_table)
	location_table.update(completionist_clear_location_table)

	if (world.options.challenge_locations.value != 0):
		location_table.update(rank_location_table)
		location_table.update(combo_location_table)
	if (world.options.challenge_locations.value == 2):
		location_table.update(character_rank_location_table)
		location_table.update(character_combo_location_table)

	if (world.options.hard_clear_locations.value != 0):
		location_table.update(hard_song_clear_location_table)
	if (world.options.hard_clear_locations.value == 2):
		location_table.update(hard_character_clear_location_table)
		location_table.update(hard_completionist_clear_location_table)

	if (world.options.hard_challenge_locations.value != 0):
		location_table.update(hard_rank_location_table)
		location_table.update(hard_combo_location_table)
	if (world.options.hard_challenge_locations.value == 2):
		location_table.update(hard_character_rank_location_table)
		location_table.update(hard_character_combo_location_table)

	if (world.options.event_locations.value):
		location_table.update(event_location_table)
	else:
		location_table.update(easy_event_location_table)

	if not world.options.full_band_goal.value: #Remove locations that cannot be completed without having already completed your seed
			location_table = {
				k: v for k, v in location_table.items()
				if not (k.startswith(world.goal_song) and k != f"{world.goal_song}: Clear")
			}

	menu_region = Region("Menu", player, multiworld)
	multiworld.regions.append(menu_region)

	for x in range(0, len(SONGS)):
		song_title = list(SONGS.keys())[x]
		song_region = Region(song_title, player, multiworld)
		song_location_names = list(filter(lambda x: f"{song_title}: " in x, location_table))
		song_region.locations += [KONLocation(player, location, location_table[location].address, song_region) for location in song_location_names]
		menu_region.connect(song_region)
		multiworld.regions.append(song_region)

	events_region = Region("Events", player, multiworld)
	event_location_names = list(filter(lambda x: f"Event: " in x, location_table))
	events_region.locations += [KONLocation(player, location, location_table[location].address, events_region) for location in event_location_names]
	multiworld.regions.append(events_region)
	menu_region.connect(events_region)
