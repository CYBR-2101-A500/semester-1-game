import random

mobs = ["zombie","witch","spider","skeleton","creeper", "ender dragon"]
inventory = ["health potion","smoked trout", "50 gold pieces"]
loot_table = ["rotting flesh","spider fang","linen cloth","sorcerer's robes of the bear","thigh bone","one-handed sword", "1 gold piece"]

# Encounter a mob
mob = mobs[random.randint(0,len(mobs)-1)]
print("Fighting " + mob)

for items in mobs:
    if item == "zombie":
        print("I am about to put you back into the ground!")
    if item == "witch":
        print("Okay big nose! Come at me!")
    if item == "spider":
        print("I hate eight legged freaks...")
    if item == "skeleton":
        print("Is the a walking bag of bones?")
    if item == "creeper":
        print("OMG!! RUN! Run!")
    if item == "ender dragon":
        print("why is there a dragon here....")

# Kill the mob
print("Killed " + mob)

# Loot the mob
print("Loot " + mob)
drops = random.randint(2,4)
loot = []
for i in range(drops):
    loot.append(loot_table[random.randint(0,len(loot_table)-1)])

print("Drops: ", loot)

inventory += loot
print("Inventory: ", inventory)

