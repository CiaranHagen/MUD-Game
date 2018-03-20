import os, npc, random
def hit(attacker, defender):
    ranDamage = random.randint(0, 11)
    Damage = ranDamage #* attacker.weaponLevel - defender.armorLevel
    defender.health -= Damage
    print(attacker.name + " hit " + defender.name + " for " + str(Damage) + " damage. \n")

def fight(char, npc):
    
    while True:
        hit(char, npc)
        if npc.health <= 0:
            print("You are victorious!")
            os.system("rm ../data/npcs/mob_" + npc.name + ".txt")
            del npc
            return "mob"

        hit(npc, char)
        if char.health <= 0:
            print("You have died.")
            char.location = [0,0]
            char.health = 100
            print()
            print("You have returned to the start-room.")
            print("".center(os.get_terminal_size().columns, "-"))
            return "char"
    
        
        
    
