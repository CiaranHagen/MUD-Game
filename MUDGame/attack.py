
def hit(attacker, defender):
    ranDamage = random(11)
    Damage = ranDamage * attacker.weaponLevel - defender.armorLevel
    defender.health -= Damage
    print(attacker.name + " hit " + defender.name + " for " + str(Damage) + " damage. \n")

def fight(char, npc):
    
    while (char.health >= 0) and (npc.health >= 0):
        hit(npc, char)
        if defender.health <= 0:
            print("You have died.")
            defender.location = (0,0)
            defender.health = 100
    
