import random
import utils.odds as odds

gear = {
    'weapon': {
        'one_handed': {
            'base': [
                'sword',
                'mace',
                'axe',
                'dagger',
                'claw'
            ],
            'epic': [
                'Sword of Omens',
                'Master Sword'
            ]
        },
        'two_handed': {
            'base': [
                'sword',
                'mace',
                'axe',
                'staff'
            ],
            'epic': [
                'Excalibur',
                'Sword of a Thousand Truths',
                'Zangetsu',
                'Energy Sword'
            ]
        },
        'ranged': {
            'base': [
                'short bow',
                'long bow',
                'wand',
                'gun'
            ],
            'epic': [
                'Revolver Gunblade',
                'Arrowsong',
                'Heartseeker'
            ]
        }
    },
    'armor': {
        'chest': {
            'base': [
                'robes',
                'tunic',
                'jerkin',
                'harness',
                'vest',
                'breastplate',
                'scale mail',
                'chestpiece'
            ],
            'epic': [
                'Robe of the Archmage',
                'Breastplate of Chromatic Flight',
                'Darkmantle Tunic'
            ]
        },
        'legs': {
            'base': [
                'kilt',
                'leggings',
                'woolies',
                'pants',
                'legplates',
                'legguards'
            ],
            'epic': [
                'Leggings of Arcana',
                'Cloudkeeper Legplates',
                'Dark Heart Pants'
            ]
        },
        'hands': {
            'base': [
                'gloves',
                'mitts',
                'gauntlets'
            ],
            'epic': [
                'Gloves of Holy Might',
                'Gauntlets of Annihilation',
                "Jarnglofar, Thor's Iron Gauntlets"
            ]
        }
    }
}

affixes = {
    'pre': {
        "warrior's": [
            '+5 strength',
            '+5 health'
        ],
        "sorcerer's": [
            '+5 intellect',
            '+5 mana'
        ],
        "priest's": [
            '+5 spirit',
            '+5 mana'
        ],
        "rogue's": [
            '+5 agility',
            '+5 health'
        ]
    },
    'post': {
        "of the bear": [
            '+5 strength',
            '+10 armor'
        ],
        "of the falcon": [
            '+5 intellect',
            '+5 spirit'
        ],
        "of the owl": [
            '+10 spirit'
        ],
        "of the tiger": [
            '+5 agility',
            '+5 strength'
        ],
        "of the wolf": [
            '+10 health',
            '+5 strength'
        ]
    }
}

normal_items = [
    'bandage',
    'healing potion',
    'mana potion',
    'smoked trout',
    'linen cloth'
]

junk = [
    'small rock',
    'tree branch',
    'pile of dirt',
    'large tooth'
]

'''
Get a gear type and subtype.

This snippet is used in both our regular and epic item getter,
so we can extract that out and reuse it
'''
def get_gear_type():
    # Weapon or Armor?
    gear_type = random.choice(list(gear.keys()))
    # What subtype? (Ranged, chest, etc)
    subtype = random.choice(list(gear[gear_type].keys()))

    return [gear_type, subtype]

'''
Generate a piece of gear based on our data
'''
def get_gear_item():
    gear_type, subtype = get_gear_type()
    # Individual item in the set
    base = random.choice(list(gear[gear_type][subtype]['base']))

    prefix = random.choice(list(affixes['pre'].keys()))
    suffix = random.choice(list(affixes['post'].keys()))

    stats = affixes['pre'][prefix] + affixes['post'][suffix]

    item = {
        'name': f"{prefix} {base} {suffix}",
        'stats': stats
    }

    return item

'''
Find an epic piece of gear from our data
'''
def get_epic_item():
    gear_type, subtype = get_gear_type()
    item = random.choice(list(gear[gear_type][subtype]['epic']))

    return item

'''
Get the random other things a mob would drop
'''
def get_misc(up_to=5):
    items = junk + normal_items
    up_to = up_to if up_to < len(items) else len(items) - 1
    num = random.randint(0, up_to + 1)
    return random.sample(items, num)


'''
What has our mob dropped?

We can change these values if a mob has a higher chance of dropping a type
Most mobs have a very low chance, but rares and named mobs have a higher chance

gear_chance 1/10 drop chance
epic_chance 1/10,000 drop chance
additional_items additional misc items

For guaranteed drops, set the relevent chance 1 when calling the function
'''
def get_loot(gear_chance=10, epic_chance=10000, misc_items=5):
    # Roll for an Epic, steps from epic_chance to 1
    epic_roll = odds.basic(epic_chance)
    got_epic = False
    gear = []

    # We need a 1 to have gotten an epic
    if(epic_roll == epic_chance):
        gear = [get_epic_item()]
    # If we got an epic, we'll skip regular gear,
    # but if we didn't get an epic, let's try for a consolation prize
    else:
        gear_roll = odds.basic(gear_chance)
        if(gear_roll == gear_chance):
            gear = [get_gear_item()]

    return gear + get_misc(misc_items)



# For debugging purposes, you can uncomment these lines and run the script directly
# print(get_epic_item())
# print(get_gear_item())
# print(get_misc(20))
# print(get_loot())
# print(get_loot(gear_chance=1))