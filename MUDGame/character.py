import os, room
from pickle import Pickler
from pickle import Unpickler

class Character:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.onPerson = {'sword':"default", 'shield':"default", 'armor':"default", 'bag':"default"}
        self.characterSkin = "default"
        self.location = (0,0)
        self.level = 0
        return

    def addItem(self, itemName):
        self.inventory.append(itemName)
        return

    def changeOnPerson(self, key, value):
        self.onPerson[key] = value
        return

    def move(self, direction):
        cRoomName = 'room' + str(self.location[0]) + '_' + str(self.location[1])
        cRoom = room.loadRoom(cRoomName)
        possibleDirections = cRoom.possibleDirections
        if direction in possibleDirections:
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

def newCharacter(name):
    character = Character(name)
    character.save()
    return loadCharacter(name)

#-------------------------------------------------------------------------

def loadCharacter(name):
    '''
    takes the character name,
    returns the character object
    '''
    try:
        f = open("../data/characters/"+ name + ".txt", "rb")
    except FileNotFoundError:
        print("Character file not found. Unable to load progress. \n")
        print("Please enter a valid character name.")
        loadCharacter(name)
    player = Unpickler(f).load()
    f.close()
    return player
