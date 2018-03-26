import character,room, npc, player, attack, os, operator, random, item,job, race, time

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




print("Commands are: room, mob, map, quit, createitem, add, addtoroom")
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
            roomL = room.loadRooms()

        elif commAdmin == "mob":
            print("Creating new mob...")
            npc.newMob()
            npcL = npc.loadNpcs()
            for c in npcL:
                npc.loadNpc(c, "mob")

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
            mapper(litX, bigX, litY, bigY, mapL)

        elif commAdmin == "createitem":
            kind = input("weapon, armor or shield: ")
            if kind == "weapon":
                item.newWeapon()
            elif kind == "shield":
                item.newShield()
            elif kind == "armor":
                item.newArmor()

        elif commAdmin == "addtoroom":
            rom = input("Room coords (<x> <y>): ")
            itemName = input("Item-name: ").lower()
            descr = input("Enter a description: ")
            addToInv = input("Add to inventory (y/n): ")
            coords = rom.split(" ")
            room.loadRoom("room" + coords[0] + "_" + coords[1]).stuffDescription[itemName] = descr
            if addToInv == "y":
                room.loadRoom("room" + coords[0] + "_" + coords[1]).inventory[itemName] = descr
            print("Added " + itemname + " to " + "room" + coords[0] + "_" + coords[1] + ".")

        elif commAdmin == "quit":
            print()
            print("Quitting...")
            print()
            break
        else:
            print("Possible commands are \"room\", \"mob\", \"map\", \"createitem\", \"addtoroom\" and \"quit\".")

    except Exception as e:
        print(e)
        print("Weeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee... Samfing diiidn't wörk.")
