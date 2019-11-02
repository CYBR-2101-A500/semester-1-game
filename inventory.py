import random

mobs = ["zombie","witch","spider","skeleton","creeper", "ender dragon", "imp", "giant fly"]
inventory = ["health potion","smoked trout", "50 gold pieces", "smoked salmon"]
loot_table = ["rotting flesh","spider fang","linen cloth","sorcerer's robes of the bear","thigh bone","one-handed sword", "1 gold piece"]

# Encounter a mob
mob = mobs[random.randint(0,len(mobs)-1)]
print("Fighting " + mob)

if mob == "zombie":
     print("I am about to put you back into the ground!")
if mob == "witch":
    print("Okay big nose! Come at me!")
if mob == "spider":
    print("I hate eight legged freaks...")
if mob == "skeleton":
    print("Is the a walking bag of bones?")
if mob == "creeper":
    print("OMG!! RUN! Run!")
if mob == "ender dragon":
    print("why is there a dragon here....")
if mob == "imp":
    print("Die puny demon!")
if mob == "giant fly":
    print("Stupid fly.")
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


