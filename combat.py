import random

def hit(health):
    hit = random.randint(0,50) # Whether hit lands
    damage = random.randint(10,50) # Damage done

    if hit >= 45:
        print("Crit!" + " " + str(damage * 2))
        return health - (damage * 2)
    elif hit <= 10:
        print("Miss")
        return health
    else:
        print ("Hit " + str(damage))
        return health - damage

player_health = 500
mob_health = 100

while player_health > 0 and mob_health > 0:
    print("Player: " + str(player_health))
    print("Mob: " + str(mob_health))
    print("Mob hit")
    player_health = hit(player_health)
    if(player_health <= 0):
        break
    print("Player hit")
    mob_health = hit(mob_health)
