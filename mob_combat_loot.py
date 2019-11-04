import random

#normal_mobs = {"zombie":50,"witch":65,"spider":50,"skeleton":60,"creeper":40, "slime":35}
#rare_mobs={"Hogger":150, "Lich King":100, "Batman":125, "Vader":75, "Skeletor":75, "Mumra":75}
#if I want to use dictionaries instead of lists


def mobselection():

    normal_mobs = ["zombie","witch","spider","skeleton","creeper", "slime"]
    rare_mobs=["Hogger", "Lich King", "Batman", "Vader", "Skeletor", "Mumra"]
    mob_type=["Elite", "Normal"]



    mobname = random.choice(normal_mobs + rare_mobs)
    print("Fighting", mobname +"\n")

    isMobElite=random.choice(mob_type)
    if isMobElite=="Elite":

        print(mobname +" is ELITE!! Health is doubled!!\n")

        return mobname

    else:
        print (mobname +" health:", mob_health,"\n")
        return mobname


def hit(health):
    hit = random.randint(0,50) # Whether hit lands
    damage = random.randint(10,50) # Damage done

    if hit >= 45:
        print("Crit!")
        return health - (damage * 2)
    elif hit <= 10:
        print("Miss")
        return health
    else:
        print ("Hit " + str(damage))
        return health - damage


def loot_table():
    rewards = []
    junk=["small rock", "tree branch", "small wrench", "folding chair", "kendo stick", "zeetar", "big rock", "femur bone"]
    weapon=["Sword","Wand","Axe","Hammer","Great Sword","2H Axe", "Staff", "2H Hammer", "Claw", "Sabre"]
    weapon_type=[" of Strength", " of Intellect", " of Agility", " of Wisdom", " of Might", " of Dexterity", " of Death", " of Unescapable Torment"]
    epic_weapons=["Sword of Omens", "Master Sword", "Lucille", "Excalibur", "Revolver Gunblade", "Sword of a Thousand Truths","Zangetsu", "Energy Sword"]



    junk_loot=[]
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
        weapon_loot.append(random.choice(weapon) + random.choice(weapon_type))

    print("Weapon Drops: ", weapon_loot)

    epic_loot=[]
    epic_drops = random.randint(0,1) #may get 1 or less epic weapon to drop

    for i in range(epic_drops):
        epic_loot.append(random.choice(epic_weapons))

    print("Epic Drops: ", epic_loot)

    rewards += junk_loot + weapon_loot + epic_loot
    return rewards


player_health = 500
mob_health = 50
inventory=[]

mobname=mobselection()


while player_health > 0 and mob_health > 0:
    print("Hero health: " + str(player_health))
    print(mobname,"health: "+ str(mob_health))
    print(mobname,"attacks hero:")
    player_health = hit(player_health)
    if(player_health <= 0):
        print("You are dead. \\sadface")
        break
    print("Hero attacks",mobname)
    mob_health = hit(mob_health)
    if(mob_health <= 0):
        print(mobname,"is dead. \\happyface\n")
        return_dungeon=(input("Press '1' to loot "))
        while return_dungeon!="1":
                print("Invalid selection.\n")
                return_dungeon=(input("Press '1' to continue "))

        print ("\nOur hero looks around.......\n")


print("Looting",mobname,":\n")
rewards=loot_table()
print("\nNow I have this: ", rewards,"\n")

answer=(input("Do you wish to continue your adventure? Press '1' if you dare or anything else to wimp out: "))
if answer=="1":
    print("\nHooray!! The adventure continues.....")

else:
    print("\nWe are sorry to see you go........well, not really, ya wimp!!")
