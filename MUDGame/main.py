import character, room, npc, player, attack, os, operator, random, item, job, race, time
import sys,tty,termios

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

class BreakIt(Exception): pass

class _Getch:
    def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

def getKey():
    inkey = _Getch()
    while(1):
            k=inkey()
            if k!='':break
    return k

##========================================================================
##===================Interesting stuff starts here========================
##========================================================================

def onstart():
    newPlayer = input("Register (r) or log in (l)." + colors.fg.cyan)
    print(colors.reset , end = '')
    charL = []
    for fIterator in os.listdir("../data/characters/"):
        charL.append(fIterator[:-4])
    if newPlayer == "r":
        currentPlayer = player.newPlayer(),
        print("------------------------------------------".center(os.get_terminal_size().columns, "-"))
        print("Character creation \n")

        #i am lazy and will just copy char creation twice, at clean up we make a function of this in char.py anyway
        # I am just as lazy and followed in your footsteps xD (Faolin)
        while True:
            charactername = input("Character name: " + colors.fg.cyan)

            if charactername in charL:
                print("This name is already taken.")
                continue
            print(colors.reset , end = '')
            raceList = ['orc', 'dwarf', 'elf', 'troll', 'succubus', 'gelfling', 'gockcobbler', 'shinigami', 'hickdead', 'thraal']
            while charactername == '':
                print("Only I am the one without name!!")
                charactername = input("Character name: \n> " + colors.fg.cyan)
                print(colors.reset , end = '')
            charRace = race.chooseRace(currentPlayer)
            charJob = job.chooseJob(currentPlayer)
            #print('\n'+charJob+'\n')
            while True:
                print("Set the stats of your character. 4 different stats, 10 points to give, you know the drill.\n")
                strength = input("How " + colors.fg.cyan + "strong " + colors.reset + "are you?: \n> "+ colors.fg.cyan)
                print(colors.reset , end = '')
                agility = input("How " + colors.fg.cyan + "agile " + colors.reset + "are you?: \n> "+ colors.fg.cyan)
                print(colors.reset , end = '')
                wit = input("How would you rate your " + colors.fg.cyan + "intelligence" + colors.reset + "?: \n> "+ colors.fg.cyan)
                print(colors.reset , end = '')
                luck = input("Are you feeling " + colors.fg.cyan + "lucky" + colors.reset + "?: \n> "+ colors.fg.cyan)
                print(colors.reset , end = '')
                try:
                    if (int(strength) >= 0) and (int(agility) >= 0) and (int(wit) >= 0) and (int(luck) >= 0):
                        if currentPlayer.admin == False:
                            if (int(strength)+int(agility)+int(wit)+int(luck)) == 10:
                                if int(strength) > 4 or int(agility)>4 or int(wit)>4 or int(luck)>4:
                                    print("What the hell should this be? Well, I don't really care...")
                                elif int(wit) < 3:
                                    print("Go and have fun in the dungeons you dumdum, I bet you will have at least one peer down there.")
                                else:
                                    print("Ok, that looks pretty solid. Have fun...")
                                break
                            else:
                                print("Do you even math?")
                        elif currentPlayer.admin == True:
                            print("Well I can't really tell you what to do, so I'm not even gonna look at what you wrote...")
                            break
                except Exception as e:
                    print(e)
                    print("Very clever... C'mon, I need numbers dude! N U M B E R S!")
                print(colors.reset , end = '')

            charStats = {'wit' : 0, 'strength': 0, 'agility': 0, 'luck': 0}

            charStats['strength'] = int(job.jobStrength(charJob,strength))
            charStats['agility'] = int(job.jobAgility(charJob,agility))
            charStats['wit'] = int(job.jobWit(charJob,wit))
            charStats['luck'] = int(job.jobLuck(charJob,luck))

            print()
            print(colors.fg.orange + 'Name: '+ colors.fg.cyan + str(charactername))
            print(colors.fg.orange + 'Race: ' + colors.fg.cyan + str(charRace))
            print(colors.fg.orange + 'Job: '+ colors.fg.cyan + str(charJob))
            print(colors.fg.orange + 'Stats: '+ colors.fg.green + str(charStats))
            break

        print(colors.reset , end = '')
        currentChar = character.newCharacter(charactername, currentPlayer.username, charRace, charJob, charStats)
        print("After you spend almost an eternity in the great nothingness, also called aether, you see an open door and step through... (enter to continue)".center(os.get_terminal_size().columns, " "))
        wait = input()

    else:
        currentPlayer = player.login()
        print ("------------------------------------------".center(os.get_terminal_size().columns, "-"))
        newCharacter = input("Create new character (1) or use existing character (2)? " + colors.fg.cyan) #or show list of characters?
        print(colors.reset , end = '')
        if newCharacter == "1":
            print("Character creation \n")
            while True:
                charactername = input("Character name: " + colors.fg.cyan)
                if charactername in charL:
                    if character.characterOwn:
                        checker = input("Are you sure you want to delete your character? (y/n)")
                        if checker == "y":
                            pass
                        else:
                            continue
                    else:
                        print("You can only overwrite characters you own.")
                        continue
                print(colors.reset , end = '')
                while charactername == '':
                    print("Only I am the one without name!!")
                    charactername = input("Character name: \n> " + colors.fg.cyan)
                    print(colors.reset , end = '')
                charRace = race.chooseRace(currentPlayer)
                charJob = job.chooseJob(currentPlayer)
                print('\n'+charJob+'\n')
                while True:
                    print("Set the stats of your character. 4 different stats, 10 points to give, you know the drill.\n")
                    strength = input("How " + colors.fg.cyan + "strong " + colors.reset + "are you?: \n> "+ colors.fg.cyan)
                    print(colors.reset , end = '')
                    agility = input("How " + colors.fg.cyan + "agile " + colors.reset + "are you?: \n> "+ colors.fg.cyan)
                    print(colors.reset , end = '')
                    wit = input("How would you rate your " + colors.fg.cyan + "intelligence" + colors.reset + "?: \n> "+ colors.fg.cyan)
                    print(colors.reset , end = '')
                    luck = input("Are you feeling " + colors.fg.cyan + "lucky" + colors.reset + "?: \n> "+ colors.fg.cyan)
                    print(colors.reset , end = '')
                    try:
                        if (int(strength) >= 0) and (int(agility) >= 0) and (int(wit) >= 0) and (int(luck) >= 0):
                            if currentPlayer.admin == False:
                                if (int(strength)+int(agility)+int(wit)+int(luck)) == 10:
                                    if int(strength) > 4 or int(agility)>4 or int(wit)>4 or int(luck)>4:
                                        print("What the hell should this be? Well, I don't really care...")
                                    elif int(wit) < 3:
                                        print("Go and have fun in the dungeons you dumdum, I bet you will have at least one peer down there.")
                                    else:
                                        print("Ok, that looks pretty solid. Have fun...")
                                    break
                                else:
                                    print("Do you even math?")
                            elif currentPlayer.admin == True:
                                print("Well I can't really tell you what to do, so I'm not even gonna look at what you wrote...")
                                break
                    except Exception as e:
                        print(e)
                        print("Very clever... C'mon, I need numbers dude! N U M B E R S!")
                print(colors.reset , end = '')

                charStats = {'wit' : 0, 'strength': 0, 'agility': 0, 'luck': 0}

                charStats['strength'] = int(job.jobStrength(charJob,strength))
                charStats['agility'] = int(job.jobAgility(charJob,agility))
                charStats['wit'] = int(job.jobWit(charJob,wit))
                charStats['luck'] = int(job.jobLuck(charJob,luck))

                print()
                print(colors.fg.orange + 'Name: '+ colors.fg.cyan + str(charactername))
                print(colors.fg.orange + 'Race: ' + colors.fg.cyan + str(charRace))
                print(colors.fg.orange + 'Job: '+ colors.fg.cyan + str(charJob))
                print(colors.fg.orange + 'Stats: '+ colors.fg.green + str(charStats))
                break

            print(colors.reset , end = '')
            currentChar = character.newCharacter(charactername, currentPlayer.username, charRace, charJob, charStats)
            print("After you spend almost an eternity in the great nothingness, also called aether, you see an open door and step through... (enter to continue)".center(os.get_terminal_size().columns, " "))
            wait = input()
        else:
            charactername = input("Which character do you want to load? ")
            currentChar = character.loadCharacter(charactername, currentPlayer.username)

    roomL = room.loadRooms()

    npcL = npc.loadNpcs()

    return currentPlayer, currentChar, roomL, npcL

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
    print()
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
            if (drawL[j + distY][i + distX] == "O") and ((i + distX) != (len(drawL[j+distY])-1)):
                if "east" in room.loadRoom("room" + str(i) + "_" + str(j)).possibleDirections.values():
                    print(colors.fg.cyan + "--", end='')
                else:
                    print("  ", end='')
            else:
                print(" ", end='')

            if (drawL[j + distY][i + distX] == "O") and ((j + distY) != 0):
                if "south" in room.loadRoom("room" + str(i) + "_" + str(j)).possibleDirections.values():
                    spaceLine += "|  "
                else:
                    spaceLine += "   "
            else:
                spaceLine += "  "

        print("", end="\n")
        print(spaceLine)
    print(colors.reset , end = '')
    print(dis*"=" + " MAP " + dis*"=")
    print()

npcCRoom = []
def loadCRoom():
    roomName = "room" + str(cChar.location[0]) + "_" + str(cChar.location[1])
    cRoom = room.loadRoom(roomName)
    return cRoom



print(colors.invisible)
os.system("clear")
print(colors.reset)
print(colors.fg.lightred)
print("===================================================".center(os.get_terminal_size().columns, "="))
print("                 ,    , __   __                    ".center(os.get_terminal_size().columns, " "))
print("================ |\  /| |_\ /  _ ==================".center(os.get_terminal_size().columns, "="))
print("================ | \/ | | \ \__/ ==================".center(os.get_terminal_size().columns, "="))
print("                                                   ".center(os.get_terminal_size().columns, " "))
print("===================================================".center(os.get_terminal_size().columns, "="))
print(colors.reset)

cPlayer, cChar, roomL, npcL = onstart()

for c in npcL:
    npc.loadNpc(c, "mob")

cRoom = loadCRoom()

helpText = {"go" : "go <direction>", "look" : "look <object (optional)>", "take" : "take <object>", "quit" : "Write this if you think you have better things to do...", "help" : "Seriously? I mean ...", "attack" : "attack <attackable npc>", "map":"Prints a map of your surroundings. If you have the map achievement, it prints the whole world map."}

print(colors.invisible)
os.system("clear")
print(colors.reset)
if not cPlayer.admin:
    print()
    print(("----- Welcome " + cPlayer.username + "! -----").center(os.get_terminal_size().columns, " "))
    print()
elif cPlayer.admin:
    print()
    print("You are logged in as admin. Remember that you are not limited to cardinal directions when moving. Just write \"go <x> <y>\".")
    print()

commandL = ["help"]
while True:
    try:

        #===============Key input part==================
        """
        I have NO idea how or why this works... but it does. DO NOT change ANYTHING!!! This took me 5 to 6 hours to make!!!!!!!
        """
        inputter = ''
        if len(commandL)>0:
            i = len(commandL)
        else:
            i = 0
        print(colors.fg.red + "> " + colors.reset + inputter, end="\r")
        while True:#making a loop
            try: #used try so that if user pressed other than the given key error will not be shown
                if inputter[len(inputter)-2:len(inputter)] == "[A":
                    print(' ' * (len(inputter)+2), end = '\r')
                    if (len(commandL)>0) and (i != 0):
                        i -= 1
                        inputter = commandL[i]
                        print(colors.fg.red + "> " + colors.reset + inputter, end="\r")
                    elif i == 0:
                        inputter = "help"
                        print(colors.fg.red + "> " + colors.reset + inputter, end="\r")
                    else:
                        continue
                elif inputter[len(inputter)-2:len(inputter)] == "[B":
                    print(' ' * (len(inputter)+2), end = '\r')
                    if (len(commandL)>0) and ( i != len(commandL)-1):
                        i += 1
                        inputter = commandL[i]
                        print(colors.fg.red + "> " + colors.reset + inputter, end="\r")
                    elif i == len(commandL)-1:
                        inputter = ""
                        print(colors.fg.red + "> " + colors.reset, end="\r")
                    else:
                        continue

                k = getKey()
                print(' ' * (len(inputter)+2), end = '\r')
                if (ord(k) == 27):#up key
                    if (ord(k) == 91):
                        if (ord(k) == 65):
                            inputter = ''

                elif (ord(k) == 27):#down key
                    if (ord(k) == 91):
                        if (ord(k) == 66):
                            inputter = ''

                elif ord(k) == 13: #enter
                    commandL.append(inputter)
                    if len(commandL)>0:
                        i = len(commandL)-1
                    else:
                        i = 0
                    print(colors.fg.red + "> " + colors.reset + inputter)
                    dupliL = ["help"]
                    commandL.reverse()
                    for w in commandL:
                        if w not in dupliL:
                            dupliL.insert(1, w)
                    commandL = dupliL
                    raise BreakIt

                elif ord(k) == 127: #backspace
                    inputter = inputter[0:len(inputter)-1]
                    print(colors.fg.red + "> " + colors.reset + inputter, end="\r")

                else: #letters etc.
                    inputter += k
                    print(colors.fg.red + "> " + colors.reset + inputter, end="\r")
            except BreakIt:
                break
        #=============================================================================

        print(colors.reset , end = '')
        command = ""
        splitIn = inputter.split(" ")
        if len(splitIn) != 1:
            splitIn[1:] = [' '.join(splitIn[1:])]
        for w in splitIn:
            w = w.lower()
        command = splitIn[0]

        #========= Go [direction] ==========#

        if command in ["go", "walk", "move", "jump", "hop", "teleport", "translate", "commute"]:
            if len(splitIn) > 1:
                if splitIn[1] in cRoom.possibleDirections:
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
                        cChar.move(splitIn[1])
                        cRoom.save()
                        cRoom = loadCRoom()
                        print("You go " + splitIn[1] + ".")

                        # ------- Move mobs -------- #

                        for c in npcL:
                            moveRan = random.randint(0,2)
                            if moveRan == 0:
                                mobber = npc.loadNpc(c, "mob")
                                mobber.move()
                                npc.loadNpc(c, "mob")
                         # -------------------------- #
                elif (cPlayer.admin == True) and (len(splitIn[1].split(" ")) > 1):
                    try:
                        coords = splitIn[1].split(" ")
                        if ("room" + coords[0] + "_" + coords[1]) in roomL:
                            print("You've teleported to "+ coords[0] + ", " + coords[1])
                            cChar.location[0] = int(coords[0])
                            cChar.location[1] = int(coords[1])
                            cRoom.save()
                            cRoom = loadCRoom()
                            for c in npcL:
                                moveRan = random.randint(0,2)
                                if moveRan == 0:
                                    mobber = npc.loadNpc(c, "mob")
                                    mobber.move()
                                    npc.loadNpc(c, "mob")
                        else:
                            print("Apparently you are too stupid to use coordinates. Do... you... need... help... ? (Tries using sign language...)")
                    except Exception as e:
                        print(e)
                        print("Apparently you are too stupid to use coordinates. Do... you... need... help... ? (Tries using sign language...)")

                else:
                    print("You cannot go " + splitIn[1] + ". Possible directions are: ", end = '')
                    for key in cRoom.possibleDirections:
                        print(key , end = ' ')
                    print("\n")
            else:
                print("Where do you want to go? Add a cardinal direction behind 'go'! Possible directions are: ", end = '')
                for key in cRoom.possibleDirections:
                    print(key , end = ' ')
                print("\n")

        #========= Look [object] ==========#

        elif command in ["look", "watch", "observe", "see", "eye", "regard", "check"]:
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
                print()
            elif splitIn[1] == "self":
                print("Health: " + str(cChar.health))
                print()
                print("Equipment: ")
                print("-----------")
                for key in cChar.onPerson:
                    print(key + " --> " + cChar.onPerson[key])
                print()
                if cPlayer.admin:
                    print("You posess the power of the kitten. Use it in a pawsitive manner.")
            else:
                if splitIn[1] in cRoom.stuffDescription:
                    print(cRoom.stuffDescription[splitIn[1]])
                elif splitIn[1] in cRoom.inventory:
                    print(cRoom.inventory[splitIn[1]])
                elif splitIn[1] in cChar.inventory:
                    print(cChar.inventory[splitIn[1]])
                elif splitIn[1] == "inventory":
                    if len(cChar.inventory) > 0:
                        items = cChar.inventory
                        for key in items:
                            print(items[key])
                    else:
                        print("Your inventory is empty")
                elif splitIn[1] in [str(cChar.name), str(cChar.name).lower()]:
                    character.checkLevel(cChar)
                    print(colors.fg.orange + 'Name: '+ colors.fg.cyan + str(cChar.name))
                    print(colors.fg.orange + 'Race: ' + colors.fg.cyan + str(cChar.race))
                    print(colors.fg.orange + 'Job: '+ colors.fg.cyan + str(cChar.job))
                    print(colors.fg.orange + 'Stats: '+ colors.fg.cyan + str(cChar.stats))
                    print(colors.fg.orange + 'Health: '+ colors.fg.green + str(cChar.health))
                    print(colors.fg.orange + 'Level: '+ colors.fg.purple + str(cChar.level))
                    print(colors.fg.orange + "Exp: ["+ colors.fg.purple + str(cChar.exp) + colors.reset + " / " + colors.fg.purple + str(cChar.exp + cChar.expneed) + colors.reset + "]")
                    print(colors.reset, end='')
                elif splitIn[1].lower() in ['name']:
                    character.checkLevel(cChar)
                    print(colors.fg.orange + 'Name: '+ colors.fg.cyan + str(cChar.name))
                    print(colors.reset, end='')
                elif splitIn[1].lower() in ['race', 'origin']:
                    print(colors.fg.orange + 'Race: ' + colors.fg.cyan + str(cChar.race))
                    print(colors.reset, end='')
                elif splitIn[1].lower() in ['job', 'occupation', 'class']:
                    print(colors.fg.orange + 'Job: '+ colors.fg.cyan + str(cChar.job))
                    print(colors.reset, end='')
                elif splitIn[1].lower() in ['stats']:
                    print(colors.fg.orange + 'Stats: '+ colors.fg.cyan + str(cChar.stats))
                    print(colors.reset, end='')
                elif splitIn[1].lower() in ['str', 'strength']:
                    print(colors.fg.orange + 'Strength: '+ colors.fg.cyan + str(cChar.stats['strength']))
                    print(colors.reset, end='')
                elif splitIn[1].lower() in ['wits', 'wit', 'intelligence', 'int', 'brains']:
                    print(colors.fg.orange + 'Wit: '+ colors.fg.cyan + str(cChar.stats['wit']))
                    print(colors.reset, end='')
                elif splitIn[1].lower() in ['agi', 'agility']:
                    print(colors.fg.orange + 'Agility: '+ colors.fg.cyan + str(cChar.stats['agility']))
                    print(colors.reset, end='')
                elif splitIn[1].lower() in ['luck']:
                    print(colors.fg.orange + 'Luck: '+ colors.fg.cyan + str(cChar.stats['luck']))
                    print(colors.reset, end='')
                elif splitIn[1].lower() in ['hp', 'health']:
                    print(colors.fg.orange + 'Health: '+ colors.fg.green + str(cChar.health))
                    print(colors.reset, end='')
                elif splitIn[1].lower() in ['lvl', 'level']:
                    print(colors.fg.orange + 'Level: '+ colors.fg.purple + str(cChar.level))
                    print(colors.reset, end='')
                elif splitIn[1].lower() in ['exp', 'xp', 'experience']:
                    print(colors.fg.orange + "Exp: ["+ colors.fg.purple + str(cChar.exp) + colors.reset + " / " + colors.fg.purple + str(cChar.exp + cChar.expneed) + colors.reset + "]")
                    print(colors.reset, end='')
                elif splitIn[1] in npcL:
                    print(npc.loadNpc(splitIn[1], "mob").description)
                else:
                    print("There is no "+ splitIn[1] + " here.")

        #========= take [object] ==========#

        elif command in ["take", "grab", "borrow"]:
            if len(splitIn) == 1:
                print("You grab in to the void.. You now own.. nothing.")
            else:
                if splitIn[1] in cRoom.inventory:
                    print(cRoom.inventory[splitIn[1]] + "\n You acquired " + splitIn[1])
                    cChar.inventory[splitIn[1]] = cRoom.inventory[splitIn[1]]
                    # cRoom.inventory.pop(splitIn[1])

                else:
                    print("There is no such thing here, " + random.choice(["weirdo", "nutter", "whippersnapper", "beavus", "butthead", "you Thraal", "whacko"]) + ".")

        #========= Map ==========#

        elif command in ["map", "where", "picture"]:
            print(colors.invisible)
            os.system("clear")
            print(colors.reset)
            mapL = []
            for o in roomL:
                oCoord = o[4:]
                x = oCoord.split("_")[0]
                y = oCoord.split("_")[1]
                mapL.append((int(x),int(y)))
            if cChar.achievements["map"] == True:
                bigY = max(mapL,key=operator.itemgetter(1))[1]
                bigX = max(mapL,key=operator.itemgetter(0))[0]
                litY = min(mapL,key=operator.itemgetter(1))[1]
                litX = min(mapL,key=operator.itemgetter(0))[0]
            else:
                bigX = cChar.location[0] + 1
                litX = cChar.location[0] - 1
                bigY = cChar.location[1] + 1
                litY = cChar.location[1] - 1
            mapper(litX, bigX, litY, bigY, mapL)

        #========= Admin part ==========#

        elif command == "admin":
            uName = input("Admin username: " + colors.invisible)
            print(colors.reset , end = '')
            pwd = input("Admin Password: " + colors.invisible)
            print(colors.reset , end = '')
            if (uName == "42") and (pwd == "42"):
                print("Username and Password correct. (\"quit\" to exit)")
                print("Commands are: room, mob, map, quit, item, add, crown <username>")
                while True:
                    try:
                        admIn = input(colors.fg.red + ">> " + colors.fg.pink)
                        print(colors.reset , end = '')
                        commAdmin = ""
                        splitMin = admIn.split(" ")
                        for w in splitMin:
                            w = w.lower()
                        commAdmin = splitMin[0]

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

                        elif commAdmin == "item":
                            kind = input("weapon, armor or shield: ")
                            if kind == "weapon":
                                item.newWeapon()
                            elif kind == "shield":
                                item.newShield()
                            elif kind == "armor":
                                item.newArmor()

                        elif commAdmin == "add":
                            kind = input("weapon, armor or shield: ")
                            if kind == "weapon":
                                kind = 'wpn'
                            elif kind == "shield":
                                kind = 'shd'
                            elif kind == "armor":
                                kind = 'arm'
                            print('Input the name of the item')
                            name = input('>')
                            cChar.inventory[item] = item.loadItem(name, kind)
                            print()
                            print(cChar.inventory)

                        elif commAdmin == "crown":
                            cPlayer.admin = True
                            cPlayer.save()
                            if cPlayer.admin:
                                print("Player " + cPlayer.username + " is now admin.")

                        elif commAdmin == "quit":
                            print()
                            print("Returning to game...")
                            print()
                            break
                        else:
                            print("Possible commands are \"room\", \"mob\", \"map\", \"item\" and \"quit\".")

                    except Exception as e:
                        print(e)
                        print("Weeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee... Samfing diiidn't wörk.")

            else:
                print("Username or password incorrect.")

        elif command in ["smite", "punish", "execute", "behead"]:
            if cPlayer.admin == True:
                if len(splitIn) > 1:
                    if (splitIn[1][0].upper() + splitIn[1][1:]) in npcL:
                        attackMob = npc.loadNpc((splitIn[1][0].upper() + splitIn[1][1:]), "mob")
                        print(colors.invisible)
                        os.system("clear")
                        print(colors.reset)
                        print("Omae Wa Mu Shindeiru !!!")
                        time.sleep(1)
                        loser = attack.smite(cChar, attackMob)
                        if loser == "mob":
                            newMob = npc.newMob()
                            npcL = npc.loadNpcs()
                            for c in npcL:
                                npc.loadNpc(c, "mob")
                    else:
                        print("Everyone is cowering in fear .... hoping not to be named")
                else:
                    print("Lightning descends from the sky, but no-one was chosen to be punished")
            else:
                print('as if that would work ...')

        #========= Quit Sequence ==========#

        elif command in ["quit", "leave", "abandon", "abort", "terminate", "exit"]:
            sureMaker = input("Are you sure you want to quit? (y/n)\n>" + colors.fg.cyan)
            print(colors.reset)
            if sureMaker == ("y" or "Y"):
                print("Quitting game...")
                cChar.save()
                cRoom.save()
                break
            else:
                print("Returning to the game...")

        #========= FizzBuzz =========#

        elif command == "fizz":
            print("buzz")

        #========= help [with commands] =========#

        elif command in ["help", "halp", "", "eehm", "?", "??", "???"]:
            if len(splitIn) == 1:
                print("Possible commands are: go, look, take, attack, map and quit (and help)")
            else:
                if splitIn[1] in helpText:
                    print()
                    print(helpText[splitIn[1]] + "\n")
                else:
                    print("There is no such command.")
            #at some point there should rather exist a dictionary of commands where the loop
            #checks if a command exists and then produces the outcome
            #then a list of commands can be automatically compiled and it would look cleaner

        #========= Attack ==========#
        #need to display remaining player HP after getting dmg
        elif command in ["attack", "strike", "kill", "engage", "challenge", 'fight']:
            if len(splitIn) > 1:
                if (splitIn[1][0].upper() + splitIn[1][1:]) in npcL:
                    attackMob = npc.loadNpc((splitIn[1][0].upper() + splitIn[1][1:]), "mob")
                    print(colors.invisible)
                    os.system("clear")
                    print(colors.reset)
                    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH!!!")
                    loser = attack.fight(cChar, attackMob)
                    if loser == "mob":
                        newMob = npc.newMob()
                        npcL = npc.loadNpcs()
                        for c in npcL:
                            npc.loadNpc(c, "mob")
                    elif loser == "char":
                        for c in cChar.inventory:
                            cRoom.inventory.append(c)
                        cChar.inventory = []
                        cRoom = loadCRoom()
                else:
                    print("You let loose a war-cry, incoherently screaming random names. Anyone present looks at you in confusion. No-one here seems to go by that name.")
            else:
                print("You shout, strike ... and land on the floor.")
                print("Your bloody nose tells you that there was no enemy to attack..")
        else:
            print(random.choice(["What the hell are you trying to say?", "STOP MUMBLING!", "Huh?", "Wut?"]), end='   ')
            print("(Write \"help\" for help. (Why else...))")
    except Exception as e:
        print(e)
        print("OOOPS!!! Either I or you made a mistake.")
