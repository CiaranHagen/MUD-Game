import os, npc, random, time
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
def hit(attacker, defender):
    ranDamage = random.randint(0, 11)
    Damage = ranDamage * weaponDict[attacker.onPerson["weapon"]][0] - armorDict[defender.onPerson["armor"]][0] - shieldDict[defender.onPerson["shield"]][0]
    if Damage < 0:
        Damage = (-1) * Damage
    defender.health -= Damage
    print(attacker.name + " hit " + defender.name + " for " + str(Damage) + " damage. \n")
    return Damage

def fight(char, npc):
    draw(npc)
    damageToll = 0
    while True:
        damageToll += hit(char, npc)
        time.sleep(1)
        if npc.health <= 0:
            os.system("clear")
            print(damageToll)
            print("You are victorious!")
            drawDead(npc)
            os.system("rm ../data/npcs/mob_" + npc.name + ".txt")
            del npc
            return "mob"

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
    
        
        
    
