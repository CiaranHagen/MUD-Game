import os, npc, random, time
def hit(attacker, defender):
    ranDamage = random.randint(0, 11)
    Damage = ranDamage #* attacker.weaponLevel - defender.armorLevel
    defender.health -= Damage
    print(attacker.name + " hit " + defender.name + " for " + str(Damage) + " damage. \n")

def fight(char, npc):
    draw(npc)
    while True:
        hit(char, npc)
        time.sleep(1)
        if npc.health <= 0:
            os.system("clear")
            print("You are victorious!")
            drawDead(npc)
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
    print("                  |o\ /o)|")
    print("                  ( (  _')")
    print("                   (._.  /")
    print("                   \___,/")
    print()
    print()
    print()
    print()
    
    print("                      . .")
    print("                     ` ' `")
    print("                 .'''. ' .'''.")
    print("                  .. ' ' ..")
    print("                  '  '.'.'  '")
    print("                  .'''.'.'''.")
    print("                  ' .''.''. '")
    print("                   . . : . .")
    print("                  '   ':'   '")
    print("                       :   __")
    print("                  ,    :  '  ')")
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
    
        
        
    
