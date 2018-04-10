import character, room, npc, player, attack, os, operator, random, item, job, race, time, mapmod, look, go
from admin import adminer
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
        currentChar = character.makeChar(charL, currentPlayer)

    else:
        currentPlayer = player.login()
        print ("------------------------------------------".center(os.get_terminal_size().columns, "-"))
        newCharacter = input("Create new character (1) or use existing character (2)? " + colors.fg.cyan) #or show list of characters?
        print(colors.reset , end = '')
        if newCharacter == "1":
            currentChar = character.makeChar(charL, currentPlayer)
        else:
            charactername = input("Which character do you want to load? ")
            currentChar = character.loadCharacter(charactername, currentPlayer.username)
            if currentChar == "new":
                currentChar = character.makeChar(charL, currentPlayer)

    roomL = room.loadRooms()

    npcL = npc.loadNpcs()

    return currentPlayer, currentChar, roomL, npcL

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

helpText = {"go" : "go <direction>", "look" : "look <object (optional)>", "take" : "take <object>", "quit" : "Write this if you think you have better things to do...", "help" : "Seriously? I mean ...", "attack" : "attack <attackable npc>", "map":"Prints a map of your surroundings. If you have the map achievement, it prints the whole world map.", "wear":"wear <item name>"}

raceDescriptions = {"orc":"Orc. A brustish ugly humanoid being. Not nice.", "dwarf":"Dwarf. Short stockish and bad-tempered with a distinct lack of hygiene. Don't mess with his hammer.", "elf":"Elf. Gracefully and elegantly deadly. Easily offended.", "troll":"Troll. Big, indescribably ugly and as dumb as he is strong.", "succubus":"Succubus.", "gelfling":"Gelfling. Small humanoid being with a bald head and a weird accent.", "gockcobbler":"GockCobbler. Shinigami.", "hickdead":"Hickdead. Annoying with an a**h*** attitude.", "thraal":"Thraal. Even dumber than a troll. It believes that if you can't see it, it can't see you."}

print(colors.invisible)
os.system("clear")
print(colors.reset)

print()
print(("----- Welcome " + cPlayer.username + "! -----").center(os.get_terminal_size().columns, " "))
print()
if cPlayer.admin:
    print("You are logged in as admin. Remember that you are not limited to cardinal directions when moving. Just write \"go <x> <y>\". Also: The key to the magical admin-part of the game is the same as the username and they are both the answer to life the universe and everything. Vi?")
print()
print(("--------------" + len(cPlayer.username)*"-" + "-------").center(os.get_terminal_size().columns, " "))
commandL = ["help"]
while True:
    print()
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
        for i in range(0,len(splitIn)):
            splitIn[i] = splitIn[i].lower()
        command = splitIn[0]
        print()

        #========= Go [direction] ==========#

        if command in ["go", "walk", "move", "jump", "hop", "teleport", "translate", "commute"]:
            go.go(command,splitIn,cRoom,roomL,cChar,cPlayer,npcL)
            npcL = npc.loadNpcs()
            for c in npcL:
                npc.loadNpc(c, "mob")
            roomL = room.loadRooms()
            cChar = character.loadCharacter(cChar.name,cPlayer.username)
            loadCRoom()
        #========= Look [object] ==========#

        elif command in ["look", "watch", "observe", "see", "eye", "regard", "check"]:
            look.look(command,splitIn,npcL,cRoom,cChar,cPlayer)
        #========= take [object] ==========#

        elif command in ["take", "grab", "borrow"]:
            if len(splitIn) == 1:
                print("You grab in to the void.. You now own.. nothing.")
            else:
                if splitIn[1] in cRoom.inventory:
                    print(cRoom.inventory[splitIn[1]] + "\n You acquired " + splitIn[1])
                    cChar.inventory[splitIn[1]] = cRoom.inventory[splitIn[1]]
                else:
                    print("There is no such thing here, " + random.choice(["weirdo", "nutter", "whippersnapper", "beavus", "butthead", "you Thraal", "whacko"]) + ".")

        #========= wear ==========#

        elif command in ["wear", "don", "mount", 'equip']:
            if (len(splitIn) == 1) or ((len(splitIn) >1) and (splitIn[1] == " ")):
                print("You take off everything and stand naked in the middle of the room, wondering why. (Put your clothes back on!)")
            else:
                itemName = splitIn[1]
                if itemName in cChar.inventory:
                    for fIterator in os.listdir("../data/items/"):
                        if fIterator[4:-4] == itemName:
                            newItem = item.loadItem(itemName, fIterator[:3])
                            if fIterator[:3] == "wpn":
                                kind = "weapon"
                            elif fIterator[:3] == "arm":
                                kind = "armor"
                            elif fIterator[:3] == "shd":
                                kind = "shield"
                            oldItem = item.loadItem(cChar.onPerson[kind], fIterator[:3])
                            cChar.onPerson[kind] = newItem.name
                    if oldItem.name != "default":
                        cChar.inventory[oldItem.name] = oldItem.description
                    print("You put on " + newItem.name + " and take off " + oldItem.name + ".")
                else:
                    print("You either don't have this item or misssppeled its name or type.")

        #========= throw away ==========#

        elif command in ["trash", "rm", "discard"]:
            if len(splitIn) > 1:
                if splitIn[1] in cChar.inventory:
                    prompter = input("Are you sure you want to throw away this item (y/n)? ")
                    if prompter == "y":
                        cRoom.inventory[splitIn[1]] = cChar.inventory[splitIn[1]]
                        cChar.inventory.pop(splitIn[1])
                elif splitIn[1] in cChar.onPerson.values():
                    print("You need to put something else on before you take this off. Nudity is NOT an option!")
                else:
                    print("You can't throw away what you don't have. It's mine! Get it? MIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIINNNNNNNEEEEEEEEEEEEEEEEEEEE!!!")
            else:
                print("Well... ok that was productive... You threw away nothing?")

        #========= Map ==========#

        elif command in ["map", "where", "picture"]:
            mapL = []
            for o in roomL:
                oCoord = o[4:]
                x = oCoord.split("_")[0]
                y = oCoord.split("_")[1]
                mapL.append((int(x),int(y)))
            if (cChar.achievements["map"] == True) or cPlayer.admin:
                bigY = max(mapL,key=operator.itemgetter(1))[1]
                bigX = max(mapL,key=operator.itemgetter(0))[0]
                litY = min(mapL,key=operator.itemgetter(1))[1]
                litX = min(mapL,key=operator.itemgetter(0))[0]
            else:
                bigX = cChar.location[0] + 1
                litX = cChar.location[0] - 1
                bigY = cChar.location[1] + 1
                litY = cChar.location[1] - 1
            mapmod.mapper(litX, bigX, litY, bigY, mapL, cRoom)

        #========= Admin part ==========#

        elif command == "admin":
            uName = input("Admin username: " + colors.invisible)
            print(colors.reset , end = '')
            pwd = input("Admin Password: " + colors.invisible)
            print(colors.reset , end = '')
            if (uName == "42") and (pwd == "42"):
                print("Username and Password correct. (\"quit\" to exit)")
                print()
                adminer(cPlayer, cChar, cRoom, roomL)
            else:
                print("Username or password incorrect.")
            #reload all items, to make sure game is uptodate
            npcL = npc.loadNpcs()
            for c in npcL:
                npc.loadNpc(c, "mob")
            roomL = room.loadRooms()

        #========= Smite ==========#

        elif command in ["smite", "punish", "execute", "behead", 'kill']:
            if cPlayer.admin == True:
                if len(splitIn) > 1:
                    if (splitIn[1][0].upper() + splitIn[1][1:]) in npcL:
                        attackMob = npc.loadNpc((splitIn[1][0].upper() + splitIn[1][1:]), "mob")
                        print(colors.invisible)
                        os.system("clear")
                        print(colors.reset)
                        print("Omae Wa Mou Shindeiru !!!")
                        time.sleep(1)
                        print('NANI ? !!!!')
                        time.sleep(0.5)
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
                print("Omae Wa Mou Shindeiru !!!")
                time.sleep(0.5)
                print()
                print('Haha, nice try. As if that would work ...')

        #========= Quit Sequence ==========#

        elif command in ["quit", "leave", "abandon", "abort", "terminate", "exit"]:
            sureMaker = input("Are you sure you want to quit? (y/n)\n\n>" + colors.fg.cyan)
            print(colors.reset)
            if sureMaker == ("y" or "Y"):
                print("Quitting game...")
                cChar.save()
                cRoom.save()
                sys.exit()
            else:
                print("Returning to the game...")

        #========= FizzBuzz =========#

        elif command == "fizz":
            print("buzz")
        #========= Speeke Rattus Rattus =========#

        elif command in ["say", "speek", "speeke", 'speak', 'tell']:
            if len(splitIn) > 1:
                print(splitIn[1][0].upper() + splitIn[1][1:])
            else:
                print("Silence... my favorite kind of discussion.")

        #========= Speeke Rattus Rattus =========#

        elif command in ["yell", "scream", "holler"]:
            if len(splitIn) > 1:
                print(splitIn[1].upper())
            else:
                print(" - inhales... -")
                time.sleep(1)
                for i in range(0, 200):
                    print("A", end="")
                    time.sleep(0.01)
                    sys.stdout.flush()
                for i in range(0, 50):
                    print("H", end="")
                    time.sleep(0.01)
                    sys.stdout.flush()
                for i in range(0, 10):
                    print("!", end="")
                    time.sleep(0.01)
                    sys.stdout.flush()
                print("")
                print()
                time.sleep(1)
                print("Feel better?")
        #========= help [with commands] =========#

        elif command in ["help", "halp", "", "eehm", "?", "??", "???"]:
            if len(splitIn) == 1:
                print("Possible commands are: go, look, take, attack, map, wear, trash and quit (and help)")
            else:
                if splitIn[1] in helpText:
                    print(helpText[splitIn[1]])
                else:
                    print("There is no such command.")
            #at some point there should rather exist a dictionary of commands where the loop
            #checks if a command exists and then produces the outcome
            #then a list of commands can be automatically compiled and it would look cleaner

        #========= Attack ==========#
        #need to display remaining player HP after getting dmg
        elif command in ["attack", "strike", "engage", "challenge", 'fight']:
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
                        cRoom.inventory.update(cChar.inventory)
                        cChar.inventory = {}
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
