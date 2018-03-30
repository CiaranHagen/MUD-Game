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

def loadCRoom(cChar):
    roomName = "room" + str(cChar.location[0]) + "_" + str(cChar.location[1])
    cRoom = room.loadRoom(roomName)
    return cRoom


def go(command,splitIn,cRoom,roomL,cChar,cPlayer,npcL):
    if len(splitIn) > 1:
        if splitIn[1] in cRoom.possibleDirections:
            movePerm = True
            npcCRoom = []
            for c in npcL:
                if npc.loadNpc(c, "mob").location == cChar.location:
                    print('a')
                    npcCRoom.append(c)
            for c in npcCRoom:
                mob = npc.loadNpc(c, "mob")
                print('b')
                if mob.angry:
                    movePerm = False
            if movePerm == False:
                print("At least one mob is blocking your way. You cannot leave here without defeating him...")
            elif movePerm == True:
                cChar.move(splitIn[1])
                print('c')
                cRoom.save()
                print('d')
                cRoom = loadCRoom(cChar)
                print('e')
                print("You go " + splitIn[1] + ".")

                # ------- Move mobs -------- #

                for c in npcL:
                    moveRan = random.randint(0,2)
                    if moveRan == 0:
                        mobber = npc.loadNpc(c, "mob")
                        print('f')
                        mobber.move()
                        print('g')
                 # -------------------------- #
        elif (cPlayer.admin == True) and (len(splitIn[1].split(" ")) > 1):
            try:
                coords = splitIn[1].split(" ")
                print('h')
                if ("room" + coords[0] + "_" + coords[1]) in roomL:
                    cChar.location = [int(coords[0]), int(coords[1])]
                    print()
                    print("You've teleported to "+ coords[0] + ", " + coords[1])
                    print()
                    cRoom.save()
                    print('i')
                    cRoom = loadCRoom(cChar)
                    print('j')
                    for c in npcL:
                        moveRan = random.randint(0,2)
                        if moveRan == 0:
                            mobber = npc.loadNpc(c, "mob")
                            print('k')
                            mobber.move()
                            print('l')
                            npc.loadNpc(c, "mob")
                            print('m')
                else:
                    print("Apparently you are too stupid to use coordinates. Do... you... need... help... ? (Tries using sign language...)")
            except Exception as e:
                print(e)
                print("Apparently you are too stupid to use coordinates. Do... you... need... help... ? (Tries using sign language...)")
        elif ("key" in cChar.inventory) and (cRoom.location == (2,1)) and (splitIn[1] == "east"):
            movePerm = True
            npcCRoom = []
            for c in npcL:
                if npc.loadNpc(c, "mob").location == cChar.location:
                    npcCRoom.append(c)
            for c in npcCRoom:
                mob = npc.loadNpc(c, "mob")
                if mob.angry:
                    movePerm = False
            if movePerm == False:
                print("At least one mob is blocking your way. You cannot leave here without defeating him...")
            elif movePerm == True:
                cChar.location = [3,1]
                cRoom.save()
                cRoom = loadCRoom(cChar)
                print("You go " + splitIn[1] + ".")
                if cChar.level == 0:
                    cChar.level = 1
                    print()
                    print("Congratulations. You have completed the tutorial dungeon and reached level 1.")
                    time.sleep(0.5)
                    job.jobLevelUp(cChar)
                    time.sleep(0.5)
                    print('Calculating accumulated EXP ...')
                    time.sleep(0.5)
                    character.checkLevel(cChar)
                    if cChar.level == 2:
                        job.jobLevelUp(cChar)
                        time.sleep(0.5)
                        character.checkLevel(cChar)
                        if cChar.level == 3:
                            job.jobLevelUp(cChar)
                    else:
                        print('you do not seem to have accumulated enough EXP to further increase your level')
        else:
            print("You cannot go " + splitIn[1] + ". Possible directions are: ", end = '')
            for key in cRoom.possibleDirections:
                print(key , end = ' ')
            print("")
    else:
        print("Where do you want to go? Add a cardinal direction behind 'go'! Possible directions are: ", end = '')
        for key in cRoom.possibleDirections:
            print(key , end = ' ')
        print("")
    cChar.save()
