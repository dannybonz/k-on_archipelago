from dataclasses import dataclass
from Options import Choice, Range, Toggle, PerGameCommonOptions, DeathLink

class TapeRequirement(Range):
    """
    Cassette Tape items are obtained by clearing unique songs. 
    The specified amount must be collected before your goal song can unlock. 
    A goal of 18 requires you to play every song in the game.
    """
    display_name = "Cassette Tape Goal"
    range_start = 0
    range_end = 18
    default = 18

class TeatimeTokens(Range):
    """
    How many (if any) Teatime Tokens to include in the item pool.
    These must be collected before your goal song can unlock. 
    This may be in addition to, or instead of, Cassette Tapes.
    """
    display_name = "Teatime Tokens"
    range_start = 0
    range_end = 100
    default = 0

class TokenPercentage(Range):
    """
    If Teatime Tokens are enabled, what percentage of them must be collected before your goal song can unlock.
    """
    display_name = "Token Percentage"
    range_start = 1
    range_end = 100
    default = 100

class CharacterRequirement(Toggle):
    """
    If this option is enabled then you must clear your goal song with every character in order to complete your seed.
    """
    display_name = "Full Band Goal"

class OutfitRequirement(Toggle):
    """
    If this option is enabled then all band members must be wearing a matching outfit before your goal song can unlock.
    Only the main outfit is relevant; hairstyles and accessories are not considered.
    Please be aware that after equipping the correct outfits, you may need to leave the song screen and then re-enter it in order for the goal song to correctly appear.
    """
    display_name = "Outfits Goal"

class ChallengeLocations(Choice):
    """
    Include locations for clearing songs with A ranks and high combos.
    """
    display_name = "Challenge Locations"
    option_none = 0
    option_once_per_song = 1
    option_character_and_song = 2
    default = 2

class HardClearLocations(Choice):
    """
    Include locations for clearing songs on Hard difficulty mode.
    """
    display_name = "Hard Clear Locations"
    option_none = 0
    option_once_per_song = 1
    option_character_and_song = 2
    default = 0

class HardChallengeLocations(Choice):
    """
    Include locations for clearing songs with A ranks and high combos on Hard difficulty mode.
    """
    display_name = "Hard Challenge Locations"
    option_none = 0
    option_once_per_song = 1
    option_character_and_song = 2
    default = 0

class EventLocations(Toggle):
    """
    Include additional locations for triggering story events. 
    Please be aware that forced tutorial events will always be locations, regardless of this setting.
    """
    display_name = "Event Locations"

class StartingSongsAmount(Range):
    """
    How many songs to begin the game with.
    """
    display_name = "Starting Songs Amount"
    range_start = 0
    range_end = 18
    default = 3

class StartingCharactersAmount(Range):
    """
    How many playable characters to begin the game with.
    """
    display_name = "Starting Characters Amount"
    range_start = 1
    range_end = 5
    default = 1

class SnackUpgrades(Range):
    """
    How many Snack Upgrade items to include in the item pool. 
    When collected, these permanently extend the duration of in-game Snack effects.
    These make the game progressively easier as more are collected.
    """
    display_name = "Snack Upgrades"
    range_start = 0
    range_end = 20
    default = 0

@dataclass
class KONOptions(PerGameCommonOptions):
    tape_requirement: TapeRequirement
    teatime_tokens: TeatimeTokens
    token_percentage: TokenPercentage
    full_band_goal: CharacterRequirement
    matching_outfits_goal: OutfitRequirement
    challenge_locations: ChallengeLocations
    hard_clear_locations: HardClearLocations
    hard_challenge_locations: HardChallengeLocations
    event_locations: EventLocations
    starting_songs_amount: StartingSongsAmount
    starting_characters_amount: StartingCharactersAmount
    snack_upgrades: SnackUpgrades
    death_link: DeathLink