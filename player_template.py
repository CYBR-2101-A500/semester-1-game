'''
The player template. This will be our starting point for a new player.

NOTE: This file does not get updated with the dynamic data of a player
in action. This is only the model for a brand new character.

TODO: We can expand on player stats to include the modifiers from items,
so that our player actually benefits from the loot they find. If we do that,
we'll also need to figure out how to apply those modifiers in a way we know
it's from items (such as a "base + modifiers" calculation).
'''

import time



Name = input("Enter a name: ")
time.sleep(1)
print ("Welcome to the Shadowlands brave warrior")
time.sleep(2)
print("You are given nothing but 1000 gold to start you journey...")
time.sleep(2)
print("Good luck...")
time.sleep(3)
print("Shopkeeper: 'Eh there stranger! Looks like you'll need some gear before going into the wild! Check out my store!'")
time.sleep(4)
print("")


IsShopLocked = False
IsDaggerEquipped = False
IsSwordEquipped = False
IsPlateMailEquipped = False



game_state = dict()

class Human(object):

    def __init__(self, name, health, strength, gold):
        self.name = name
        self.health = health
        self.strength = strength
        self.gold = gold

class Item(object):

    def __init__(self, name, hvalue, strvalue):
        self.name = name
        self.hvalue = hvalue
        self.strvalue = strvalue


def initialize_game():
    global game_state
    player = Human('Josh', 100, 10, 1000)

    state = dict()
    state['players'] = [player]
    return state

def Shop():
    global game_state
    player = game_state['players'][0]
    dagger = Item('Dagger', 0, 5)
    sword = Item('Sword', 0, 10)
    plate_mail = Item('Plate_Mail', 15, 0)
    if IsShopLocked == True:
        print("The shop is locked!")
    else:
        print()
        print("Welcome to the Shadowland's shop! What would you like to buy?\n1. Weapons\n2. Armor\n3. Go back")
        selection = int(input("Enter a value: "))

    if selection == 1:
        if player.gold >= 50:
            print("Weapons shop")
            print("1. Bronze Dagger: 50 gold\n. Bronze Sword: 150 gold")
            wpnselection = int(input("Enter a value: "))

        if wpnselection == 1:
            global IsDaggerEquipped
            global IsSwordEquipped
            if IsDaggerEquipped == True or IsSwordEquipped == True:
                print("You already have this or another weapon equipped...")
                Game_Loop()
            else:
                dagger = Item('Dagger', 0, 5)
                IsDaggerEquipped = True
                player.strength += dagger.strvalue
                player.gold -= 50
                print("strength increased to: {}".format(player.strength))
                Game_Loop()
        elif wpnselection == 2:
            if IsDaggerEquipped == True or IsSwordEquipped == True:
                print("You already have this or another weapon equipped...")
                Game_Loop()
            else:
                sword = Item('Sword', 0, 10)
                IsSwordEquipped = True
                player.strength += sword.strvalue
                player.gold -= 200
                print("strength increased to: {}".format(player.strength))
                Game_Loop()

        elif wpnselection == 3:
            Game_Loop()
    elif selection == 2:
        if player.gold >= 150:
            print("Armor shop")
            print("1. Plate mail\n2. Go back")
            armselection = int(input("Enter a value: "))

        if armselection == 1:
            global IsPlatemailEquipped
            if IsPlatemailEquipped == True:
                print("You are already wearing armor!")
                Game_Loop()
            else:
                plate_mail = Item('Plate mail', 15, 0)
                IsPlatemailEquipped = True
                player.health += plate_mail.hvalue
                player.gold -= 150
                print("Health increased to: {}".format(player.health))
                Game_Loop()

        elif armselection == 2:
            Game_Loop()

    elif selection == 3:
        Game_Loop()


def Game_Loop():
    global game_state

    while True:
        print()
        print("You are currently in the Shadowland's shop!")
        print("What would you like to do?")
        print("1. Shop\n2. View player statistics")
        print()

        try:
            selection = int(input("Enter a Value: "))
        except ValueError:
            print()
            print("You are only allowed to use the numbers 1 and 2.")
            if selection == 1:
                Shop()
            elif selection == 2:
                player = game_state['players'][0]
                print()
                print("Your players stats:\nHealth: {}\nStrength: {}\nGold: {}".format(player.health, player.strength,
                                                                                      player.gold))
            if IsDaggerEquipped == True:
                print("You have a dagger equipped")
            elif IsSwordEquipped == True:
                print("You have a sword equipped")
            elif IsPlateMailEquipped == True:
                print("You are wearing a breast plate")

            else:
                print()
                print("Oh no! That is not a valid input!")
                print()

def main():

    global game_state

    game_state = initialize_game()
    Game_Loop()

if __name__ == '__main__':
    main()
