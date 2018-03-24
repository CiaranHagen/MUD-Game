import os, room
from pickle import Pickler
from pickle import Unpickler

class Character:
    def __init__(self, name, race, job, player, wit, strength, agility, luck):
        self.name = name
        self.race = race
        self.job = job
        self.inventory = {"map": 0}
        self.onPerson = {'weapon':"default", 'shield':"default", 'armor':"default", 'bag':'default', 'skin':'default'}
        self.location = [0,0]
        self.level = 0
        self.player = player
        self.health = 500
        self.stats = {'wit' : wit, 'strength': strength, 'agility': agility, 'luck': luck}
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
                self.location = (self.location[0], self.location[1] + 1)
            elif direction == ('south' or 's'):
                self.location = (self.location[0], self.location[1] - 1)
            elif direction == ('east' or 'e'):
                self.location = (self.location[0] + 1, self.location[1])
            elif direction == ('west' or 'w'):
                self.location = (self.location[0] - 1, self.location[1])
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

def newCharacter(player):
    raceList = ['orc', 'dwarf', 'elf', 'troll', 'succubus', 'gelfling', 'gockcobbler', 'shinigami', 'hickdead', 'thraal']
    jobList = {'warrior': "Warriors are a heavy class known for their strength and proficiency with swords & shields\n\n You get a bonus of " + '\033[46m' + '+5 on strength' + '\033[0m' + ', proficiency with swords & shields \nand bonus on any armor but you loose out on ' + '\033[31m' + '1 wit and 1 agility' + '\033[0m' , 'rogue':"rogues are a nimble class known for their agility and proficiency with daggers\n\nyou get a bonus of " + '\033[46m' + "+3 on agility" + '\033[0m' + ", proficiency with daggers \nand bonus on light armor",  'beggar': 'beggars are beggars, nothing special .... what did you expect ?\nyou get a non-existant bonus of +999 on everything,\nproficiency in begging and an additional amount of self-pity'}
    charRace = ''
    charJob = ''
    wit = 0
    strength = 0
    agility = 0
    luck = 0

    while True:
        charactername = input("Character name: " + '\033[33m')
        print('\033[0m' , end = '')

        while charactername == '':
            print("Only I am the one without name!!")
            charactername = input("Character name: \n> " + '\033[33m')
            print('\033[0m' , end = '')

        while True:
            charRace = input("What is your race?\nChoose from: orc, dwarf, elf, troll, succubus, gelfling, gockcobbler, shinigami and hickdead.\n> " + '\033[33m')
            print('\033[0m' , end = '')
            if charRace in raceList:
                break
            else:
                print("This race is not known to me.. Try again.")

        def choice(charJob):
            while True:
                print("Do you wish to choose " + '\033[46m' + str(charJob.upper()) + '\033[0m' + " as your class ? \n["
                      + '\033[32m' + "y" + '\033[0m' + "/" + '\033[31m' + "n" + '\033[0m' , end = ''  + "]")
                answer = input('> ' + '\033[33m').lower()
                print('\033[0m' , end = '')
                if answer == 'y':
                    return False
                if answer == 'n':
                    return True
                else:
                    print ("this is not a valid input, try again ... \n")
                    return choice(charJob)



        run = True
        while run:
            charJob = input("What class do you choose? \nYou can choose from: "+ (for key in jobList: key))
            print('\033[0m' , end = '')

            if charJob in jobList:
                print(jobList[charjob])
            else:
                print("This class is not known to me.. Try again.\n")
        while True:
            print("Set the stats of your character. 4 different stats, 10 points to give, you know the drill.")
            strength = input("How " + '\033[46m' + "strong " + '\033[0m' + "are you?: \n> "+ '\033[33m')
            print('\033[0m' , end = '')
            agility = input("How " + '\033[46m' + "agile " + '\033[0m' + "are you?: \n> "+ '\033[33m')
            print('\033[0m' , end = '')
            wit = input("How would you rate your " + '\033[46m' + "intelligence" + '\033[0m' + "?: \n> "+ '\033[33m')
            print('\033[0m' , end = '')
            luck = input("Are you feeling " + '\033[46m' + "lucky" + '\033[0m' + "?: \n> "+ '\033[33m')
            print('\033[0m' , end = '')
            try:
                if (int(strength)+int(agility)+int(wit)+int(luck)) == 10:
                    if int(strength) > 4 or int(agility)>4 or int(wit)>4 or int(luck)>4:
                        print("What the hell should this be? Well, I don't really care...")
                    if int(wit) < 3:
                        print("Go and have fun in the dungeons you dumdum, I bet you will have at least one peer down there.")
                    else:
                        print("Ok, that looks pretty solid. Have fun...")
                    break
                else:
                    print("Do you even math?")
            except:
                print("Very clever... C'mon, I need numbers dude! N U M B E R S!")
        print('\033[0m' , end = '')
        char = Character(charactername, charRace, charJob, player, wit, strength, agility, luck)
        char.save()
        if char.job == 'warrior':
            char.stats['strength'] = int(strength)+5
            char.stats['agility'] = int(agility)-1
            char.stats['wit'] = int(wit)-1
            char.stats['luck'] = int(luck)
        if char.job == 'rogue':
            char.stats['strength'] = int(strength)
            char.stats['agility'] = int(agility)+3
            char.stats['wit'] = int(wit)+1
            char.stats['luck'] = int(luck)+1
        if char.job == 'beggar':
            char.stats['strength'] = int(strength)
            char.stats['agility'] = int(agility)
            char.stats['wit'] = int(wit)+2
            char.stats['luck'] = int(luck)+2
        print()
        print('\033[33m' + 'Name: '+ '\033[46m' + str(charactername))
        print('\033[33m' + 'Race: ' + '\033[46m' + str(charRace))
        print('\033[33m' + 'Job: '+ '\033[46m' + str(charJob))
        print('\033[33m' + 'Stats: '+ '\033[32m' + str(char.stats))
        break

    print('\033[0m' , end = '')
    char.save()
    return char.name

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
