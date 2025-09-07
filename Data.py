CHARACTERS = ["Yui", "Mio", "Ritsu", "Mugi", "Azusa"]

UI_REQUIREMENTS = ["Head Over Heels for Giita", "Let's Go", "I Go My Own Road", "Curry, Then Rice", "Aim for Happy 100%"] #According to my testing these are the requirements for Ui's event to unlock, though I'm not completely certain
NODOKA_REQUIREMENTS = ["I Go My Own Road", "Curry, Then Rice", "Aim for Happy 100%", "Heart Goes Boom!!", "Girly Storm Sprint Stick"] #Similarly for Nodoka

SONGS = {"Cagayake!GIRLS": {"item_id": 101, "address": 0x90b0ab0, "bit": 0, "combo": 80}, 
        "Don't Say Lazy": {"item_id": 102, "address": 0x90b0ab0, "bit": 1, "combo": 80}, 
        "Fuwa Fuwa Time": {"item_id": 103, "address": 0x90b0ab0, "bit": 2, "combo": 80}, 
        "My Love is a Stapler": {"item_id": 104, "address": 0x90b0ab0, "bit": 3, "combo": 80}, 
        "Calligraphy Pen ~Ballpoint Pen~": {"item_id": 105, "address": 0x90b0ab0, "bit": 4, "combo": 80}, 
        "Curry, Then Rice": {"item_id": 106, "address": 0x90b0ab0, "bit": 5, "combo": 80}, 
        "Let's Go": {"item_id": 107, "address": 0x90b0ab0, "bit": 6, "combo": 100}, 
        "Happy!? Sorry!!": {"item_id": 108, "address": 0x90b0ab0, "bit": 7, "combo": 80}, 

        "Sweet Bitter Beauty Song": {"item_id": 109, "address": 0x90b0ab1, "bit": 0, "combo": 80}, 
        "Head Over Heels for Giita": {"item_id": 110, "address": 0x90b0ab1, "bit": 1, "combo": 80}, 
        "Sunday Siesta": {"item_id": 111, "address": 0x90b0ab1, "bit": 2, "combo": 80}, 
        "Heart Goes Boom!!": {"item_id": 112, "address": 0x90b0ab1, "bit": 3, "combo": 100}, 
        "Hello Little Girl": {"item_id": 113, "address": 0x90b0ab1, "bit": 4, "combo": 80}, 
        "Jajauma Way To Go": {"item_id": 114, "address": 0x90b0ab1, "bit": 5, "combo": 80},
        "I Go My Own Road": {"item_id": 115, "address": 0x90b0ab1, "bit": 6, "combo": 100}, 
        "Dear My Keys": {"item_id": 116, "address": 0x90b0ab1, "bit": 7, "combo": 80}, 

        "Humming Bird": {"item_id": 117, "address": 0x90b0ab2, "bit": 0, "combo": 80}, 
        "Girly Storm Sprint Stick": {"item_id": 118, "address": 0x90b0ab2, "bit": 1, "combo": 100}, 
        "Aim for Happy 100%": {"item_id": 119, "address": 0x90b0ab2, "bit": 2, "combo": 100},
}

HARD_SONGS = {"Cagayake!GIRLS (Hard)": {"item_id": 120, "address": 0x90b0ab4, "bit": 0}, 
        "Don't Say Lazy (Hard)": {"item_id": 121, "address": 0x90b0ab4, "bit": 1}, 
        "Fuwa Fuwa Time (Hard)": {"item_id": 122, "address": 0x90b0ab4, "bit": 2}, 
        "My Love is a Stapler (Hard)": {"item_id": 123, "address": 0x90b0ab4, "bit": 3}, 
        "Calligraphy Pen ~Ballpoint Pen~ (Hard)": {"item_id": 124, "address": 0x90b0ab4, "bit": 4}, 
        "Curry, Then Rice (Hard)": {"item_id": 125, "address": 0x90b0ab4, "bit": 5}, 
        "Let's Go (Hard)": {"item_id": 126, "address": 0x90b0ab4, "bit": 6}, 
        "Happy!? Sorry!! (Hard)": {"item_id": 127, "address": 0x90b0ab4, "bit": 7}, 

        "Sweet Bitter Beauty Song (Hard)": {"item_id": 128, "address": 0x90b0ab5, "bit": 0}, 
        "Head Over Heels for Giita (Hard)": {"item_id": 129, "address": 0x90b0ab5, "bit": 1}, 
        "Sunday Siesta (Hard)": {"item_id": 130, "address": 0x90b0ab5, "bit": 2}, 
        "Heart Goes Boom!! (Hard)": {"item_id": 131, "address": 0x90b0ab5, "bit": 3}, 
        "Hello Little Girl (Hard)": {"item_id": 131, "address": 0x90b0ab5, "bit": 4}, 
        "Jajauma Way To Go (Hard)": {"item_id": 132, "address": 0x90b0ab5, "bit": 5}, 
        "I Go My Own Road (Hard)": {"item_id": 133, "address": 0x90b0ab5, "bit": 6}, 
        "Dear My Keys (Hard)": {"item_id": 134, "address": 0x90b0ab5, "bit": 7}, 

        "Humming Bird (Hard)": {"item_id": 135, "address": 0x90b0ab6, "bit": 0}, 
        "Girly Storm Sprint Stick (Hard)": {"item_id": 136, "address": 0x90b0ab6, "bit": 1}, 
        "Aim for Happy 100% (Hard)": {"item_id": 137, "address": 0x90b0ab6, "bit": 2},
}

SONG_NAME_FROM_ID = {}
SONG_FLAGS_FROM_ADDRESS = {}
for song_name in SONGS:
    #Add to ID dict
    SONG_NAME_FROM_ID[SONGS[song_name]["item_id"]] = song_name

    #Add to address flag dict
    song_address = SONGS[song_name]["address"]
    song_bit = SONGS[song_name]["bit"]
    if not song_address in SONG_FLAGS_FROM_ADDRESS:
        SONG_FLAGS_FROM_ADDRESS[song_address] = {}
    SONG_FLAGS_FROM_ADDRESS[song_address][song_bit] = song_name

PROPS = {"Tea Set": {"item_id": 401, "address": 0x90b0b6c, "bit": 0},
    "Yui's Guitar": {"item_id": 402, "address": 0x90b0b6c, "bit": 1},
    "Azusa's Guitar": {"item_id": 403, "address": 0x90b0b6c, "bit": 2},
    "Mio's Bass": {"item_id": 404, "address": 0x90b0b6c, "bit": 3},
    "Ritsu's Drums": {"item_id": 405, "address": 0x90b0b6c, "bit": 4},
    "Mugi's Keyboard": {"item_id": 406, "address": 0x90b0b6c, "bit": 5},
    "Kitty Teacup": {"item_id": 407, "address": 0x90b0b6c, "bit": 6},
    "Shellfish": {"item_id": 408, "address": 0x90b0b6c, "bit": 7},

    "Costume Trunk": {"item_id": 409, "address": 0x90b0b6d, "bit": 0},
    "Board Game": {"item_id": 410, "address": 0x90b0b6d, "bit": 1},
    "Tuner": {"item_id": 411, "address": 0x90b0b6d, "bit": 2},
    "Cat Ears": {"item_id": 412, "address": 0x90b0b6d, "bit": 3},
    "Lyrics Card": {"item_id": 413, "address": 0x90b0b6d, "bit": 4},
    "Secret Photo": {"item_id": 414, "address": 0x90b0b6d, "bit": 5},
    "Documents": {"item_id": 415, "address": 0x90b0b6d, "bit": 6},
    "Note": {"item_id": 416, "address": 0x90b0b6d, "bit": 7},

    "Barnacles": {"item_id": 417, "address": 0x90b0b6e, "bit": 0},
    "Microphone": {"item_id": 418, "address": 0x90b0b6e, "bit": 1},
    "Sad Novel": {"item_id": 419, "address": 0x90b0b6e, "bit": 2},
    "Castanets": {"item_id": 420, "address": 0x90b0b6e, "bit": 3},
    "Horror Novel": {"item_id": 421, "address": 0x90b0b6e, "bit": 4},
    "Textbook": {"item_id": 422, "address": 0x90b0b6e, "bit": 5},
    "Purse": {"item_id": 423, "address": 0x90b0b6e, "bit": 6},
    "Chalk": {"item_id": 424, "address": 0x90b0b6e, "bit": 7},

    "School Uniform": {"item_id": 425, "address": 0x90b0b6f, "bit": 0},
    "Swimsuit": {"item_id": 426, "address": 0x90b0b6f, "bit": 1},
    "Plain Clothes": {"item_id": 427, "address": 0x90b0b6f, "bit": 2},
    "Ticket": {"item_id": 428, "address": 0x90b0b6f, "bit": 3},
    "Photo of the Villa": {"item_id": 429, "address": 0x90b0b6f, "bit": 4},
    "Picnic Sheet": {"item_id": 430, "address": 0x90b0b6f, "bit": 5},
    "Key": {"item_id": 431, "address": 0x90b0b6f, "bit": 6},
    "Duster": {"item_id": 432, "address": 0x90b0b6f, "bit": 7},

#    "Performance Scroll": {"address": 0x90b0b70, "bit": 0},
#    "Clock Scroll": {"address": 0x90b0b70, "bit": 1},
#    "Sing Scroll": {"address": 0x90b0b70, "bit": 2},
#    "Album Scroll": {"address": 0x90b0b70, "bit": 3},
#    "Communication Scroll": {"address": 0x90b0b70, "bit": 4},
    "Sawako's Guitar": {"item_id": 438, "address": 0x90b0b70, "bit": 5},
    "Lottery Ticket": {"item_id": 439, "address": 0x90b0b70, "bit": 6},
#    "Clubroom Sign": {"address": 0x90b0b70, "bit": 7},

#    "Item Scroll": {"address": 0x90b0b71, "bit": 0},
#    "Festival Memories": {"item_id": 442, "address": 0x90b0b71, "bit": 1},
#    "Sawako's Memory": {"address": 0x90b0b71, "bit": 2},
#    "Ui's Memory": {"address": 0x90b0b71, "bit": 3},
#    "Nodoka's Memory": {"address": 0x90b0b71, "bit": 4},
#    "Memory of the Live Performance": {"address": 0x90b0b71, "bit": 5},
#    "Memories of the Light Music Club": {"address": 0x90b0b71, "bit": 6},
#    "Memories of After School": {"address": 0x90b0b71, "bit": 7},

    "Secret Score": {"item_id": 493, "address": 0x90b0b72, "bit": 0},
    "Chocolate": {"address": 0x90b0b72, "bit": 1},
    "Popsicle": {"address": 0x90b0b72, "bit": 2},
    "Taiyaki": {"address": 0x90b0b72, "bit": 3},
    "Cake": {"address": 0x90b0b72, "bit": 4},
    "Cookie": {"address": 0x90b0b72, "bit": 5},
    "Tart": {"address": 0x90b0b72, "bit": 6},
    "Sweets": {"address": 0x90b0b72, "bit": 7},

    "Strawberry Milk": {"address": 0x90b0b73, "bit": 0},
    "Radio Cassette Player": {"item_id": 449, "address": 0x90b0b73, "bit": 1},
    "Rubber Boat": {"item_id": 450, "address": 0x90b0b73, "bit": 2},
    "Amp": {"item_id": 451, "address": 0x90b0b73, "bit": 3},
    "Snowman": {"item_id": 452, "address": 0x90b0b73, "bit": 4},
    "Parasol": {"item_id": 453, "address": 0x90b0b73, "bit": 5},
    "Bookcase": {"item_id": 454, "address": 0x90b0b73, "bit": 6},
    "Yui Poster": {"item_id": 455, "address": 0x90b0b73, "bit": 7},

    "Mio Poster": {"item_id": 456, "address": 0x90b0b74, "bit": 0},
    "Ritsu Poster": {"item_id": 457, "address": 0x90b0b74, "bit": 1},
    "Mugi Poster": {"item_id": 458, "address": 0x90b0b74, "bit": 2},
    "Azusa Poster": {"item_id": 459, "address": 0x90b0b74, "bit": 3},
    "HTT Poster": {"item_id": 460, "address": 0x90b0b74, "bit": 4},
    "Scary Poster": {"item_id": 461, "address": 0x90b0b74, "bit": 5},
    "Principal's Statue": {"item_id": 462, "address": 0x90b0b74, "bit": 6},
    "Rabbit Ornament": {"item_id": 463, "address": 0x90b0b74, "bit": 7},

    "Turtle Ornament": {"item_id": 464, "address": 0x90b0b75, "bit": 0},
    "Sand Castle": {"item_id": 465, "address": 0x90b0b75, "bit": 1},
    "Signboard": {"item_id": 466, "address": 0x90b0b75, "bit": 2},
    "Hen Puppet": {"item_id": 467, "address": 0x90b0b75, "bit": 3},
    "Horse Puppet": {"item_id": 468, "address": 0x90b0b75, "bit": 4},
    "Dog Puppet": {"item_id": 469, "address": 0x90b0b75, "bit": 5},
    "Cat Puppet": {"item_id": 470, "address": 0x90b0b75, "bit": 6},
    "Pig Puppet": {"item_id": 471, "address": 0x90b0b75, "bit": 7},

    "Decorative Plant": {"item_id": 472, "address": 0x90b0b76, "bit": 0},
    "Karakasa Monster": {"item_id": 473, "address": 0x90b0b76, "bit": 1},
    "Cupboard": {"item_id": 474, "address": 0x90b0b76, "bit": 2},
    "Doll": {"item_id": 475, "address": 0x90b0b76, "bit": 3},
    "Christmas Tree": {"item_id": 476, "address": 0x90b0b76, "bit": 4},
    "Member Recruitment Poster": {"item_id": 477, "address": 0x90b0b76, "bit": 5},
    "BBQ Set": {"item_id": 478, "address": 0x90b0b76, "bit": 6},
    "Yui's Instrument Case": {"item_id": 479, "address": 0x90b0b76, "bit": 7},

    "Mio's Instrument Case": {"item_id": 480, "address": 0x90b0b77, "bit": 0},
    "Mugi's Instrument Case": {"item_id": 481, "address": 0x90b0b77, "bit": 1},
    "Azusa's Instrument Case": {"item_id": 482, "address": 0x90b0b77, "bit": 2},
    "Mio Fan Club Poster": {"item_id": 483, "address": 0x90b0b77, "bit": 3},
    "Sofa": {"item_id": 484, "address": 0x90b0b77, "bit": 4},
#    "Yui's Phone Number": {"address": 0x90b0b77, "bit": 5},
#    "Mio's Phone Number": {"address": 0x90b0b77, "bit": 6},
#    "Ritsu's Phone Number": {"address": 0x90b0b77, "bit": 7},

#    "Mugi's Phone Number": {"address": 0x90b0b78, "bit": 0},
#    "Azusa's Phone Number": {"address": 0x90b0b78, "bit": 1},
#    "Sawako's Phone Number": {"address": 0x90b0b78, "bit": 2},
#    "Nodoka's Phone Number": {"address": 0x90b0b78, "bit": 3},
#    "Ui's Phone Number": {"address": 0x90b0b78, "bit": 4}
}

PROGRESSION_PROPS = ["Sweets", "Taiyaki", "Chocolate", "Mio's Bass", "Yui's Guitar", 'Textbook', 'Barnacles', 'Lottery Ticket', 'Radio Cassette Player', 'Castanets', 'Cat Ears', "Ritsu's Drums", 'Photo of the Villa', 'Snowman', 'Shellfish', "Azusa's Guitar", 'Sad Novel', 'Ticket', 'Note', 'Mio Fan Club Poster', 'Tuner', 'Tea Set', 'Documents', 'Purse', 'Parasol', 'Secret Photo', 'Board Game', 'Horror Novel', 'Microphone', 'Picnic Sheet', 'Amp', 'Lyrics Card', 'Kitty Teacup', 'Key'] #All the props that are used to trigger events

PROP_NAME_FROM_ID = {}
PROP_FLAGS_FROM_ADDRESS = {}
for prop_name in PROPS:
    #Add to ID dict
    if "item_id" in PROPS[prop_name]:
        PROP_NAME_FROM_ID[PROPS[prop_name]["item_id"]] = prop_name

    #Add to address flag dict
    prop_address = PROPS[prop_name]["address"]
    prop_bit = PROPS[prop_name]["bit"]
    if not prop_address in PROP_FLAGS_FROM_ADDRESS:
        PROP_FLAGS_FROM_ADDRESS[prop_address] = {}
    PROP_FLAGS_FROM_ADDRESS[prop_address][prop_bit] = prop_name

SNACKS = {"Chocolate": {"item_id": 601, "address": 0x90b0a99},
        "Popsicle": {"item_id": 602, "address": 0x90b0a9a},
        "Taiyaki": {"item_id": 603, "address": 0x90b0a9b},
        "Cake": {"item_id": 604, "address": 0x90b0a9c},
        "Cookie": {"item_id": 605, "address": 0x90b0a9d},
        "Tart": {"item_id": 606, "address": 0x90b0a9e},
        "Sweets": {"item_id": 607, "address": 0x90b0a9f},
        "Strawberry Milk": {"item_id": 608, "address": 0x90b0aa0},
}

SNACK_NAME_FROM_ID = {}
SNACK_NAME_FROM_ADDRESS = {}
for snack_name in SNACKS:
    #Add to ID dict
    SNACK_NAME_FROM_ID[SNACKS[snack_name]["item_id"]] = snack_name

    #Add to address dict
    if not SNACKS[snack_name]["address"] == None:
        SNACK_NAME_FROM_ADDRESS[SNACKS[snack_name]["address"]] = snack_name

PLAYABLE_CHARACTERS = {"Playable Yui": {"item_id": 201},
        "Playable Mio": {"item_id": 202},
        "Playable Ritsu": {"item_id": 203},
        "Playable Mugi": {"item_id": 204},
        "Playable Azusa": {"item_id": 205}
}

PLAYABLE_CHARACTER_NAME_FROM_ID = {}
for playable_character_name in PLAYABLE_CHARACTERS:
    #Add to ID dict
    PLAYABLE_CHARACTER_NAME_FROM_ID[PLAYABLE_CHARACTERS[playable_character_name]["item_id"]] = playable_character_name

EVENTS = {"Event: Play Tutorial": {'location_id': 4001, 'address': 0x90b0b8c, 'bit': 0, 'requirements': [], 'ingame_id': 0},
        "Event: Item Tutorial": {'location_id': 4002, 'address': 0x90b0b8c, 'bit': 1, 'requirements': [], 'ingame_id': 1},
        "Event: Communication Tutorial": {'location_id': 4003, 'address': 0x90b0b8c, 'bit': 2, 'requirements': ['Fuwa Fuwa Time'], 'ingame_id': 2},
        "Event: Dress Tutorial": {'location_id': 4004, 'address': 0x90b0b8c, 'bit': 3, 'requirements': [], 'ingame_id': 3},
        "Event: Album Tutorial": {'location_id': 4005, 'address': 0x90b0b8c, 'bit': 4, 'requirements': [], 'ingame_id': 4},
        "Event: Clock Tutorial": {'location_id': 4006, 'address': 0x90b0b8c, 'bit': 5, 'requirements': ['Heart Goes Boom', 'Girly Storm Sprint Stick'], 'ingame_id': 5},
        "Event: Sing Tutorial": {'location_id': 4007, 'address': 0x90b0b8c, 'bit': 6, 'requirements': ['Head Over Heels for Giita', 'Curry, Then Rice'], 'ingame_id': 6},
        "Event: A Sense of Accomplishment!": {'location_id': 4008, 'address': 0x90b0b8c, 'bit': 7, 'requirements': ['Fuwa Fuwa Time'], 'ingame_id': 7},

        "Event: First Live!": {'location_id': 4009, 'address': 0x90b0b8d, 'bit': 0, 'requirements': ["Don't Say Lazy"], 'ingame_id': 8},
#       "Event: I Love K-On!": {'location_id': 4010, 'address': 0x90b0b8d, 'bit': 1, 'requirements': [], 'ingame_id': 9}, 
#       "Event: Credits!": {'location_id': 4011, 'address': 0x90b0b8d, 'bit': 2, 'requirements': [], 'ingame_id': 10},
        "Event: Haggling!": {'location_id': 4012, 'address': 0x90b0b8d, 'bit': 3, 'requirements': ['Lottery Ticket', 'Purse'], 'ingame_id': 11},
        "Event: Puni Puni!": {'location_id': 4013, 'address': 0x90b0b8d, 'bit': 4, 'requirements': ["Yui's Guitar"], 'ingame_id': 12},
        "Event: Pamper!": {'location_id': 4014, 'address': 0x90b0b8d, 'bit': 5, 'requirements': ['Key', 'Textbook'], 'ingame_id': 13},
        "Event: Ferocity!": {'location_id': 4015, 'address': 0x90b0b8d, 'bit': 6, 'requirements': ['Photo of the Villa', "Ritsu's Drums"], 'ingame_id': 14},
        "Event: Moe Moe!": {'location_id': 4016, 'address': 0x90b0b8d, 'bit': 7, 'requirements': ['Ticket', 'Radio Cassette Player'], 'ingame_id': 15},

        "Event: Friends!": {'location_id': 4017, 'address': 0x90b0b8e, 'bit': 0, 'requirements': ['Photo of the Villa', 'Radio Cassette Player'], 'ingame_id': 16},
        "Event: Fuwa Fuwa Time!": {'location_id': 4018, 'address': 0x90b0b8e, 'bit': 1, 'requirements': ['Lyrics Card'], 'ingame_id': 17},
        "Event: 6 Times!": {'location_id': 4019, 'address': 0x90b0b8e, 'bit': 2, 'requirements': ['Documents'], 'ingame_id': 18},
        "Event: Gottsan desu!": {'location_id': 4020, 'address': 0x90b0b8e, 'bit': 3, 'requirements': ['Microphone'], 'ingame_id': 19},
        "Event: Bearer of Power!": {'location_id': 4021, 'address': 0x90b0b8e, 'bit': 4, 'requirements': ['Amp'], 'ingame_id': 20},
        "Event: Strong Luck!": {'location_id': 4022, 'address': 0x90b0b8e, 'bit': 5, 'requirements': ['Lottery Ticket', 'Board Game'] + NODOKA_REQUIREMENTS, 'ingame_id': 21},
        "Event: Reservation!": {'location_id': 4023, 'address': 0x90b0b8e, 'bit': 6, 'requirements': ['Note'], 'ingame_id': 22},
        "Event: Ice Cream!": {'location_id': 4024, 'address': 0x90b0b8e, 'bit': 7, 'requirements': ['Key'] + UI_REQUIREMENTS, 'ingame_id': 23},

        "Event: Tea Time!": {'location_id': 4025, 'address': 0x90b0b8f, 'bit': 0, 'requirements': ['Tea Set'], 'ingame_id': 24},
        "Event: Azunyan!": {'location_id': 4026, 'address': 0x90b0b8f, 'bit': 1, 'requirements': ['Cat Ears'], 'ingame_id': 25},
        "Event: Sense of Danger!": {'location_id': 4027, 'address': 0x90b0b8f, 'bit': 2, 'requirements': ['Kitty Teacup'], 'ingame_id': 26},
        "Event: Encircled Secret!": {'location_id': 4028, 'address': 0x90b0b8f, 'bit': 3, 'requirements': ['Secret Photo', 'Picnic Sheet'], 'ingame_id': 27},
        "Event: Tuning!": {'location_id': 4029, 'address': 0x90b0b8f, 'bit': 4, 'requirements': ['Tuner'], 'ingame_id': 28},
        "Event: Barnacles!": {'location_id': 4030, 'address': 0x90b0b8f, 'bit': 5, 'requirements': ['Barnacles', 'Ticket'], 'ingame_id': 29},
        "Event: Resort!": {'location_id': 4031, 'address': 0x90b0b8f, 'bit': 6, 'requirements': ['Parasol', 'Ticket'], 'ingame_id': 30},
        "Event: Unique!": {'location_id': 4032, 'address': 0x90b0b8f, 'bit': 7, 'requirements': ['Snowman'], 'ingame_id': 31},

        "Event: Reading One's Heart!": {'location_id': 4033, 'address': 0x90b0b90, 'bit': 0, 'requirements': ['Microphone'], 'ingame_id': 32},
        "Event: First Experience!": {'location_id': 4034, 'address': 0x90b0b90, 'bit': 1, 'requirements': [], 'ingame_id': 33},
        "Event: Freedom!": {'location_id': 4035, 'address': 0x90b0b90, 'bit': 2, 'requirements': ['Ticket', 'Shellfish'], 'ingame_id': 34},
        "Event: Farewell!": {'location_id': 4036, 'address': 0x90b0b90, 'bit': 3, 'requirements': ['Sad Novel'], 'ingame_id': 35},
        "Event: Secret Training!": {'location_id': 4037, 'address': 0x90b0b90, 'bit': 4, 'requirements': ["Mio's Bass"], 'ingame_id': 36},
        "Event: Untan!": {'location_id': 4038, 'address': 0x90b0b90, 'bit': 5, 'requirements': ['Castanets'], 'ingame_id': 37},
        "Event: Smile!": {'location_id': 4039, 'address': 0x90b0b90, 'bit': 6, 'requirements': ["Azusa's Guitar"], 'ingame_id': 38},
        "Event: Acting School!": {'location_id': 4040, 'address': 0x90b0b90, 'bit': 7, 'requirements': ['Sad Novel'], 'ingame_id': 39},

        "Event: Taiyaki!": {'location_id': 4041, 'address': 0x90b0b91, 'bit': 0, 'requirements': [], 'ingame_id': 40},
        "Event: 7 Wonders!": {'location_id': 4042, 'address': 0x90b0b91, 'bit': 1, 'requirements': ['Horror Novel'], 'ingame_id': 41},
        "Event: Daze!": {'location_id': 4043, 'address': 0x90b0b91, 'bit': 2, 'requirements': ['Mio Fan Club Poster'], 'ingame_id': 42},
        "Event: Teacher Advisor!": {'location_id': 4044, 'address': 0x90b0b91, 'bit': 3, 'requirements': ['Documents'], 'ingame_id': 43},
        "Event: Teacher... Advisor!": {'location_id': 4045, 'address': 0x90b0b91, 'bit': 4, 'requirements': ['Tea Set'], 'ingame_id': 44},
        "Event: Childhood Friend!": {'location_id': 4046, 'address': 0x90b0b91, 'bit': 5, 'requirements': NODOKA_REQUIREMENTS, 'ingame_id': 45},
        "Event: Event Invitation!": {'location_id': 4047, 'address': 0x90b0b91, 'bit': 6, 'requirements': ['Note'] + NODOKA_REQUIREMENTS, 'ingame_id': 46},
        "Event: The Guardian!": {'location_id': 4048, 'address': 0x90b0b91, 'bit': 7, 'requirements': ['Textbook'] + NODOKA_REQUIREMENTS, 'ingame_id': 47},

        "Event: Little Sister!": {'location_id': 4049, 'address': 0x90b0b92, 'bit': 0, 'requirements': UI_REQUIREMENTS, 'ingame_id': 48},
        "Event: Good Friends!": {'location_id': 4050, 'address': 0x90b0b92, 'bit': 1, 'requirements': ['Key'] + UI_REQUIREMENTS, 'ingame_id': 49}
}

EVENT_TITLES_FROM_INGAME_ID = {}
EVENT_FLAGS_FROM_ADDRESS = {}
for event_name in EVENTS:
    event_address = EVENTS[event_name]["address"]
    event_bit = EVENTS[event_name]["bit"]
    
    if not event_address in EVENT_FLAGS_FROM_ADDRESS:
        EVENT_FLAGS_FROM_ADDRESS[event_address] = {}
    EVENT_FLAGS_FROM_ADDRESS[event_address][event_bit] = event_name
    EVENT_TITLES_FROM_INGAME_ID[EVENTS[event_name]["ingame_id"]] = event_name

SONG_CLEARS = {}
HARD_SONG_CLEARS = {}
SONG_COMPLETIONIST_CLEARS = {}
HARD_SONG_COMPLETIONIST_CLEARS = {}
SONG_RANK_CLEARS = {}
HARD_SONG_RANK_CLEARS = {}
SONG_COMBO_CLEARS = {}
HARD_SONG_COMBO_CLEARS = {}
CHARACTER_CLEARS = {}
HARD_CHARACTER_CLEARS = {}
CHARACTER_RANK_CLEARS = {}
HARD_CHARACTER_RANK_CLEARS = {}
CHARACTER_COMBO_CLEARS = {}
HARD_CHARACTER_COMBO_CLEARS = {}

for song in SONGS:

    SONG_CLEARS[f"{song}: Clear"] = {"location_id": 5000 + len(SONG_CLEARS)}

    HARD_SONG_CLEARS[f"{song}: Clear on Hard"] = {"location_id": 5100 + len(HARD_SONG_CLEARS)}

    SONG_COMPLETIONIST_CLEARS[f"{song}: Full Band Clear"] = {"location_id": 5200 + len(SONG_COMPLETIONIST_CLEARS)}

    HARD_SONG_COMPLETIONIST_CLEARS[f"{song}: Full Band Clear on Hard"] = {"location_id": 5300 + len(HARD_SONG_COMPLETIONIST_CLEARS)}

    SONG_RANK_CLEARS[f"{song}: A Rank"] = {"location_id": 5400 + len(SONG_RANK_CLEARS)}

    HARD_SONG_RANK_CLEARS[f"{song}: A Rank on Hard"] = {"location_id": 5500 + len(HARD_SONG_RANK_CLEARS)}

    SONG_COMBO_CLEARS[f"{song}: {SONGS[song]['combo']} Combo"] = {"location_id": 5600 + len(SONG_COMBO_CLEARS)}

    HARD_SONG_COMBO_CLEARS[f"{song}: {SONGS[song]['combo']} Combo on Hard"] = {"location_id": 5700 + len(HARD_SONG_COMBO_CLEARS)}

    for character in CHARACTERS:
        CHARACTER_CLEARS[f"{song}: Clear with {character}"] = {"location_id": 5800 + len(CHARACTER_CLEARS)}

        HARD_CHARACTER_CLEARS[f"{song}: Clear with {character} on Hard"] = {"location_id": 5900 + len(HARD_CHARACTER_CLEARS)}

        CHARACTER_RANK_CLEARS[f"{song}: A Rank with {character}"] = {"location_id": 6000 + len(CHARACTER_RANK_CLEARS)}

        HARD_CHARACTER_RANK_CLEARS[f"{song}: A Rank with {character} on Hard"] = {"location_id": 6100 + len(HARD_CHARACTER_RANK_CLEARS)}

        CHARACTER_COMBO_CLEARS[f"{song}: {SONGS[song]['combo']} Combo with {character}"] = {"location_id": 6200 + len(CHARACTER_COMBO_CLEARS)}

        HARD_CHARACTER_COMBO_CLEARS[f"{song}: {SONGS[song]['combo']} Combo with {character} on Hard"] = {"location_id": 6300 + len(HARD_CHARACTER_COMBO_CLEARS)}

CHARACTER_CLEAR_NAME_FROM_ID = {}
for clear_name in CHARACTER_CLEARS:
    CHARACTER_CLEAR_NAME_FROM_ID[CHARACTER_CLEARS[clear_name]["location_id"]] = clear_name

HARD_CHARACTER_CLEAR_NAME_FROM_ID = {}
for clear_name in HARD_CHARACTER_CLEARS:
    HARD_CHARACTER_CLEAR_NAME_FROM_ID[HARD_CHARACTER_CLEARS[clear_name]["location_id"]] = clear_name

OUTFIT_MAPPING = {0: "Winter Uniform Outfit",
        1: "Summer Uniform Outfit",
        2: "Jersey Outfit",
        3: "Fuwa Fuwa Time Outfit",
        4: "Gothic Outfit",
        5: "Yukata Outfit",
        6: "Animal Costume Outfit",
        7: "Maid Outfit",

        8: "Waitress Outfit",
        9: "Chinese Dress Outfit",
        10: "Part-time Uniform Outfit",
        11: "Parka Outfit",
        12: "Swimsuit Outfit",
        13: "Casual Outfit",
        14: "Summer Outfit A",
        15: "Summer Outfit B",

        16: "Winter Outfit",
        17: "Coat Outfit",
        18: "Santa Outfit",
        19: "Active Outfit",
        20: "Nurse Outfit",
        21: "School Swimsuit Outfit"
}

OUTFITS = {"Yui's Winter Uniform Outfit": {"item_id": 801, "address": 0x90b0b38, "bit": 0, "ingame_id": 0},
        "Yui's Summer Uniform Outfit": {"item_id": 802, "address": 0x90b0b38, "bit": 1, "ingame_id": 1},
        "Yui's Jersey Outfit": {"item_id": 803, "address": 0x90b0b38, "bit": 2, "ingame_id": 2},
        "Yui's Fuwa Fuwa Time Outfit": {"item_id": 804, "address": 0x90b0b38, "bit": 3, "ingame_id": 3},
        "Yui's Gothic Outfit": {"item_id": 805, "address": 0x90b0b38, "bit": 4, "ingame_id": 4},
        "Yui's Yukata Outfit": {"item_id": 806, "address": 0x90b0b38, "bit": 5, "ingame_id": 5},
        "Yui's Animal Costume Outfit": {"item_id": 807, "address": 0x90b0b38, "bit": 6, "ingame_id": 6},
        "Yui's Maid Outfit": {"item_id": 808, "address": 0x90b0b38, "bit": 7, "ingame_id": 7},

        "Yui's Waitress Outfit": {"item_id": 809, "address": 0x90b0b39, "bit": 0, "ingame_id": 8},
        "Yui's Chinese Dress Outfit": {"item_id": 810, "address": 0x90b0b39, "bit": 1, "ingame_id": 9},
        "Yui's Part-time Uniform Outfit": {"item_id": 811, "address": 0x90b0b39, "bit": 2, "ingame_id": 10},
        "Yui's Parka Outfit": {"item_id": 812, "address": 0x90b0b39, "bit": 3, "ingame_id": 11},
        "Yui's Swimsuit Outfit": {"item_id": 813, "address": 0x90b0b39, "bit": 4, "ingame_id": 12},
        "Yui's Casual Outfit": {"item_id": 814, "address": 0x90b0b39, "bit": 5, "ingame_id": 13},
        "Yui's Summer Outfit A": {"item_id": 815, "address": 0x90b0b39, "bit": 6, "ingame_id": 14},
        "Yui's Summer Outfit B": {"item_id": 816, "address": 0x90b0b39, "bit": 7, "ingame_id": 15},

        "Yui's Winter Outfit": {"item_id": 817, "address": 0x90b0b3a, "bit": 0, "ingame_id": 16},
        "Yui's Coat Outfit": {"item_id": 818, "address": 0x90b0b3a, "bit": 1, "ingame_id": 17},
        "Yui's Santa Outfit": {"item_id": 819, "address": 0x90b0b3a, "bit": 2, "ingame_id": 18},
        "Yui's Active Outfit": {"item_id": 820, "address": 0x90b0b3a, "bit": 3, "ingame_id": 19},
        "Yui's Nurse Outfit": {"item_id": 821, "address": 0x90b0b3a, "bit": 4, "ingame_id": 20},
        "Yui's School Swimsuit Outfit": {"item_id": 822, "address": 0x90b0b3a, "bit": 5, "ingame_id": 21},

        "Mio's Winter Uniform Outfit": {"item_id": 823, "address": 0x90b0b3c, "bit": 0, "ingame_id": 0},
        "Mio's Summer Uniform Outfit": {"item_id": 824, "address": 0x90b0b3c, "bit": 1, "ingame_id": 1},
        "Mio's Jersey Outfit": {"item_id": 825, "address": 0x90b0b3c, "bit": 2, "ingame_id": 2},
        "Mio's Fuwa Fuwa Time Outfit": {"item_id": 826, "address": 0x90b0b3c, "bit": 3, "ingame_id":3},
        "Mio's Gothic Outfit": {"item_id": 827, "address": 0x90b0b3c, "bit": 4, "ingame_id": 4},
        "Mio's Yukata Outfit": {"item_id": 828, "address": 0x90b0b3c, "bit": 5, "ingame_id": 5},
        "Mio's Animal Costume Outfit": {"item_id": 829, "address": 0x90b0b3c, "bit": 6, "ingame_id": 6},
        "Mio's Maid Outfit": {"item_id": 830, "address": 0x90b0b3c, "bit": 7, "ingame_id": 7},    

        "Mio's Waitress Outfit": {"item_id": 831, "address": 0x90b0b3d, "bit": 0, "ingame_id": 8},
        "Mio's Chinese Dress Outfit": {"item_id": 832, "address": 0x90b0b3d, "bit": 1, "ingame_id": 9},
        "Mio's Part-time Uniform Outfit": {"item_id": 833, "address": 0x90b0b3d, "bit": 2, "ingame_id": 10},
        "Mio's Parka Outfit": {"item_id": 834, "address": 0x90b0b3d, "bit": 3, "ingame_id": 11},
        "Mio's Swimsuit Outfit": {"item_id": 835, "address": 0x90b0b3d, "bit": 4, "ingame_id": 12},
        "Mio's Casual Outfit": {"item_id": 836, "address": 0x90b0b3d, "bit": 5, "ingame_id": 13},
        "Mio's Summer Outfit A": {"item_id": 837, "address": 0x90b0b3d, "bit": 6, "ingame_id": 14},
        "Mio's Summer Outfit B": {"item_id": 838, "address": 0x90b0b3d, "bit": 7, "ingame_id": 15},

        "Mio's Winter Outfit": {"item_id": 839, "address": 0x90b0b3e, "bit": 0, "ingame_id": 16},
        "Mio's Coat Outfit": {"item_id": 840, "address": 0x90b0b3e, "bit": 1, "ingame_id": 17},
        "Mio's Santa Outfit": {"item_id": 841, "address": 0x90b0b3e, "bit": 2, "ingame_id": 18},
        "Mio's Active Outfit": {"item_id": 842, "address": 0x90b0b3e, "bit": 3, "ingame_id": 19},
        "Mio's Nurse Outfit": {"item_id": 843, "address": 0x90b0b3e, "bit": 4, "ingame_id": 20},

        "Ritsu's Winter Uniform Outfit": {"item_id": 844, "address": 0x90b0b40, "bit": 0, "ingame_id": 0},
        "Ritsu's Summer Uniform Outfit": {"item_id": 845, "address": 0x90b0b40, "bit": 1, "ingame_id": 1},
        "Ritsu's Jersey Outfit": {"item_id": 846, "address": 0x90b0b40, "bit": 2, "ingame_id": 2},
        "Ritsu's Fuwa Fuwa Time Outfit": {"item_id": 847, "address": 0x90b0b40, "bit": 3, "ingame_id": 3},
        "Ritsu's Gothic Outfit": {"item_id": 848, "address": 0x90b0b40, "bit": 4, "ingame_id": 4},
        "Ritsu's Yukata Outfit": {"item_id": 849, "address": 0x90b0b40, "bit": 5, "ingame_id": 5},
        "Ritsu's Animal Costume Outfit": {"item_id": 850, "address": 0x90b0b40, "bit": 6, "ingame_id": 6},
        "Ritsu's Maid Outfit": {"item_id": 851, "address": 0x90b0b40, "bit": 7, "ingame_id": 7},    

        "Ritsu's Waitress Outfit": {"item_id": 852, "address": 0x90b0b41, "bit": 0, "ingame_id": 8},
        "Ritsu's Chinese Dress Outfit": {"item_id": 853, "address": 0x90b0b41, "bit": 1, "ingame_id": 9},
        "Ritsu's Part-time Uniform Outfit": {"item_id": 854, "address": 0x90b0b41, "bit": 2, "ingame_id": 10},
        "Ritsu's Parka Outfit": {"item_id": 855, "address": 0x90b0b41, "bit": 3, "ingame_id": 11},
        "Ritsu's Swimsuit Outfit": {"item_id": 856, "address": 0x90b0b41, "bit": 4, "ingame_id": 12},
        "Ritsu's Casual Outfit": {"item_id": 857, "address": 0x90b0b41, "bit": 5, "ingame_id": 13},
        "Ritsu's Summer Outfit A": {"item_id": 858, "address": 0x90b0b41, "bit": 6, "ingame_id": 14},
        "Ritsu's Summer Outfit B": {"item_id": 859, "address": 0x90b0b41, "bit": 7, "ingame_id": 15},

        "Ritsu's Winter Outfit": {"item_id": 860, "address": 0x90b0b42, "bit": 0, "ingame_id": 16},
        "Ritsu's Coat Outfit": {"item_id": 861, "address": 0x90b0b42, "bit": 1, "ingame_id": 17},
        "Ritsu's Santa Outfit": {"item_id": 862, "address": 0x90b0b42, "bit": 2, "ingame_id": 18},
        "Ritsu's Active Outfit": {"item_id": 863, "address": 0x90b0b42, "bit": 3, "ingame_id": 19},
        "Ritsu's Nurse Outfit": {"item_id": 864, "address": 0x90b0b42, "bit": 4, "ingame_id": 20},

        "Mugi's Winter Uniform Outfit": {"item_id": 865, "address": 0x90b0b44, "bit": 0, "ingame_id": 0},
        "Mugi's Summer Uniform Outfit": {"item_id": 866, "address": 0x90b0b44, "bit": 1, "ingame_id": 1},
        "Mugi's Jersey Outfit": {"item_id": 867, "address": 0x90b0b44, "bit": 2, "ingame_id": 2},
        "Mugi's Fuwa Fuwa Time Outfit": {"item_id": 868, "address": 0x90b0b44, "bit": 3, "ingame_id": 3},
        "Mugi's Gothic Outfit": {"item_id": 869, "address": 0x90b0b44, "bit": 4, "ingame_id": 4},
        "Mugi's Yukata Outfit": {"item_id": 870, "address": 0x90b0b44, "bit": 5, "ingame_id": 5},
        "Mugi's Animal Costume Outfit": {"item_id": 871, "address": 0x90b0b44, "bit": 6, "ingame_id": 6},
        "Mugi's Maid Outfit": {"item_id": 872, "address": 0x90b0b44, "bit": 7, "ingame_id": 7},    

        "Mugi's Waitress Outfit": {"item_id": 873, "address": 0x90b0b45, "bit": 0, "ingame_id": 8},
        "Mugi's Chinese Dress Outfit": {"item_id": 874, "address": 0x90b0b45, "bit": 1, "ingame_id": 9},
        "Mugi's Part-time Uniform Outfit": {"item_id": 875, "address": 0x90b0b45, "bit": 2, "ingame_id": 10},
        "Mugi's Parka Outfit": {"item_id": 876, "address": 0x90b0b45, "bit": 3, "ingame_id": 11},
        "Mugi's Swimsuit Outfit": {"item_id": 877, "address": 0x90b0b45, "bit": 4, "ingame_id": 12},
        "Mugi's Casual Outfit": {"item_id": 878, "address": 0x90b0b45, "bit": 5, "ingame_id": 13},
        "Mugi's Summer Outfit A": {"item_id": 879, "address": 0x90b0b45, "bit": 6, "ingame_id": 14},
        "Mugi's Summer Outfit B": {"item_id": 880, "address": 0x90b0b45, "bit": 7, "ingame_id": 15},

        "Mugi's Winter Outfit": {"item_id": 881, "address": 0x90b0b46, "bit": 0, "ingame_id": 16},
        "Mugi's Coat Outfit": {"item_id": 882, "address": 0x90b0b46, "bit": 1, "ingame_id": 17},
        "Mugi's Santa Outfit": {"item_id": 883, "address": 0x90b0b46, "bit": 2, "ingame_id": 18},
        "Mugi's Active Outfit": {"item_id": 884, "address": 0x90b0b46, "bit": 3, "ingame_id": 19},
        "Mugi's Nurse Outfit": {"item_id": 885, "address": 0x90b0b46, "bit": 4, "ingame_id": 20},

        "Azusa's Winter Uniform Outfit": {"item_id": 886, "address": 0x90b0b48, "bit": 0, "ingame_id": 0},
        "Azusa's Summer Uniform Outfit": {"item_id": 887, "address": 0x90b0b48, "bit": 1, "ingame_id": 1},
        "Azusa's Jersey Outfit": {"item_id": 888, "address": 0x90b0b48, "bit": 2, "ingame_id": 2},
        "Azusa's Fuwa Fuwa Time Outfit": {"item_id": 889, "address": 0x90b0b48, "bit": 3, "ingame_id": 3},
        "Azusa's Gothic Outfit": {"item_id": 890, "address": 0x90b0b48, "bit": 4, "ingame_id": 4},
        "Azusa's Yukata Outfit": {"item_id": 891, "address": 0x90b0b48, "bit": 5, "ingame_id": 5},
        "Azusa's Animal Costume Outfit": {"item_id": 892, "address": 0x90b0b48, "bit": 6, "ingame_id": 6},
        "Azusa's Maid Outfit": {"item_id": 893, "address": 0x90b0b48, "bit": 7, "ingame_id": 7},    

        "Azusa's Waitress Outfit": {"item_id": 894, "address": 0x90b0b49, "bit": 0, "ingame_id": 8},
        "Azusa's Chinese Dress Outfit": {"item_id": 895, "address": 0x90b0b49, "bit": 1, "ingame_id": 9},
        "Azusa's Part-time Uniform Outfit": {"item_id": 896, "address": 0x90b0b49, "bit": 2, "ingame_id": 10},
        "Azusa's Parka Outfit": {"item_id": 897, "address": 0x90b0b49, "bit": 3, "ingame_id": 11},
        "Azusa's Swimsuit Outfit": {"item_id": 898, "address": 0x90b0b49, "bit": 4, "ingame_id": 12},
        "Azusa's Casual Outfit": {"item_id": 899, "address": 0x90b0b49, "bit": 5, "ingame_id": 13},
        "Azusa's Summer Outfit A": {"item_id": 900, "address": 0x90b0b49, "bit": 6, "ingame_id": 14},
        "Azusa's Summer Outfit B": {"item_id": 901, "address": 0x90b0b49, "bit": 7, "ingame_id": 15},

        "Azusa's Old Uniform Outfit": {"item_id": 902, "address": 0x90b0b4a, "bit": 0, "ingame_id": 16},
        "Azusa's Coat Outfit": {"item_id": 903, "address": 0x90b0b4a, "bit": 1, "ingame_id": 17},
        "Azusa's Santa Outfit": {"item_id": 904, "address": 0x90b0b4a, "bit": 2, "ingame_id": 18},
        "Azusa's Active Outfit": {"item_id": 905, "address": 0x90b0b4a, "bit": 3, "ingame_id": 19},
        "Azusa's Nurse Outfit": {"item_id": 906, "address": 0x90b0b4a, "bit": 4, "ingame_id": 20}
}

UNIQUE_OUTFIT_SETS = [
    "Winter Uniform Outfit",
    "Summer Uniform Outfit",
    "Jersey Outfit",
    "Fuwa Fuwa Time Outfit",
    "Gothic Outfit",
    "Yukata Outfit",
    "Animal Costume Outfit",
    "Maid Outfit",
    "Waitress Outfit",
    "Chinese Dress Outfit",
    "Part-time Uniform Outfit",
    "Parka Outfit",
    "Swimsuit Outfit",
    "Casual Outfit",
    "Summer Outfit A",
    "Summer Outfit B",
    "Coat Outfit",
    "Santa Outfit",
    "Active Outfit",
    "Nurse Outfit",
]

OUTFIT_NAME_FROM_ID = {}
OUTFIT_FLAGS_FROM_ADDRESS = {}
for outfit_name in OUTFITS:
    #Add to ID dict
    if "item_id" in OUTFITS[outfit_name]:
        OUTFIT_NAME_FROM_ID[OUTFITS[outfit_name]["item_id"]] = outfit_name

    #Add to address flag dict
    outfit_address = OUTFITS[outfit_name]["address"]
    outfit_bit = OUTFITS[outfit_name]["bit"]
    if not outfit_address in OUTFIT_FLAGS_FROM_ADDRESS:
        OUTFIT_FLAGS_FROM_ADDRESS[outfit_address] = {}
    OUTFIT_FLAGS_FROM_ADDRESS[outfit_address][outfit_bit] = outfit_name