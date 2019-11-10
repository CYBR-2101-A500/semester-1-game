'''
This will be the entrypoint of our game. Everything else can get pulled in to here as needed.
'''

import player_template

# Create a new player
player = player_template.player_template
player['name'] = input('Hello. What is your name? ')

print(f"Welcome, {player['name']}")