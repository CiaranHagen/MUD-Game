import os, npc, random, time, item, character, room, job, race, time

class colors:
    '''Colors class:reset all colors with colors.reset; two
    sub classes fg for foregroun
    and bg for background; use as colors.subclass.colorname.
    i.e. colors.fg.red or colors.bg.greenalso, the generic bold, disable,
    underline, reverse, strike through,
    and invisible work with the main class i.e. colors.bold'''
    reset='\033[0m'
    bold='\033[01m'
    disable='\033[02m'
    underline='\033[04m'
    reverse='\033[07m'
    strikethrough='\033[09m'
    invisible='\033[08m'
    class fg:
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'
    class bg:
        black='\033[40m'
        red='\033[41m'
        green='\033[42m'
        orange='\033[43m'
        blue='\033[44m'
        purple='\033[45m'
        cyan='\033[46m'
        lightgrey='\033[47m'


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

def smite(char, npc):
    char.exp += npc.level * 50
    levelBefore = int(char.level)
    character.checkLevel(char)
    drawDead(npc)
    time.sleep(2)
    print('\033[08m')
    os.system("clear")
    print('\033[0m')
    print("You are victorious!")
    print()
    print("Gained " + str(npc.level * 50) + " EXP.")
    if char.level > levelBefore:
        job.jobLevelUp(char)
    os.system("rm ../data/npcs/mob_" + npc.name + ".txt")
    del npc
    return "mob"


def hit(attacker, defender):
    attWeapon = item.loadItem(attacker.onPerson["weapon"], "wpn")
    defArmor = item.loadItem(defender.onPerson["armor"], "arm")
    defShield = item.loadItem(defender.onPerson["shield"], "shd")
    ranDamage = random.randint(0, 51)
    attWeaponV = attWeapon.attackValue
    defArmorV = defArmor.defenceValue
    defShieldV = defShield.defenceValue

    # Special calcs for characters
    if type(attacker) == character.Character:
        attWeapon.health -= 1
        if ((attWeapon.kind == "dagger") and (attacker.job == "rogue")):
            if (attacker.level >= 3):
                chance = random.randint(0 + attacker.stats["luck"], 2 + attacker.stats["agility"])
                if chance in range(1 + npc.level*2 - attacker.level, 2 + attacker.stats["agility"]):
                    print()
                    print('! Double Strike !')
                    print()
                    attWeaponV += attacker.stats['agility'] * 2
            else:
                attWeaponV += attacker.stats['agility']

        if ((attWeapon.kind == "sword") and (attacker.job == "warrior")):
            if (attacker.level >= 3):
                chance = random.randint(0 + attacker.stats["luck"], 2 + attacker.stats["strength"])
                if chance in range(1 + npc.level*2 - attacker.level, 2 + attacker.stats["strength"]):
                    print()
                    print('! Heavy Strike !')
                    print()
                    attWeaponV += attacker.stats['strength'] * 2
            else:
                attWeaponV += attacker.stats['strength']

        ranDamage = random.randint(0 + attacker.stats["luck"], 51 + attacker.stats["luck"])
        ranDamage += attacker.stats["strength"]
    if type(defender) == character.Character:
        if defArmor.health == 0:
            print("Your armor is broken and fails to protect you.")
        if defShield.health == 0:
            print("Your shield is broken and fails to protect you.")
    # General calcs
    if defArmor.health > 0:
        defArmor.health -= 1
    elif defArmor.health == 0:
        defArmorV = 0
    if defShield.health > 0:
        defShield.health -= 1
    elif defShield.health == 0:
        defShieldV = 0

    Damage = ranDamage * attWeaponV - defArmorV - defShieldV
    if Damage < 0:
        Damage = 0

    oldHP = defender.health
    defender.health -= Damage
    print(attacker.name + " hit " + defender.name + " for " + str(Damage) + " damage. \n")

    if type(attacker) == npc.Mob and defender.health > 0 :
        if ((Damage *100)/oldHP) > 80:
            print("Dang!! That bastard almost killed you! Consider retreat weakling.")
        if ((Damage *100)/oldHP) <= 80 and ((Damage *100)/oldHP) > 50:
            print("Oh man, that was a hard hit. One more like this and you kick the bucket.")
        if ((Damage *100)/oldHP) <= 50 and ((Damage *100)/oldHP) > 30:
            print("Outch!! A big scratch for a big boy")
        if ((Damage *100)/oldHP) <= 30 and ((Damage *100)/oldHP) > 10:
            print("You're bleeding here and there, but nothing that could stop a proud "+defender.race+".")
        if ((Damage *100)/oldHP) <= 10:
            print("You didn't even flinch. Your enemy looks at you in shock. Kill that impotent whim.")

    return Damage

def fight(char, npc):
    draw(npc)
    damageToll = 0
    while True:
        action = input("\033[31mo\033[33m-\033[90m(\033[37m==> ")
        if action in ["hit", "slash", "lunge", "stab"]:
            if item.loadItem(char.onPerson["weapon"], "wpn").health > 0:
                damageToll += hit(char, npc)
                time.sleep(1)
                if npc.health <= 0:
                    char.exp += npc.level * 50
                    levelBefore = char.level
                    character.checkLevel(char)
                    print('\033[08m')
                    os.system("clear")
                    print('\033[0m')
                    print("You are victorious!")
                    print()
                    drawDead(npc)
                    time.sleep(1)
                    print("Gained " + str(npc.level * 50) + " EXP.")
                    if char.level > levelBefore:
                        job.jobLevelUp(char)
                    os.system("rm ../data/npcs/mob_" + npc.name + ".txt")
                    del npc
                    return "mob"
            else:
                print("Your weapon is broken and useless. You desperately try to punch a better equipped opponent, but fail miserably.")

        elif action in ["flee", "retreat", "run", "turn tail"]:
            chance = random.randint(0, 2 + char.stats["luck"])
            if chance == 0:
                print("You manage to flee the scene and sit in a corner, shivering like the coward that you are.")
                char.move(random.choice(room.loadRoom('room' + str(char.location[0]) + '_' + str(char.location[1])).possibleDirections.values()))
                return "none"
            else:
                print("The enemy hit you back into the room.")

        elif action in ["dodge", "roll", "parry", "evade"]:
            if char.job == 'rogue' and char.level >= 2: #(@lvl 2, rogue gains passive evasion buff)
                chance = random.randint(0, 2 + char.stats["agility"])
                if chance in range(1 + npc.level*2 - char.level, 2 + char.stats["agility"]):
                    print("You evade the enemy's attack.")
                    continue
                else:
                    chance = random.randint(0, 2 + char.stats["agility"])
                    if chance in range(1 + npc.level*2 - char.level, 2 + char.stats["agility"]):
                        print("You evade the enemy's attack.")
                        continue
                    else:
                        print("Bad luck. The enemy hit you anyways.")
            elif not char.job == 'rogue':
                chance = random.randint(0, 2 + char.stats["agility"])
                if chance in range(1 + npc.level*2 - char.level, 2 + char.stats["agility"]):
                    print("You evade the enemy's attack.")
                    continue
                else:
                    print("Bad luck. The enemy hit you anyways.")
        else:
            print("That is not an option...")
            continue
        hit(npc, char)
        if char.health <= 0:
            print("You have died.")
            char.location = [0,0]
            char.health = 500
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
