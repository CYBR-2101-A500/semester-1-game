import utils.odds as odds
import random

mobs = {
    'normal': {
        'zombie': {
            'hp': 20,
            'minhit': 1,
            'maxhit': 5
        },
        'witch': {
            'hp': 60,
            'minhit': 1,
            'maxhit': 15
        },
        'spider': {
            'hp': 30,
            'minhit': 1,
            'maxhit': 10
        },
        'skeleton': {
            'hp': 15,
            'minhit': 1,
            'maxhit': 5
        },
        'creeper': {
            'hp': 30,
            'minhit': 1,
            'maxhit': 15
        },
        'slime': {
            'hp': 40,
            'minhit': 1,
            'maxhit': 10
        }
    },
    'rare': {
        'Hogger': {
            'hp': 100,
            'minhit': 10,
            'maxhit': 40
        },
        'Lich King': {
            'hp': 200,
            'minhit': 10,
            'maxhit': 40
        },
        'Batman': {
            'hp': 150,
            'minhit': 10,
            'maxhit': 40
        },
        'Vader': {
            'hp': 200,
            'minhit': 10,
            'maxhit': 40
        },
        'Skeletor': {
            'hp': 200,
            'minhit': 10,
            'maxhit': 40
        },
        'Mumra': {
            'hp': 200,
            'minhit': 10,
            'maxhit': 40
        },
    }
}

'''
Get a mob

Odds calculation works like the loot one

rare_chance 1/1000 will be a named rare
elite_chance 1/50 will be an elite version of the basic
'''
def get_mob(rare_chance=1000, elite_chance=50):
    rare_roll = odds.basic(rare_chance)
    mob = {
        'name': None,
        'stats': None
    }

    if(rare_roll == rare_chance):
        # We got a rare
        mob['name'] = random.choice(list(mobs['rare'].keys()))
        mob['stats'] = mobs['rare'][mob['name']]
    else:
        mob['name'] = random.choice(list(mobs['normal'].keys()))
        mob['stats'] = mobs['normal'][mob['name']]
        elite_roll = odds.basic(elite_chance)
        # Elites have doulbe the health and do more damage
        if(elite_roll == elite_chance):
            mob['stats']['hp'] *= 2
            mob['stats']['minhit'] *= 1.25
            mob['stats']['maxhit'] *= 1.25

    return mob


# For debugging purposes, you can uncomment these lines and run the script directly
# print(get_mob())