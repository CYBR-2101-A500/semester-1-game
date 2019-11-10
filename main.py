'''
This will be the entrypoint of our game.
Everything else can get pulled in to here as needed.

NOTE: There should NOT be much in the way of logic
in this file. If you're writing any kind of logic or
calculation, that's your cue to put it into a module.

TODO: How can we implement saving the user's character?
Can we add a second user? How would we do that?
'''

import player_template

# Create a new player
player = player_template.player_template
player['name'] = input('Hello. What is your name? ')

print(f"Welcome, {player['name']}")

# Generate the map and place the player in it


# Start gameplay by allowing the player to move


# Engage a mob when the player reaches one


# Repeat until the player dies, or reaches some success goal


# After an end trigger.
# TODO: How do we get this to _actually_ continue the adventure?
# What does "continuing the adventure" actually mean, programmatically?
# Do we generate a new map and give them a new "level"?
answer=(input("Do you wish to continue your adventure? Press '1' if you dare or anything else to wimp out: "))
if answer=="1":
    print("\nHooray!! The adventure continues.....")

else:
    print("\nWe are sorry to see you go........well, not really, ya wimp!!")