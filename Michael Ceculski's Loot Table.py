import random

mobs = ["goo manifestation", "bat", "bear", "tiger", "eagle"]
inventory = ["apple", "energy elixir", "wood", "olive oil"]
loot_table = ["poisonous waste", "bat wing", "animal skin", "meat", "feather"]

# Encounter a mob
mob = mobs[random.randint(0,len(mobs)-1)]
print("Fighting " + mob)

# Kill the mob
print("Killed " + mob)

# Loot the mob
if mob == "goo manifestation":
    print("Loot goo manifestation")
    print("Drop: poisonous waste")
    print("Inventory: apple, energy elixir, wood, olive oil, poisonous waste")
elif mob == "bat":
    print("Loot bat")
    print("Drop: bat wing")
    print("Inventory: apple, energy elixir, wood, olive oil, bat wing")
elif mob == "bear":
    print("Loot bear")
    print("Drops: animal skin, meat")
    print("Inventory: apple, energy elixir, wood, olive oil, animal skin, meat")
elif mob == "tiger":
    print("Loot tiger")
    print("Drops: animal skin, meat")
    print("Inventory: apple, energy elixir, wood, olive oil, animal skin, meat")
else:
    print("Loot eagle")
    print("Drop: feather")
    print("Inventory: apple, energy elixir, wood, olive oil, feather")