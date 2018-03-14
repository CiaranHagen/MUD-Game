import subprocess
def hit(attacker, defender):
    ranDamage = random(11)
    Damage = ranDamage * attacker.weaponLevel - defender.armorLevel
    defender.health -= Damage
    print(attacker.name + " hit " + defender.name + " for " + str(Damage) + " damage. \n")

def fight(char, npc):
    
    while (char.health >= 0) and (npc.health >= 0):
        hit(char, npc)
        if npc.health <= 0:
            print("You are victorious!")
            subprocess.popen("rm ../data/npcs/mob_" + npc.name + ".txt").communicate()
            del npc
            break

        hit(npc, char)
        if char.health <= 0:
            print("You have died.")
            defender.location = (0,0)
            defender.health = 100
            break
        
        
    
