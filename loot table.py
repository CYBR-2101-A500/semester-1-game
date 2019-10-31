import random

normal_mobs = ["zombie","witch","spider","skeleton","creeper", "slime"]
rare_mobs=["Hogger", "Lich King", "Batman", "Vader", "Skeletor", "Mumra"]
inventory = ["some old stuff"]

junk=["small rock", "tree branch", "small wrench", "folding chair", "kendo stick", "zeetar", "big rock", "femur bone"]
weapon=["Sword","Wand","Axe","Hammer","Great Sword","2H Axe", "Staff", "2H Hammer", "Claw", "Sabre"]
weapon_type=[" of Strength", " of Intellect", " of Agility", " of Wisdom", " of Might", " of Dexterity", " of Death", " of Unescapable Torment"]
epic_weapons=["Sword of Omens", "Master Sword", "Lucille", "Excalibur", "Revolver Gunblade", "Sword of a Thousand Truths","Zangetsu", "Energy Sword"]

# Encounter a mob
mob = random.choice(normal_mobs + rare_mobs)
print("Fighting " + mob+"\n")

# Kill the mob
print("Killed " + mob+"\n")

# Loot the mob
print("Looting " + mob +":\n")

junk_drops = random.randint(3,4) #may get 3 or 4 pieces of junk
for i in range(junk_drops):
    junk_loot.append(random.choice(junk)) #makes random choice from junk

print("Junk Drops: ", junk_loot)

weapon_loot = []
weapon_drops = random.randint(1,2)
for i in range(weapon_drops):
    #x= weapon[random.randint(0,len(weapon)-1)]
    #y=weapon_type[random.randint(0,len(weapon)-1)]
    #xy_weapon=x+y
    #weapon_loot.append(xy_weapon)
    weapon_loot.append(random.choice(weapon) + random.choice(weapon_type))


print("Weapon Drops: ", weapon_loot)

epic_loot=[]
epic_drops = random.randint(0,1)  #may get 1 or less epic weapon to drop

for i in range(epic_drops):
    #epic_loot.append(epic_weapons[random.randint(0,len(junk)-1)])
    epic_loot.append(random.choice(epic_weapons))

print("Epic Drops: ", epic_loot)

inventory += junk_loot + weapon_loot + epic_loot

print("Inventory: ", inventory)
