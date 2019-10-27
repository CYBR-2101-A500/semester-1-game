import random

mobs = ["goo manifestation", "bat", "bear", "tiger", "eagle"]
inventory = ["apple", "energy elixir", "wood", "olive oil"]
loot_table = ["poisonous waste", "bat wing", "animal skin", "meat", "feather"]

# Encounter a mob
mob = mobs[random.randint(0,len(mobs)-1)]
print("Fighting " + mob)

#Combat phrase
if mob == "goo manifestation":
    print("So slimy... And slow.")
elif mob == "bat":
    print("Eeek! So scary! I'll smash 'em!")
elif mob == "bear":
    print("You being so big is unfair! But that won't stop me!")
elif mob == "tiger":
    print("You're too fast! But I'm still smarter!")
else:
    print("No way! I have to take the shot quickly!")

# Kill the mob
print("Killed " + mob)

# Loot the mob
if mob == "goo manifestation":
    print("Loot goo manifestation")
    print("Drop: poisonous waste")
    print("Inventory: ", inventory + "poisonous waste")
elif mob == "bat":
    print("Loot bat")
    print("Drop: bat wing")
    print("Inventory: ", inventory + "bat wing")
elif mob == "bear":
    print("Loot bear")
    print("Drops: animal skin, meat")
    print("Inventory: ", inventory + "animal skin, meat")
elif mob == "tiger":
    print("Loot tiger")
    print("Drops: animal skin, meat")
    print("Inventory: ", inventory + "animal skin, meat")
else:
    print("Loot eagle")
    print("Drop: feather")
    print("Inventory: ", inventory + "feather")