from typing import Dict, NamedTuple, Optional

from BaseClasses import Item, ItemClassification
from .Data import SONGS, SNACKS, PROPS, PLAYABLE_CHARACTERS, OUTFITS, PROGRESSION_PROPS

class KONItem(Item):
	game: str = "K-On! After School Live!!"

item_ids: Dict[str, int] = {
	"Happy End": 301,
	"Hard Difficulty": 302,
	"Teatime Token": 700,
	"Cassette Tape": 701,
	"Snack Upgrade": 800
}

for song in SONGS:
	item_ids[song] = SONGS[song]["item_id"]

for snack in SNACKS:
	item_ids[snack] = SNACKS[snack]["item_id"]

for prop in PROPS:
	if "item_id" in PROPS[prop]:
		if prop in PROGRESSION_PROPS:
			item_ids[prop] = PROPS[prop]["item_id"]
		else:
			item_ids[prop] = PROPS[prop]["item_id"]

for outfit in OUTFITS:
	if "item_id" in OUTFITS[outfit]:
		item_ids[outfit] = OUTFITS[outfit]["item_id"]

for playable_character in PLAYABLE_CHARACTERS:
	item_ids[playable_character] = PLAYABLE_CHARACTERS[playable_character]["item_id"]