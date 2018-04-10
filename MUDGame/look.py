import character, room, npc, player, attack, os, operator, random, item, job, race, time, mapmod, look, go
from admin import adminer

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

def look(command,splitIn,npcL,cRoom,cChar,cPlayer):
    if len(splitIn) == 1:
        npcCRoom = []
        for c in npcL:
            if npc.loadNpc(c, "mob").location == cChar.location:
                npcCRoom.append(c)
        print(cRoom.description)
        if len(npcCRoom) > 0:
            print("Also present: ", end="")
            for c in npcCRoom:
                mob = npc.loadNpc(c, "mob")
                if mob.angry:
                    print(colors.fg.red + mob.name + colors.reset, end = "")
                elif not mob.angry:
                    print(colors.fg.green + mob.name + colors.reset, end = "")
                if npcCRoom.index(mob.name) != len(npcCRoom):
                    print(", ", end = "")
            print("")
    else:
        if splitIn[1] in cRoom.stuffDescription:
            print(cRoom.stuffDescription[splitIn[1]])
        elif splitIn[1] in cRoom.inventory:
            print(splitIn[1][0].upper() + splitIn[1][1:] + "--> " + cRoom.inventory[splitIn[1]])
        elif splitIn[1] in cChar.inventory:
            print(splitIn[1][0].upper() + splitIn[1][1:] + "--> " + cChar.inventory[splitIn[1]])
        elif splitIn[1] in ["inventory", "inv", "backpack", "sack"]:
            if len(cChar.inventory) > 0:
                items = cChar.inventory
                print(colors.fg.orange + "Inventory: ")
                print("-----------"+ colors.fg.cyan)
                for key in items:
                    print(str(key)[0].upper() + str(key)[1:])
                print(colors.reset, end='')
            else:
                print("Your inventory is empty")
        elif splitIn[1] in [cChar.name.lower(), "self"]:
            character.checkLevel(cChar)
            print(colors.fg.orange + 'Name: '+ colors.fg.cyan + str(cChar.name))
            print(colors.fg.orange + 'Race: ' + colors.fg.cyan + str(cChar.race))
            print(colors.fg.orange + 'Job: '+ colors.fg.cyan + str(cChar.job))
            print(colors.fg.orange + 'Level: '+ colors.fg.purple + str(cChar.level))
            print(colors.fg.orange + "Exp: ["+ colors.fg.purple + str(cChar.exp) + colors.reset + " / " + colors.fg.purple + str(cChar.expneed) + colors.reset + "]")
            print(colors.fg.orange + 'Character Stats: '+ colors.fg.cyan + str(cChar.stats))
            weapon = item.loadItem(cChar.onPerson['weapon'],"wpn")
            armor = item.loadItem(cChar.onPerson['armor'],"arm")
            shield = item.loadItem(cChar.onPerson['shield'],"shd")
            print(colors.fg.orange + 'Equipment StatBonus: '+ colors.fg.cyan + '{wit: '+str(weapon.giver['wit']+armor.giver['wit']+shield.giver['wit'])+', strength: '+str(weapon.giver['strength']+armor.giver['strength']+shield.giver['strength'])+
                  ', agility: '+str(weapon.giver['agility']+armor.giver['agility']+shield.giver['agility'])+', luck: '+str(weapon.giver['luck']+armor.giver['luck']+shield.giver['luck'])+'}')
            print(colors.fg.orange + 'Health: ['+ colors.fg.green + str(cChar.health) + colors.reset + ' / ' + colors.fg.green + str(cChar.maxhealth) + colors.reset + ']')
            print()
            if len(cChar.inventory) > 0:
                items = cChar.inventory
                print(colors.fg.orange + "Inventory: ")
                print("-----------" + colors.fg.cyan)
                for key in items:
                    print(str(key)[0].upper() + str(key)[1:])
                print(colors.reset, end='')
                print()
            else:
                print("Your inventory is empty")
                print()
            print(colors.fg.orange + "Equipment: ")
            print("-----------")
            for key in cChar.onPerson:
                print(colors.fg.orange + key + " --> "+ colors.fg.cyan + cChar.onPerson[key])
                if key == 'weapon':
                    c = 'wpn'
                if key == 'armor':
                    c = 'arm'
                if key == 'shield':
                    c = 'shd'
                if not key == 'bag':
                    equip = item.loadItem(cChar.onPerson[key],c)
                    print(colors.fg.orange + 'StatBonus: '+ colors.fg.cyan + str(equip.giver))
            print()
            if cPlayer.admin:
                print(colors.fg.orange + "You posess the power of the kitten. Use it in a pawsitive manner.")
            print(colors.reset, end='')
        elif splitIn[1] in ['name']:
            character.checkLevel(cChar)
            print(colors.fg.orange + 'Name: '+ colors.fg.cyan + cChar.name)
            print(colors.reset, end='')
        elif splitIn[1] in ['race', 'origin']:
            print(colors.fg.orange + 'Race: ' + colors.fg.cyan + cChar.race)
            print(raceDescriptions[cChar.race])
            print(colors.reset, end='')
        elif splitIn[1] in ['job', 'occupation', 'class']:
            print(colors.fg.orange + 'Job: '+ colors.fg.cyan + cChar.job)
            print(colors.reset, end='')
        elif splitIn[1] in ['equipment', 'on person', 'on me', 'worn']:
            print(colors.fg.orange + "Equipment: ")
            print("-----------")
            for key in cChar.onPerson:
                print(colors.fg.orange + key + " --> "+ colors.fg.cyan + cChar.onPerson[key])
                if key == 'weapon':
                    c = 'wpn'
                if key == 'armor':
                    c = 'arm'
                if key == 'shield':
                    c = 'shd'
                if not key == 'bag':
                    equip = item.loadItem(cChar.onPerson[key],c)
                    print(colors.fg.orange + 'StatBonus: '+ colors.fg.cyan + str(equip.giver))
            print()
            if cPlayer.admin:
                print(colors.fg.orange + "You posess the power of the kitten. Use it in a pawsitive manner.")
            print(colors.reset, end='')
        elif splitIn[1] in ['stats']:
            print(colors.fg.orange + 'Stats: '+ colors.fg.cyan + str(cChar.stats))
            weapon = item.loadItem(cChar.onPerson['weapon'],"wpn")
            armor = item.loadItem(cChar.onPerson['armor'],"arm")
            shield = item.loadItem(cChar.onPerson['shield'],"shd")
            print(colors.fg.orange + 'Equipment StatBonus: '+ colors.fg.cyan + '{wit: '+str(weapon.giver['wit']+armor.giver[wit]+shield.giver['wit'])+', strength: '+str(weapon.giver['strength']+armor.giver['strength']+shield.giver['strength'])+
                  ', agility: '+str(weapon.giver['agility']+armor.giver['agility']+shield.giver['agility'])+', luck: '+str(weapon.giver['luck']+armor.giver[luck]+shield.giver['luck'])+'}')
            print(colors.fg.orange + 'Health: ['+ colors.fg.green + str(cChar.health) + colors.reset + ' / ' + colors.fg.green + str(cChar.maxhealth) + colors.reset + ']')
        elif splitIn[1] in ['str', 'strength']:
            print(colors.fg.orange + 'Strength: '+ colors.fg.cyan + str(cChar.stats['strength']))
            print(colors.reset, end='')
        elif splitIn[1] in ['wits', 'wit', 'intelligence', 'int', 'brains']:
            print(colors.fg.orange + 'Wit: '+ colors.fg.cyan + str(cChar.stats['wit']))
            print(colors.reset, end='')
        elif splitIn[1] in ['agi', 'agility']:
            print(colors.fg.orange + 'Agility: '+ colors.fg.cyan + str(cChar.stats['agility']))
            print(colors.reset, end='')
        elif splitIn[1] in ['luck']:
            print(colors.fg.orange + 'Luck: '+ colors.fg.cyan + str(cChar.stats['luck']))
            print(colors.reset, end='')
        elif splitIn[1] in ['hp', 'health']:
            print(colors.fg.orange + 'Health: ['+ colors.fg.green + str(cChar.health) + colors.reset + ' / ' + colors.fg.green + str(cChar.maxhealth) + colors.reset + ']')
            print(colors.reset, end='')
        elif splitIn[1] in ['lvl', 'level']:
            print(colors.fg.orange + 'Level: '+ colors.fg.purple + str(cChar.level))
            print(colors.reset, end='')
        elif splitIn[1] in ['exp', 'xp', 'experience']:
            print(colors.fg.orange + "Exp: ["+ colors.fg.purple + str(cChar.exp) + colors.reset + " / " + colors.fg.purple + str(cChar.expneed) + colors.reset + "]")
            print(colors.reset, end='')
        elif splitIn[1] in npcL:
            print(npc.loadNpc(splitIn[1], "mob").description)
        else:
            print("There is no "+ splitIn[1] + " here.")
