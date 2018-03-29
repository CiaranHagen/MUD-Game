import os, room, time
from pickle import Pickler
from pickle import Unpickler

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
def characterOwn(name):
    try:
        f = open("../data/characters/"+ name + ".txt", "rb")
    except FileNotFoundError:
        print("Character file not found. Unable to load progress. \n")
    character = Unpickler(f).load()
    if character.player == cPlayerName:
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
