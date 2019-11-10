import random

'''
Deal a hit to the creature

health - current HP of creature being hit
min_dmg - minimum damage done by opposing creature
max_dmg - maximum damage done by opposing creature
'''
def hit(health, min_dmg, max_dmg):
    hit = random.randint(0,50) # Whether hit lands
    damage = random.randint(min_dmg,max_dmg) # Damage done

    if hit >= 45:
        print("Crit!" + " " + str(damage * 2))
        return health - (damage * 2)
    elif hit <= 10:
        print("Miss")
        return health
    else:
        print ("Hit " + str(damage))
        return health - damage

'''
Initiate the combat sequence

player - a dictionary representing the player, must include:
    stats.hp - player's current hit points
    stats.minhit - player's minimum hit capability
    stats.maxhit - player's maximum hit capability
'''
def enter_combat(player, mob):
    # Go through combat until something dies
    while player['stats']['hp'] > 0 and mob['stats']['hp'] > 0:
        print("Player: " + str(player['stats']['hp']))
        print("Mob: " + str(mob['stats']['hp']))
        print("Mob hit")
        player['stats']['hp'] = hit(player['stats']['hp'], mob['stats']['minhit'], mob['stats']['maxhit'])
        if(player['stats']['hp'] <= 0):
            break
        print("Player hit")
        mob['stats']['hp'] = hit(mob['stats']['hp'], player['stats']['minhit'], player['stats']['maxhit'])

    # Combat has ended, return combatants' current state
    return [player, mob]


# For debugging purposes, you can uncomment these lines and run the script directly
# player = {
#     'stats': {
#         'hp': 200,
#         'maxhp': 200,
#         'minhit': 10,
#         'maxhit': 50
#     }
# }

# mob = {
#     'stats': {
#         'hp': 200,
#         'minhit': 10,
#         'maxhit': 20
#     }
# }
# print(enter_combat(player, mob))