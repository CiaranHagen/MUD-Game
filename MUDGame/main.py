import character, room, npc, player, attack

def onstart():
    newPlayer = input("Register (r) or log in (l).")
    if newPlayer == "r":
        currentPlayer = player.newPlayer()
        print("------------------------------------------")
        print("Character creation \n")

        charactername = input("Character name: ")
        currentChar = character.newCharacter(charactername)

    else:
        currentPlayer = player.login()
        print ("------------------------------------------")
        newCharacter = input("Create new character (1) or use existsing character (2)? ")
        if newCharacter == "1":
            print("Character creation \n")

            charactername = input("Character name: ")
            currentChar = character.newCharacter(charactername)
        else:
            charactername = charactername = input("What character do you want to load? ")
            currentChar = character.loadCharacter(charactername)

    roomL = room.loadRooms()

    npcL = npc.loadNpcs()

    return currentPlayer, currentChar, roomL, npcL

def loadCRoom():
    roomName = "room" + str(cChar.location[0]) + "_" + str(cChar.location[1])
    cRoom = room.loadRoom(roomName)
    return cRoom




cPlayer, cChar, roomL, npcL = onstart()

cRoom = loadCRoom()



while True:
    try:
        inputter = input("> ")
        command = ""
        splitIn = inputter.split(" ")
        command = splitIn[0]

        #========= Go [direction] ==========#
        if command == "go":
            if splitIn[1] in cRoom.possibleDirections:
                character.move(splitIn[1])
                cRoom.save()
                cRoom = loadCRoom()
            else:
                print("You cannot go there.")
        #========= help [with commands] =========#
        if command == "help":
            print("Possible commands are: go, look and quit")
            #at some point there should rather exist a dictionary of commands where the loop
            #checks if a command exists and then produces the outcome
            #then a list of commands can be automatically compiled and it would look cleaner

        #========= Look [object] ==========#
        elif command == "look":
            if len(splitIn) == 1:
                print(cRoom.description)
            else:
                print(cRoom.stuffDescription[splitIn[1]])
        #========= Quit Sequence ==========#
        elif command == "quit":
            sureMaker = input("Are you sure you want to quit? (y/n)")
            if sureMaker == "y" or "Y":
                print("Quitting game...")
                cChar.save()
                cRoom.save()
                break
            else:
                print("Returning to the game...")
    except:
        print("OOOPS! Either you or I did a mistake ^^")
    #========= Attack ==========#
