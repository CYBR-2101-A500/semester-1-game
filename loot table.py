import random

mobs = ["zombie","witch","spider","skeleton","creeper"]
inventory = ["some old stuff"]

junk=["small rock", "tree branch", "small wrench", "folding chair", "kendo stick", "zeetar", "big rock", "femur bone"]
weapon=["Sword","Wand","Axe","Hammer","Great Sword","2H Axe", "Staff", "2H Hammer"]
weapon_type=[" of Strength", " of Intellect", " of Agility", " of Wisdom", " of Might", " of Dexterity", " of Death", " of Unescapable Torment"]
epic_weapons=["Sword of Omens", "Master Sword", "Lucille", "Excalibur", "Revolver Gunblade", "Sword of a Thousand Truths","Zangetsu", "Energy Sword"]

# Encounter a mob
mob = mobs[random.randint(0,len(mobs)-1)]
print("Fighting " + mob)

# Kill the mob
print("Killed " + mob)

# Loot the mob
print("Loot " + mob)

junk_loot=[]
junk_drops = random.randint(3,4)

for i in range(junk_drops):
    junk_loot.append(junk[random.randint(0,len(junk)-1)])

print("Junk Drops: ", junk_loot)

weapon_loot = []
weapon_drops = random.randint(1,2)
for i in range(weapon_drops):
    x= weapon[random.randint(0,len(weapon)-1)]
    y=weapon_type[random.randint(0,len(weapon)-1)]
    xy_weapon=x+y
    weapon_loot.append(xy_weapon)


print("Weapon Drops: ", weapon_loot)

epic_loot=[]
epic_drops = random.randint(0,1)

for i in range(epic_drops):
    epic_loot.append(epic_weapons[random.randint(0,len(junk)-1)])

print("Epic Drops: ", epic_loot)

inventory += junk_loot + weapon_loot + epic_loot

print("Inventory: ", inventory)
