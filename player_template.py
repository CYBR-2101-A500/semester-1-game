'''
The player template. This will be our starting point for a new player.

NOTE: This file does not get updated with the dynamic data of a player
in action. This is only the model for a brand new character.

TODO: We can expand on player stats to include the modifiers from items,
so that our player actually benefits from the loot they find. If we do that,
we'll also need to figure out how to apply those modifiers in a way we know
it's from items (such as a "base + modifiers" calculation).
'''

player_template = {
    'name': '',
    'stats': {
        'hp': 200,
        'maxhp': 200,
        'minhit': 10,
        'maxhit': 50
    },
    'inventory': {
        'gold': 0,
        'items': []
    }
}