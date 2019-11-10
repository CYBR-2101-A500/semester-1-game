'''
This will be the entrypoint of our game.
Everything else can get pulled in to here as needed.

NOTE: There should NOT be much in the way of logic
in this file. If you're writing any kind of logic or
calculation, that's your cue to put it into a module.
'''

import player_template

# Create a new player
player = player_template.player_template
player['name'] = input('Hello. What is your name? ')

print(f"Welcome, {player['name']}")

#