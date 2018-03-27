import character,room, npc, player, attack, os, operator, random, item, job, race, time

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

def mapper(litX, bigX, litY, bigY, mapL):
    drawL = []
    distX = (-1) * litX
    distY = (-1) * litY
    for j in range(litY, bigY+1):
        drawL.append([])
        for i in range(litX, bigX+1):
            if (i,j) in mapL:
                drawL[j + distY].append("O")
            else:
                drawL[j + distY].append(" ")
    dis = (bigX - litX - 2)//2
    if dis < 2:
        dis = 2
    print(dis*"=" + " MAP " + dis*"=")
    print()
    for j in range(bigY, litY-1, -1):
        spaceLine = " "
        print(" ", end="")
        for i in range(litX, bigX+1):
            if cRoom.location == (i,j):
                print(colors.fg.red, end='')
            else:
                print(colors.fg.cyan, end='')
            print(drawL[j + distY][i + distX], end='')
            print(colors.fg.cyan, end='')
            if (drawL[j + distY][i + distX] == "O") and ((i + distX) != (len(drawL[j+distY])-1)):
                if "east" in room.loadRoom("room" + str(i) + "_" + str(j)).possibleDirections.values():
                    print(colors.fg.cyan + "--", end='')
                else:
                    print("  ", end='')
            else:
                print("  ", end='')

            if (drawL[j + distY][i + distX] == "O") and ((j + distY) != 0):
                if "south" in room.loadRoom("room" + str(i) + "_" + str(j)).possibleDirections.values():
                    spaceLine += "|  "
                else:
                    spaceLine += "   "
            else:
                spaceLine += "   "

        print("", end="\n")
        print(spaceLine)
    print(colors.reset , end = '')
    print(dis*"=" + " MAP " + dis*"=")


def adminer(cPlayer, cChar, cRoom, roomL):
    print("Commands are: room, mob, map, quit, createitem, additem, addtoroom, changestats, crown <username>")
    while True:
        print()
        try:
            admIn = input(colors.fg.red + ">> " + colors.fg.pink)
            print(colors.reset , end = '')
            commAdmin = ""
            splitMin = admIn.split(" ")
            for w in splitMin:
                w = w.lower()
            commAdmin = splitMin[0]
            print()
            if commAdmin == "room":
                coord = input("Please enter the coordinates (seperate by space): ")
                room.newRoom(int(coord.split(' ')[0]), int(coord.split(' ')[1]))
            """
            elif commAdmin == "mob":
                print("Creating new mob...")
                npc.newMob()
            """
            elif commAdmin == "map":
                mapL = []
                for o in roomL:
                    oCoord = o[4:]
                    x = oCoord.split("_")[0]
                    y = oCoord.split("_")[1]
                    mapL.append((int(x),int(y)))
                bigY = max(mapL,key=operator.itemgetter(1))[1]
                bigX = max(mapL,key=operator.itemgetter(0))[0]
                litY = min(mapL,key=operator.itemgetter(1))[1]
                litX = min(mapL,key=operator.itemgetter(0))[0]
                main.mapper(litX, bigX, litY, bigY, mapL)

            elif commAdmin == "createitem":
                kind = input("weapon, armor or shield: ").lower()
                if kind == "weapon":
                    item.newWeapon()
                elif kind == "shield":
                    item.newShield()
                elif kind == "armor":
                    item.newArmor()

            elif commAdmin == "changestats":
                changestats = 1
                while changestats == 1:
                    print(colors.fg.orange + 'Stats: '+ colors.fg.cyan + str(cChar.stats))
                    print(colors.fg.orange + 'MaxHealth: '+ colors.fg.green + str(cChar.maxhealth))
                    print()
                    print(colors.reset, end='')
                    print ('what stat do you wish to modify ? (' + colors.fg.orange + 'strength' + colors.reset + ' / ' + colors.fg.orange + 'agility' + colors.reset + ' / '
                           + colors.fg.orange + 'wit' + colors.reset + ' / ' + colors.fg.orange + 'luck' + colors.reset + ' / ' + colors.fg.green + 'maxhealth' + colors.reset + ')')
                    choice = input('>').lower()

                    if choice in ['strength', 'agility', 'wit', 'luck']:
                        confirm = 1
                        while confirm == 1:
                            print('your ' + colors.fg.orange + str(choice) + colors.reset + ' is: '+ colors.fg.cyan + str(cChar.stats[str(choice)]) + colors.reset)
                            print()
                            print('input new value')
                            value = input('>')
                            try:
                                if (int(value) >= 0):
                                    cChar.stats[str(choice)] = int(value)
                                    print('your new ' + colors.fg.orange + str(choice) + colors.reset + ' is: '+ colors.fg.cyan + str(cChar.stats[str(choice)]) + colors.reset)
                                    answer = ''
                                    while answer not in ['y', 'yes','n', 'no']:
                                        print()
                                        print('do you wish to continue modifying your stats ?')
                                        print("[" + colors.fg.green + "yes" + colors.reset + "/" + colors.fg.red + "no" + colors.reset + "]")
                                        answer = input('>').lower()
                                        if answer in ['y', 'yes']:
                                            changestats = 1
                                            confirm = 0
                                        elif answer in ['n', 'no']:
                                            changestats = 0
                                            confirm = 0
                                            Print('Quitting ...')
                                        elif answer not in ['y', 'yes','n', 'no']:
                                            print(str(answer) + ' is not a valid input, try again :')
                            except Exception as e:
                                print(e)
                                print("Very clever... C'mon, I need numbers dude! N U M B E R S!")

                    if choice in ['maxhealth']:
                        confirm = 1
                        while confirm == 1:
                            print('your ' + colors.fg.orange + str(choice) + colors.reset + ' is: '+ colors.fg.cyan + str(cChar.maxhealth) + colors.reset)
                            print()
                            print('input new value')
                            value = input('>')
                            try:
                                if (int(value) >= 0):
                                    cChar.maxhealth = int(value)
                                    cChar.health = cChar.maxhealth
                                    print('your new ' + colors.fg.orange + str(choice) + colors.reset + ' is: '+ colors.fg.cyan + str(cChar.maxhealth) + colors.reset)
                                    answer = ''
                                    while answer not in ['y', 'yes','n', 'no']:
                                        print()
                                        print('do you wish to continue modifying your stats ?')
                                        print("[" + colors.fg.green + "yes" + colors.reset + "/" + colors.fg.red + "no" + colors.reset + "]")
                                        answer = input('>').lower()
                                        if answer in ['y', 'yes']:
                                            changestats = 1
                                            confirm = 0
                                        elif answer in ['n', 'no']:
                                            changestats = 0
                                            confirm = 0
                                            Print('Quitting ...')
                                        elif answer not in ['y', 'yes','n', 'no']:
                                            print(str(answer) + ' is not a valid input, try again :')
                            except Exception as e:
                                print(e)
                                print("Very clever... C'mon, I need numbers dude! N U M B E R S!")

                    elif choice in ['q', 'quit']:
                        quit = 1
                        while quit == 1:
                            print('Are you sure you wish to quit ?')
                            print("[" + colors.fg.green + "yes" + colors.reset + "/" + colors.fg.red + "no" + colors.reset + "]")
                            answer = input('>').lower()
                            if answer in ['y', 'yes']:
                                print('Quitting ...')
                                quit = 0
                                changestats = 0
                                confirm = 0
                                continue
                            elif answer in ['n', 'no']:
                                quit = 0
                                changestats = 1
                                confirm = 0
                                continue

                    elif choice not in ['q', 'quit', 'strength', 'agility', 'wit', 'luck', 'health']:
                        print('The status ' + colors.fg.orange + str(choice) + colors.reset + ' is not known to me or the game ... try again or enter' + colors.fg.orange + ' quit' + colors.reset + ' to abort')
                        continue

            elif commAdmin == "additem":
                kind = input("weapon, armor or shield: ")
                if kind == "weapon":
                    kind = 'wpn'
                elif kind == "shield":
                    kind = 'shd'
                elif kind == "armor":
                    kind = 'arm'
                print('Input the name of the item')
                name = input('>')
                cChar.inventory[name] = item.loadItem(name, kind).description
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

            elif commAdmin == "addtoroom":
                rom = input("Room coords (<x> <y>): ")
                itemName = input("Item-name: ").lower()
                descr = input("Enter a description: ")
                addToInv = input("Add to inventory (y/n): ")
                coords = rom.split(" ")
                room.loadRoom("room" + coords[0] + "_" + coords[1]).stuffDescription[itemName] = descr
                if addToInv == "y":
                    rom = room.loadRoom("room" + coords[0] + "_" + coords[1])
                    rom.inventory[itemName] = descr
                    rom.save()
                print("Added " + itemName + " to " + "room" + coords[0] + "_" + coords[1] + ".")
            
            elif commAdmin == "addroomdir":
                rom = input("Room coords (<x> <y>): ")
                pointerDir = input("Direction: ")
                actualDir = input("Whereto: ")
                coords = rom.split(" ")
                rom = room.loadRoom("room" + coords[0] + "_" + coords[1])
                rom.possibleDirections[pointerDir] = actualDir
                rom.save()
            
            elif commAdmin == "crown":
                cPlayer.admin = True
                cPlayer.save()
                if cPlayer.admin:
                    print("Player " + cPlayer.username + " is now admin.")

            elif commAdmin == "quit":
                print()
                print("Returning to game...")
                print()
                return
            else:
                print("Possible commands are \"room\", \"mob\", \"map\", \"createitem\", \"additem\", \"addtoroom\", \"changestats\", \"crown <username>\" and \"quit\".")
        except Exception as e:
            print(e)
            print("Weeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee... Samfing diiidn't wörk.")
            return
