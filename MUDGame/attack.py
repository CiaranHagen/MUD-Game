import os, npc, random, time, item, character, room
"""
weaponDict = {

#[name, level, cost]
"default":[1, 0],
"rusty sword":[2, 20],
"short sword":[3, 100],
"long sword":[4, 150],
"dwarven sword":[5, 200],
"elven sword":[6, 300],
"uber-blade":[10, 1000]
}
shieldDict = {
#[name, level, cost]
"default":[1, 0],
"cardboard shield":[2, 20],
"fence fragment":[3, 100],
"wooden shield":[4, 150],
"metal shield":[5, 300],
"firewall":[6, 500],
"towel":[10, 1000]
}
armorDict = {
#[name, level, cost]
"default":[1, 0],
"linen clothes":[2, 20],
"leather armor":[3, 100],
"orkish armor":[4, 150],
"dwarven armor":[5, 200],
"elven armor":[6, 300],
"rayshielded suit":[10, 1000]
}
"""
def hit(attacker, defender):
    ranDamage = random.randint(0, 51)
    if type(attacker) == character.Character:
        ranDamage = random.randint(0 + attacker.stats["luck"], 51)
        ranDamage += attacker.stats["strength"]
    Damage = ranDamage * item.loadItem(attacker.onPerson["weapon"], "wpn").attackValue - item.loadItem(defender.onPerson["armor"], "arm").defenceValue - item.loadItem(defender.onPerson["shield"], "shd").defenceValue
    if Damage < 0:
        Damage = (-1) * Damage
    defender.health -= Damage
    print(attacker.name + " hit " + defender.name + " for " + str(Damage) + " damage. \n")
    return Damage

def fight(char, npc):
    draw(npc)
    damageToll = 0
    while True:
        action = input("\033[31mo\033[33m-\033[90m(\033[37m==> ")
        if action in ["hit", "slash", "lunge", "stab"]:
            damageToll += hit(char, npc)
            time.sleep(1)
            if npc.health <= 0:
                #os.system("clear")
                print("You are victorious!")
                drawDead(npc)
                os.system("rm ../data/npcs/mob_" + npc.name + ".txt")
                del npc
                return "mob"

        elif action in ["flee", "retreat", "run", "turn tail"]:
            chance = random.randint(0, 2)
            if chance == 0:
                print("You manage to flee the scene and sit in a corner, shivering like the coward that you are.")
                char.move(random.choice(room.loadRoom('room' + str(char.location[0]) + '_' + str(char.location[1])).possibleDirections.values()))
                return "none"
            else:
                print("The enemy hit you back into the room.")        

        elif action in ["dodge", "roll", "parry"]:
            chance = random.randint(0, 2 + char.stats["agility"])
            if chance in range(1, 2 + char.stats["agility"]):
                print("You evade the enemy's attack.")
                continue
            else:
                print("Bad luck. The enemy hit you anyways.")
        else:
            print("That is not an option...")
            continue
        hit(npc, char)
        if char.health <= 0:
            print(damageToll)
            print("You have died.")
            char.location = [0,0]
            char.health = 100
            print()
            print("You have returned to the start-room.")
            print("".center(os.get_terminal_size().columns, "-"))
            return "char"

def draw(mob):
    print()
    print("                   (    )")
    print("                  ((((()))")
    print("                  |o\ /o)|")
    print("                  ( (  _')")
    print("                   (._.  /\__")
    print("                  ,\___,/ '  ')")
    print("    '.,_,,       (  .- .   .    )")
    print("     \   \\\\     ( '        )(    )")
    print("      \   \\\\    \.  _.__ ____( .  |")
    print("       \  /\\\\   .(   .'  /\  '.  )")
    print("        \(  \\\\.-' ( /    \/    \)")
    print("         '  ()) _'.-|/\/\/\/\/\|")
    print("             '\\\\ .( |\/\/\/\/\/|")
    print("               '((  \    /\    /")
    print("               ((((  '.__\/__.')")
    print("                ((,) /   ((()   )")
    print("                 \"..-,  (()(\"   /")
    print("                  _//.   ((() .\"")
    print("          _____ //,/\" ___ ((( ', ___")
    print("                           ((  )")
    print("                            / /")
    print("                          _/,/'")
    print("                        /,/,\"")
    print()

def drawDead(mob):
    print()
    print("                   (    )")
    print("                  ((((()))")
    print("                  |x\ /x)|")
    print("                  ( (  _')")
    print("                   (._.  /")
    print("                   \___,/")
    print()
    print()
    print()
    print()
    
    print("\033[31m                      . .")
    print("                     ` ' `")
    print("                 .'''. ' .'''.")
    print("                  .. ' ' ..")
    print("                  '  '.'.'  '")
    print("                  .'''.'.'''.")
    print("                  ' .''.''. '")
    print("                   . . : . .")
    print("                  '   ':'   '")
    print("                       :   \033[0m__")
    print("                  ,   \033[31m :  \033[0m'  ')")
    print("    '.,_,,       (  .- .   .    )")
    print("     \   \\\\     ( '        )(    )")
    print("      \   \\\\    \.  _.__ ____( .  |")
    print("       \  /\\\\   .(   .'  /\  '.  )")
    print("        \(  \\\\.-' ( /    \/    \)")
    print("         '  ()) _'.-|/\/\/\/\/\|")
    print("             '\\\\ .( |\/\/\/\/\/|")
    print("               '((  \    /\    /")
    print("               ((((  '.__\/__.')")
    print("                ((,) /   ((()   )")
    print("                 \"..-,  (()(\"   /")
    print("                  _//.   ((() .\"")
    print("          _____ //,/\" ___ ((( ', ___")
    print("                           ((  )")
    print("                            / /")
    print("                          _/,/'")
    print("                        /,/,\"")
    print()
    
        
        
    
