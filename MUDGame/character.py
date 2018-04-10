import os, room, time, job, race
from pickle import Pickler
from pickle import Unpickler

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

class Character:
    def __init__(self, name):
        self.name = name
        self.race = ''
        self.job = ''
        self.inventory = {}
        self.onPerson = {'weapon':"default", 'shield':"default", 'armor':"default", 'bag':'default'}
        self.characterSkin = "default"
        self.location = [0,0]
        self.level = 0
#Character level follows: [lvl / Exp to next lvl / Total Exp] // [1 / 200 / 200] // [2 / 1600 / 1800] // [3 / 4200 / 6000] // [4 / 8000 / 14000] // [5 / 13000 / 27000]
        self.player = ''
        self.achievements = {"map":False}
        self.health = 0
        self.maxhealth = 0
        self.stats = {'wit' : 0, 'strength': 0, 'agility': 0, 'luck': 0}
        self.exp = 0
        self.expneed = ((200 * (1 + self.level * 3) * (1 + self.level)) - self.exp)
        return

    def addStatVal(self, key, value):
        self.stats[key] += value
        return

    def addItem(self, item, descr):
        self.inventory[item] = descr
        return

    def changeOnPerson(self, key, value):
        self.onPerson[key] = value
        return

    def move(self, direction):
        cRoomName = 'room' + str(self.location[0]) + '_' + str(self.location[1])
        cRoom = room.loadRoom(cRoomName)
        if direction in cRoom.possibleDirections:
            direction = cRoom.possibleDirections[direction]
            if direction == ('north' or 'n'):
                self.location = [self.location[0], self.location[1] + 1]
            elif direction == ('south' or 's'):
                self.location = [self.location[0], self.location[1] - 1]
            elif direction == ('east' or 'e'):
                self.location = [self.location[0] + 1, self.location[1]]
            elif direction == ('west' or 'w'):
                self.location = [self.location[0] - 1, self.location[1]]
            elif direction == 'northwest':
                self.location = [self.location[0] - 1, self.location[1] + 1]
            elif direction == 'southwest':
                self.location = [self.location[0] - 1, self.location[1] - 1]
            elif direction == 'northeast':
                self.location = [self.location[0] + 1, self.location[1] + 1]
            elif direction == 'southeast':
                self.location = [self.location[0] + 1, self.location[1] - 1]
            elif direction == "":
                return
            else:
                print("The creators of this game have f***** up and entered a non-existent actual direction. Go complain...")
        return

    def save(self):

        try:
            f = open("../data/characters/"+ self.name + ".txt", "wb")
        except FileNotFoundError:
            print('Character file not found. Unable to save progress.')
            print()
            return
        Pickler(f).dump(self)
        f.close()
        return

#-------------------------------------------------------------------------

def newCharacter(name, cPlayerName, Race, Job, Stats, Health):
    character = Character(name)
    character.player = cPlayerName
    character.race = Race
    character.job = Job
    character.stats = Stats
    character.health = Health
    character.maxhealth = Health
    character.save()
    return loadCharacter(name, cPlayerName)

#-------------------------------------------------------------------------

def loadCharacter(name, cPlayerName):
    '''
    takes the character name,
    returns the character object
    '''
    try:
        f = open("../data/characters/"+ name + ".txt", "rb")
    except FileNotFoundError:
        print("Character file not found. Unable to load progress. \n")
        name = input("Please enter a valid character name (if you want to create a new character, type \"new\"): \n")
        if name == "new":
            return "new"
        else:
            return loadCharacter(name, cPlayerName)

    character = Unpickler(f).load()
    if character.player == cPlayerName:
        f.close()
        return character
    else:
        print("Character does not belong to you. Please choose one of your own characters.")
        f.close
        name = input("Please enter a valid character name (if you want to create a new character, type \"new\"): \n")
        if name == "new":
            return "new"
        else:
            return loadCharacter(name, cPlayerName)
def characterOwn(name, cPlayername):
    try:
        f = open("../data/characters/"+ name + ".txt", "rb")
    except FileNotFoundError:
        print("Character file not found. Unable to load progress. \n")
    character = Unpickler(f).load()
    if character.player == cPlayername:
        f.close()
        return True
    else:
        print("Character does not belong to you. Please choose one of your own characters.")
        f.close
        return False


def checkLevel(char):
    if not char.level == 0:
        if char.exp >= char.expneed:
            char.exp -= char.expneed
            if char.exp < 0:
                char.exp = 0
            char.level += 1
            char.expneed = ((200 * (1 + char.level * 3) * (1 + char.level)))

def makeChar(charL, currentPlayer):
    print("------------------------------------------".center(os.get_terminal_size().columns, "-"))
    print("Character creation \n")
    while True:
        charactername = input("Character name: " + colors.fg.cyan)
        if charactername in charL:
            if characterOwn(charactername, currentPlayer.username):
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
        print(currentPlayer.admin)
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
        charHealth = int(job.jobHealth(charJob))

        print()
        print(colors.fg.orange + 'Name: '+ colors.fg.cyan + str(charactername))
        print(colors.fg.orange + 'Race: ' + colors.fg.cyan + str(charRace))
        print(colors.fg.orange + 'Job: '+ colors.fg.cyan + str(charJob))
        print(colors.fg.orange + 'Stats: '+ colors.fg.purple + str(charStats))
        print(colors.fg.orange + 'Health: '+ colors.fg.green + str(charHealth))
        break

    print(colors.reset , end = '')
    currentChar = newCharacter(charactername, currentPlayer.username, charRace, charJob, charStats, charHealth)
    print("After you spend almost an eternity in the great nothingness, also called aether, you see an open door and step through... (enter to continue)".center(os.get_terminal_size().columns, " "))
    wait = input()
    return currentChar
