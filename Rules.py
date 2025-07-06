from worlds.AutoWorld import World
from .Data import SONGS, CHARACTERS, UNIQUE_OUTFIT_SETS

def goal_song_unlock_conditions(state, world, player):
    clear_conditions: list[bool] = []
    if world.token_requirement > 0:
        clear_conditions.append(state.has("Teatime Token", player, world.token_requirement))
    if world.tape_requirement > 0:
        clear_conditions.append(state.has("Cassette Tape", player, world.tape_requirement))

    return clear_conditions

def song_unlock_rule(state, world, player, song):
    if world.goal_song == song:
        return all(goal_song_unlock_conditions(state, world, player))
    else:
        return state.has(song, player)

def set_song_rules(song, world):

    player = world.player
    multiworld = world.multiworld

    multiworld.get_location(f"{song}: Clear", player).access_rule = lambda state: song_unlock_rule(state, world, player, song)

    if not (world.goal_song == song and not world.options.full_band_goal.value):
        multiworld.get_location(f"{song}: Clear with Yui", player).access_rule = lambda state: song_unlock_rule(state, world, player, song) and state.has("Playable Yui", player)
        multiworld.get_location(f"{song}: Clear with Mio", player).access_rule = lambda state: song_unlock_rule(state, world, player, song) and state.has("Playable Mio", player)
        multiworld.get_location(f"{song}: Clear with Ritsu", player).access_rule = lambda state: song_unlock_rule(state, world, player, song) and state.has("Playable Ritsu", player)
        multiworld.get_location(f"{song}: Clear with Mugi", player).access_rule = lambda state: song_unlock_rule(state, world, player, song) and state.has("Playable Mugi", player)
        multiworld.get_location(f"{song}: Clear with Azusa", player).access_rule = lambda state: song_unlock_rule(state, world, player, song) and state.has("Playable Azusa", player)
        multiworld.get_location(f"{song}: Full Band Clear", player).access_rule = lambda state: song_unlock_rule(state, world, player, song) and state.has("Playable Yui", player) and state.has("Playable Mio", player) and state.has("Playable Ritsu", player) and state.has("Playable Mugi", player) and state.has("Playable Azusa", player)

        if world.options.challenge_locations.value > 0:
            combo = SONGS[song]["combo"]
            multiworld.get_location(f"{song}: A Rank", player).access_rule = lambda state: song_unlock_rule(state, world, player, song)
            multiworld.get_location(f"{song}: {combo} Combo", player).access_rule = lambda state: song_unlock_rule(state, world, player, song)

            if world.options.challenge_locations.value > 1:
                multiworld.get_location(f"{song}: A Rank with Yui", player).access_rule = lambda state: song_unlock_rule(state, world, player, song) and state.has("Playable Yui", player)
                multiworld.get_location(f"{song}: A Rank with Mio", player).access_rule = lambda state: song_unlock_rule(state, world, player, song) and state.has("Playable Mio", player)
                multiworld.get_location(f"{song}: A Rank with Ritsu", player).access_rule = lambda state: song_unlock_rule(state, world, player, song) and state.has("Playable Ritsu", player)
                multiworld.get_location(f"{song}: A Rank with Mugi", player).access_rule = lambda state: song_unlock_rule(state, world, player, song) and state.has("Playable Mugi", player)
                multiworld.get_location(f"{song}: A Rank with Azusa", player).access_rule = lambda state: song_unlock_rule(state, world, player, song) and state.has("Playable Azusa", player)

                multiworld.get_location(f"{song}: {combo} Combo with Yui", player).access_rule = lambda state: song_unlock_rule(state, world, player, song) and state.has("Playable Yui", player)
                multiworld.get_location(f"{song}: {combo} Combo with Mio", player).access_rule = lambda state: song_unlock_rule(state, world, player, song) and state.has("Playable Mio", player)
                multiworld.get_location(f"{song}: {combo} Combo with Ritsu", player).access_rule = lambda state: song_unlock_rule(state, world, player, song) and state.has("Playable Ritsu", player)
                multiworld.get_location(f"{song}: {combo} Combo with Mugi", player).access_rule = lambda state: song_unlock_rule(state, world, player, song) and state.has("Playable Mugi", player)
                multiworld.get_location(f"{song}: {combo} Combo with Azusa", player).access_rule = lambda state: song_unlock_rule(state, world, player, song) and state.has("Playable Azusa", player)

        if world.options.hard_clear_locations.value > 0:
            multiworld.get_location(f"{song}: Clear on Hard", player).access_rule = lambda state: song_unlock_rule(state, world, player, song)

            if world.options.hard_clear_locations.value > 1:
                multiworld.get_location(f"{song}: Clear with Yui on Hard", player).access_rule = lambda state: song_unlock_rule(state, world, player, song) and state.has("Playable Yui", player)
                multiworld.get_location(f"{song}: Clear with Mio on Hard", player).access_rule = lambda state: song_unlock_rule(state, world, player, song) and state.has("Playable Mio", player)
                multiworld.get_location(f"{song}: Clear with Ritsu on Hard", player).access_rule = lambda state: song_unlock_rule(state, world, player, song) and state.has("Playable Ritsu", player)
                multiworld.get_location(f"{song}: Clear with Mugi on Hard", player).access_rule = lambda state: song_unlock_rule(state, world, player, song) and state.has("Playable Mugi", player)
                multiworld.get_location(f"{song}: Clear with Azusa on Hard", player).access_rule = lambda state: song_unlock_rule(state, world, player, song) and state.has("Playable Azusa", player)
                multiworld.get_location(f"{song}: Full Band Clear on Hard", player).access_rule = lambda state: song_unlock_rule(state, world, player, song) and state.has("Playable Yui", player) and state.has("Playable Mio", player) and state.has("Playable Ritsu", player) and state.has("Playable Mugi", player) and state.has("Playable Azusa", player)

        if world.options.hard_challenge_locations.value > 0:
            combo = SONGS[song]["combo"]
            multiworld.get_location(f"{song}: A Rank on Hard", player).access_rule = lambda state: song_unlock_rule(state, world, player, song)
            multiworld.get_location(f"{song}: {combo} Combo on Hard", player).access_rule = lambda state: song_unlock_rule(state, world, player, song)

            if world.options.hard_challenge_locations.value > 1:
                multiworld.get_location(f"{song}: A Rank with Yui on Hard", player).access_rule = lambda state: song_unlock_rule(state, world, player, song) and state.has("Playable Yui", player)
                multiworld.get_location(f"{song}: A Rank with Mio on Hard", player).access_rule = lambda state: song_unlock_rule(state, world, player, song) and state.has("Playable Mio", player)
                multiworld.get_location(f"{song}: A Rank with Ritsu on Hard", player).access_rule = lambda state: song_unlock_rule(state, world, player, song) and state.has("Playable Ritsu", player)
                multiworld.get_location(f"{song}: A Rank with Mugi on Hard", player).access_rule = lambda state: song_unlock_rule(state, world, player, song) and state.has("Playable Mugi", player)
                multiworld.get_location(f"{song}: A Rank with Azusa on Hard", player).access_rule = lambda state: song_unlock_rule(state, world, player, song) and state.has("Playable Azusa", player)

                multiworld.get_location(f"{song}: {combo} Combo with Yui on Hard", player).access_rule = lambda state: song_unlock_rule(state, world, player, song) and state.has("Playable Yui", player)
                multiworld.get_location(f"{song}: {combo} Combo with Mio on Hard", player).access_rule = lambda state: song_unlock_rule(state, world, player, song) and state.has("Playable Mio", player)
                multiworld.get_location(f"{song}: {combo} Combo with Ritsu on Hard", player).access_rule = lambda state: song_unlock_rule(state, world, player, song) and state.has("Playable Ritsu", player)
                multiworld.get_location(f"{song}: {combo} Combo with Mugi on Hard", player).access_rule = lambda state: song_unlock_rule(state, world, player, song) and state.has("Playable Mugi", player)
                multiworld.get_location(f"{song}: {combo} Combo with Azusa on Hard", player).access_rule = lambda state: song_unlock_rule(state, world, player, song) and state.has("Playable Azusa", player)

def set_rules(world: World) -> None:

    player = world.player
    multiworld = world.multiworld

    for song in SONGS:
        set_song_rules(song, world)

    multiworld.get_location("Event: Album Tutorial", player).access_rule = lambda state: song_unlock_rule(state, world, player, "Fuwa Fuwa Time")
    multiworld.get_location("Event: Communication Tutorial", player).access_rule = lambda state: song_unlock_rule(state, world, player, "Fuwa Fuwa Time")
    multiworld.get_location("Event: Clock Tutorial", player).access_rule = lambda state: song_unlock_rule(state, world, player, "Heart Goes Boom!!") and song_unlock_rule(state, world, player, "Girly Storm Sprint Stick")
    multiworld.get_location("Event: Sing Tutorial", player).access_rule = lambda state: song_unlock_rule(state, world, player, "Head Over Heels for Giita") and song_unlock_rule(state, world, player, "Curry, Then Rice") 
    if (world.options.event_locations.value):
        multiworld.get_location("Event: A Sense of Accomplishment!", player).access_rule = lambda state: song_unlock_rule(state, world, player, "Fuwa Fuwa Time")
        multiworld.get_location("Event: Haggling!", player).access_rule = lambda state: state.has("Lottery Ticket", player) and state.has("Purse", player)
        multiworld.get_location("Event: Puni Puni!", player).access_rule = lambda state: state.has("Yui's Guitar", player) 
        multiworld.get_location("Event: Pamper!", player).access_rule = lambda state: state.has("Key", player) and state.has("Textbook", player) 
        multiworld.get_location("Event: Ferocity!", player).access_rule = lambda state: state.has("Photo of the Villa", player) and state.has("Ritsu's Drums", player) 
        multiworld.get_location("Event: Moe Moe!", player).access_rule = lambda state: state.has("Ticket", player) and state.has("Radio Cassette Player", player) 
        multiworld.get_location("Event: Friends!", player).access_rule = lambda state: state.has("Photo of the Villa", player) and state.has("Radio Cassette Player", player) 
        multiworld.get_location("Event: Fuwa Fuwa Time!", player).access_rule = lambda state: state.has("Lyrics Card", player) 
        multiworld.get_location("Event: 6 Times!", player).access_rule = lambda state: state.has("Documents", player) 
        multiworld.get_location("Event: Gottsan desu!", player).access_rule = lambda state: state.has("Microphone", player) 
        multiworld.get_location("Event: Bearer of Power!", player).access_rule = lambda state: state.has("Amp", player) 
        multiworld.get_location("Event: Strong Luck!", player).access_rule = lambda state: state.has("Lottery Ticket", player) and state.has("Board Game", player) and song_unlock_rule(state, world, player, "I Go My Own Road") and song_unlock_rule(state, world, player, "Curry, Then Rice") and song_unlock_rule(state, world, player, "Aim for Happy 100%") and song_unlock_rule(state, world, player, "Heart Goes Boom!!") and song_unlock_rule(state, world, player, "Girly Storm Sprint Stick")
        multiworld.get_location("Event: Reservation!", player).access_rule = lambda state: state.has("Note", player) 
        multiworld.get_location("Event: Ice Cream!", player).access_rule = lambda state: state.has("Key", player) and song_unlock_rule(state, world, player, "Head Over Heels for Giita") and song_unlock_rule(state, world, player, "Let's Go") and song_unlock_rule(state, world, player, "I Go My Own Road") and song_unlock_rule(state, world, player, "Curry, Then Rice") and song_unlock_rule(state, world, player, "Aim for Happy 100%")
        multiworld.get_location("Event: Tea Time!", player).access_rule = lambda state: state.has("Tea Set", player) 
        multiworld.get_location("Event: Azunyan!", player).access_rule = lambda state: state.has("Cat Ears", player) 
        multiworld.get_location("Event: Sense of Danger!", player).access_rule = lambda state: state.has("Kitty Teacup", player) 
        multiworld.get_location("Event: Encircled Secret!", player).access_rule = lambda state: state.has("Secret Photo", player) and state.has("Picnic Sheet", player) 
        multiworld.get_location("Event: Tuning!", player).access_rule = lambda state: state.has("Tuner", player) 
        multiworld.get_location("Event: Barnacles!", player).access_rule = lambda state: state.has("Barnacles", player) and state.has("Ticket", player) 
        multiworld.get_location("Event: Resort!", player).access_rule = lambda state: state.has("Parasol", player) and state.has("Ticket", player) 
        multiworld.get_location("Event: Unique!", player).access_rule = lambda state: state.has("Snowman", player) 
        multiworld.get_location("Event: Reading One's Heart!", player).access_rule = lambda state: state.has("Microphone", player) 
        multiworld.get_location("Event: Freedom!", player).access_rule = lambda state: state.has("Ticket", player) and state.has("Shellfish", player) 
        multiworld.get_location("Event: Farewell!", player).access_rule = lambda state: state.has("Sad Novel", player) 
        multiworld.get_location("Event: Secret Training!", player).access_rule = lambda state: state.has("Mio's Bass", player) 
        multiworld.get_location("Event: Untan!", player).access_rule = lambda state: state.has("Castanets", player) 
        multiworld.get_location("Event: Smile!", player).access_rule = lambda state: state.has("Azusa's Guitar", player) 
        multiworld.get_location("Event: Acting School!", player).access_rule = lambda state: state.has("Sad Novel", player) 
        multiworld.get_location("Event: 7 Wonders!", player).access_rule = lambda state: state.has("Horror Novel", player) 
        multiworld.get_location("Event: Daze!", player).access_rule = lambda state: state.has("Mio Fan Club Poster", player) 
        multiworld.get_location("Event: Teacher Advisor!", player).access_rule = lambda state: state.has("Documents", player) 
        multiworld.get_location("Event: Teacher... Advisor!", player).access_rule = lambda state: state.has("Tea Set", player) 
        multiworld.get_location("Event: Childhood Friend!", player).access_rule = lambda state: song_unlock_rule(state, world, player, "I Go My Own Road") and song_unlock_rule(state, world, player, "Curry, Then Rice") and song_unlock_rule(state, world, player, "Aim for Happy 100%") and song_unlock_rule(state, world, player, "Heart Goes Boom!!") and song_unlock_rule(state, world, player, "Girly Storm Sprint Stick")
        multiworld.get_location("Event: Event Invitation!", player).access_rule = lambda state: state.has("Note", player) and song_unlock_rule(state, world, player, "I Go My Own Road") and song_unlock_rule(state, world, player, "Curry, Then Rice") and song_unlock_rule(state, world, player, "Aim for Happy 100%") and song_unlock_rule(state, world, player, "Heart Goes Boom!!") and song_unlock_rule(state, world, player, "Girly Storm Sprint Stick")
        multiworld.get_location("Event: The Guardian!", player).access_rule = lambda state: state.has("Textbook", player) and song_unlock_rule(state, world, player, "I Go My Own Road") and song_unlock_rule(state, world, player, "Curry, Then Rice") and song_unlock_rule(state, world, player, "Aim for Happy 100%") and song_unlock_rule(state, world, player, "Heart Goes Boom!!") and song_unlock_rule(state, world, player, "Girly Storm Sprint Stick") 
        multiworld.get_location("Event: Little Sister!", player).access_rule = lambda state: song_unlock_rule(state, world, player, "Head Over Heels for Giita") and song_unlock_rule(state, world, player, "Let's Go") and song_unlock_rule(state, world, player, "I Go My Own Road") and song_unlock_rule(state, world, player, "Curry, Then Rice") and song_unlock_rule(state, world, player, "Aim for Happy 100%") 
        multiworld.get_location("Event: Good Friends!", player).access_rule = lambda state: state.has("Key", player) and song_unlock_rule(state, world, player, "Head Over Heels for Giita") and song_unlock_rule(state, world, player, "Let's Go") and song_unlock_rule(state, world, player, "I Go My Own Road") and song_unlock_rule(state, world, player, "Curry, Then Rice") and song_unlock_rule(state, world, player, "Aim for Happy 100%")
        multiworld.get_location("Event: Taiyaki!", player).access_rule = lambda state: state.has("Taiyaki", player)
        multiworld.get_location("Event: First Experience!", player).access_rule = lambda state: state.has("Sweets", player)
        multiworld.get_location("Event: First Live!", player).access_rule = lambda state: song_unlock_rule(state, world, player, "Don't Say Lazy")

    multiworld.completion_condition[player] = lambda state: state.has("Happy End", player)