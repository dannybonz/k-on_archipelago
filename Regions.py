from typing import Dict, List, NamedTuple, Optional

from BaseClasses import Region
from worlds.AutoWorld import World
from .Locations import KONLocation, song_clear_location_ids, character_clear_location_ids, event_location_ids, completionist_clear_location_ids, rank_location_ids, combo_location_ids, character_rank_location_ids, character_combo_location_ids, hard_song_clear_location_ids, hard_combo_location_ids, hard_rank_location_ids, hard_character_clear_location_ids, hard_completionist_clear_location_ids, hard_character_combo_location_ids, hard_character_rank_location_ids
from .Data import SONGS

def create_regions(world: World) -> None:
	player = world.player
	multiworld = world.multiworld
	
	location_ids: Dict[str, int] = {}

	location_ids.update(song_clear_location_ids)
	location_ids.update(character_clear_location_ids)
	location_ids.update(completionist_clear_location_ids)

	if (world.options.challenge_locations.value != 0):
		location_ids.update(rank_location_ids)
		location_ids.update(combo_location_ids)
	if (world.options.challenge_locations.value == 2):
		location_ids.update(character_rank_location_ids)
		location_ids.update(character_combo_location_ids)

	if (world.options.hard_clear_locations.value != 0):
		location_ids.update(hard_song_clear_location_ids)
	if (world.options.hard_clear_locations.value == 2):
		location_ids.update(hard_character_clear_location_ids)
		location_ids.update(hard_completionist_clear_location_ids)

	if (world.options.hard_challenge_locations.value != 0):
		location_ids.update(hard_rank_location_ids)
		location_ids.update(hard_combo_location_ids)
	if (world.options.hard_challenge_locations.value == 2):
		location_ids.update(hard_character_rank_location_ids)
		location_ids.update(hard_character_combo_location_ids)

	if (world.options.event_locations.value):
		location_ids.update(event_location_ids)

	if not world.options.full_band_goal.value: #Remove locations that cannot be completed without having already completed your seed
			location_ids = {
				k: v for k, v in location_ids.items()
				if not (k.startswith(world.goal_song) and k != f"{world.goal_song}: Clear")
			}

	menu_region = Region("Menu", player, multiworld)
	multiworld.regions.append(menu_region)

	for x in range(0, len(SONGS)):
		song_title = list(SONGS.keys())[x]
		song_region = Region(song_title, player, multiworld)
		song_location_names = list(filter(lambda x: f"{song_title}: " in x, location_ids))
		song_region.locations += [KONLocation(player, location, location_ids[location], song_region) for location in song_location_names]
		menu_region.connect(song_region)
		multiworld.regions.append(song_region)

	events_region = Region("Events", player, multiworld)
	event_location_names = list(filter(lambda x: f"Event: " in x, location_ids))
	events_region.locations += [KONLocation(player, location, location_ids[location], events_region) for location in event_location_names]
	multiworld.regions.append(events_region)
	menu_region.connect(events_region)
