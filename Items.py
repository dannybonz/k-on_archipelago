from typing import Dict, NamedTuple, Optional

from BaseClasses import Item, ItemClassification
from .Data import SONGS, SNACKS, PROPS, PLAYABLE_CHARACTERS, OUTFITS, PROGRESSION_PROPS

class KONItem(Item):
	game: str = "K-On! After School Live!!"

class KONItemData(NamedTuple):
	category: str
	address: Optional[int] = None
	classification: ItemClassification = ItemClassification.filler
	max_quantity: int = 1
	weight: int = 1

def get_items_by_category(category: str) -> Dict[str, KONItemData]:
	item_dict: Dict[str, KONItemData] = {}
	for name, data in item_table.items():
		if data.category == category:
			item_dict.setdefault(name, data)

	return item_dict

item_table: Dict[str, KONItemData] = {
	#Victory
	"Happy End": KONItemData("Victory", 301, ItemClassification.progression),

	#Progression
	"Teatime Token": KONItemData("Token", 700, ItemClassification.progression),
	"Cassette Tape": KONItemData("Token", 701, ItemClassification.progression),

	#Upgrades
	"Snack Upgrade": KONItemData("Upgrade", 800, ItemClassification.useful),
	"High Tension Upgrade": KONItemData("Upgrade", 801, ItemClassification.useful),
}

for song in SONGS:
	item_table[song] = KONItemData("Songs", SONGS[song]["item_id"], ItemClassification.progression)

for snack in SNACKS:
	item_table[snack] = KONItemData("Snacks", SNACKS[snack]["item_id"], ItemClassification.useful)

for prop in PROPS:
	if "item_id" in PROPS[prop]:
		if prop in PROGRESSION_PROPS:
			item_table[prop] = KONItemData("Props", PROPS[prop]["item_id"], ItemClassification.progression)
		else:
			item_table[prop] = KONItemData("Props", PROPS[prop]["item_id"], ItemClassification.filler)

for outfit in OUTFITS:
	if "item_id" in OUTFITS[outfit]:
		item_table[outfit] = KONItemData("Outfits", OUTFITS[outfit]["item_id"], ItemClassification.filler)

for playable_character in PLAYABLE_CHARACTERS:
	item_table[playable_character] = KONItemData("Characters", PLAYABLE_CHARACTERS[playable_character]["item_id"], ItemClassification.progression)