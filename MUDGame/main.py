import character, room, npc, player, attack, os, operator, random

class colors:
    '''Colors class:reset all colors with colors.reset; two
    sub classes fg for foreground
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


def onstart():
    newPlayer = input("Register (r) or log in (l)." + colors.fg.orange)
    print(colors.reset , end = '')

    if newPlayer == "r":
        currentPlayer = player.newPlayer()
        print("------------------------------------------".center(os.get_terminal_size().columns, "-"))
        print("Character creation \n")

        charactername = input("Character name: " + colors.fg.orange)
        print(colors.reset , end = '')
        currentChar = character.newCharacter(charactername, currentPlayer.username)
        print("After you spend almost an eternity in the great nothingness, also called aether, you see an open door and step through... (enter to continue)".center(os.get_terminal_size().columns, " "))
        wait = input()

    else:
        currentPlayer = player.login()
        print ("------------------------------------------".center(os.get_terminal_size().columns, "-"))
        newCharacter = input("Create new character (1) or use existing character (2)? " + colors.fg.orange) #or show list of characters?
        print(colors.reset , end = '')
        if newCharacter == "1":
            print("Character creation \n")

            charactername = input("Character name: " + colors.fg.orange)
            print(colors.reset , end = '')
            currentChar = character.newCharacter(charactername, currentPlayer.username)
            print("After you spend almost an eternity in the great nothingness, also called aether, you see an open door and step through... (enter to continue)".center(os.get_terminal_size().columns, " "))
            wait = input()
        else:
            charactername = charactername = input("What character do you want to load? " + colors.fg.orange)
            print(colors.reset , end = '')
            currentChar = character.loadCharacter(charactername, currentPlayer.username)
            if currentChar == "new":
                print("Character creation \n")

                charactername = input("Character name: " + colors.fg.orange)
                print(colors.reset , end = '')
                currentChar = character.newCharacter(charactername, currentPlayer.username)
                print("After you spend almost an eternity in the great nothingness, also called aether, you see an open door and step through... (enter to continue)".center(os.get_terminal_size().columns, " "))
                wait = input()

    roomL = room.loadRooms()

    npcL = npc.loadNpcs()

    return currentPlayer, currentChar, roomL, npcL

def loadCRoom():
    roomName = "room" + str(cChar.location[0]) + "_" + str(cChar.location[1])
    cRoom = room.loadRoom(roomName)
    return cRoom



os.system("clear")
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

helpText = {"go" : "go <direction>", "look" : "look <object (optional)>", "take" : "take <object>", "quit" : "Write this if you think you have better things to do...", "help" : "Seriously? I mean ...", "attack" : "attack <attackable npc>"}

os.system("clear")
print()
print(("----- Welcome " + cPlayer.username + "! -----").center(os.get_terminal_size().columns, " "))
print()

while True:
    try:
        inputter = input(colors.fg.red + "> " + colors.fg.orange)
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
                    cChar.move(splitIn[1])
                    cRoom.save()
                    cRoom = loadCRoom()
                    print("You go " + splitIn[1] + ".")
                    
                    # ------- Move mobs -------- #
                    
                    for c in npcL:
                        mobber = npc.loadNpc(c, "mob")
                        mobber.move()
                    for c in npcL:
                        npc.loadNpc(c, "mob")
                     # -------------------------- #   
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

        elif command in ["look", "watch", "observe", "see", "eye", "regard"]:
            if len(splitIn) == 1:
                print(cRoom.description)
                print("Also present: ", end="")
                for c in npcL:
                    if (npc.loadNpc(c, "mob").location[0] == cRoom.location[0]) and (npc.loadNpc(c, "mob").location[1] == cRoom.location[1]):
                        print(npc.loadNpc(c, "mob").name , end=" ")
                print()
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
                else:
                    print("There is no "+ splitIn[1] + " here.")

        #========= take [object] ==========#

        elif command in ["take", "grab", "borrow"]:
            if len(splitIn) == 1:
                print("You grab in to the void.. You own now.. nothing.")
            else:
                if splitIn[1] in cRoom.inventory:
                    print(cRoom.inventory[splitIn[1]] + "\n You acquired " + splitIn[1])
                    cChar.inventory[splitIn[1]] = cRoom.inventory[splitIn[1]]
                    cRoom.inventory.pop(splitIn[1])

                else:
                    print("There is no such thing here weirdo.")

        #========= Map ==========#

        elif command in ["map", "where", "picture"]:
            os.system("clear")
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
            drawL = []
            for j in range(litY, bigY+1):
                drawL.append([])
                for i in range(litX, bigX+1):
                    if (i,j) in mapL:
                        drawL[j].append("O")
                    else:
                        drawL[j].append(" ")
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
                    print(drawL[j][i], end='')
                    if drawL[j][i] == "O":       
                        if "east" in room.loadRoom("room" + str(i) + "_" + str(j)).possibleDirections.values():
                            print(colors.fg.cyan + "-", end='')
                        else:
                            print(" ", end='')
                    else:
                        print(" ", end='')
                    
                    if drawL[j][i] == "O":       
                        if "south" in room.loadRoom("room" + str(i) + "_" + str(j)).possibleDirections.values():
                            spaceLine += "| "
                        else:
                            spaceLine += "  "
                    else:
                        spaceLine += "  "

                print("", end="\n")
                print(spaceLine)
            print(colors.reset , end = '')
            print(dis*"=" + " MAP " + dis*"=")
            print()        
            
        
        #========= Admin part ==========#
        
        elif command == "admin":
            uName = input("Admin username: " + colors.invisible)
            print(colors.reset , end = '')
            pwd = input("Admin Password: " + colors.invisible)
            print(colors.reset , end = '')
            if (uName == "42") and (pwd == "42"):
                print("Username and Password correct. (\"quit\" to exit)")
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
                            coord = input("Please enter the coordinates: ")
                            room.newRoom(int(coord.split(' ')[0]), int(coord.split(' ')[1]))
                            roomL = room.loadRooms()
                        elif commAdmin == "mob":
                            print("Creating new mob...")
                            npc.newMob()
                        elif commAdmin == "quit":
                            print()
                            print("Returning to game...")
                            print()
                            break
                        else:
                            print("Possible commands are \"room\", \"mob\" and \"quit\".")
                    except:
                        print("Weeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee... Samfing diiidn't wörk.") 
            else:
                print("Username or password incorrect.")
                        

        #========= Quit Sequence ==========#

        elif command in ["quit", "leave", "abandon", "abort", "terminate"]:
            sureMaker = input("Are you sure you want to quit? (y/n)" + colors.fg.orange)
            print(colors.reset)
            if sureMaker == ("y" or "Y"):
                print("Quitting game...")
                cChar.save()
                cRoom.save()
                break
            else:
                print("Returning to the game...")

        #========= help [with commands] =========#

        elif command in ["help", "halp", "", "eehm", "?", "??", "???"]:
            if len(splitIn) == 1:
                print("Possible commands are: go, look, take, attack and quit")
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

        elif command in ["attack", "strike", "kill", "engage", "challenge"]:
            if len(splitIn) > 1:
                if splitIn[1] in npcL:
                    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH!!!")
                    loser = attack.fight(cChar, splitIn[1])
                    if loser == "mob":
                        newMob = npc.newMob()
                        npcL = npc.loadNpcs()
                        for c in npcL:
                            npc.loadNpc(c, "mob")
                else:
                    print("You let loose a war-cry, incoherently screaming random names. Anyone present looks at you in confusion. No-one here seems to go by that name.")
            else:
                print("You shout, strike ... and land on the floor.")
                print("Your bloody nose tells you that there was no enemy to attack..")

    except Exception as e: 
        print(e)
        print("OOOPS!!! Either I or you made a mistake.")
