import os, string
from pickle import Pickler
from pickle import Unpickler
import random

class Npc:
    def __init__(self, name):
        self.race = ''
        self.name = name
        self.inventory = []
        self.location = [0,0]
        self.level = 0
        return

    def move(self, direction):
        exec('possibleDirections = ' + 'room' + str(self.location[0]) + '_' + str(self.location[1]) + '.possibleDirections')
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
            f = open("../data/npcs/"+ self.name + ".txt", "wb")
        except FileNotFoundError:
            print('NPC file not found. Unable to save progress.')
            print()
            return
        Pickler(f).dump(self)
        f.close()
        return

#------------------------------------------------------------------------------

class Mob(Npc):
    def __init__(self, name):
        Npc.__init__(self, name)
        return

    def attack():
        print('AAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHH...')

    def save(self):
        try:
            f = open("../data/npcs/mob_"+ self.name + ".txt", "wb")
        except FileNotFoundError:
            print('NPC file not found. Unable to save progress.')
            print()
            return
        Pickler(f).dump(self)
        f.close()
        return



#------------------------------------------------------------------------------

def newMob():
    races = ['orc', 'dwarf', 'elf']
    name = ''
    race = random.choice(races)
    letters = string.ascii_uppercase
    ranLen = 3 + random.randint(0, 6)
    for i in range(0, ranLen):
        name += letters[random.randint(0, 25)]
    mob = Mob(name)
    mob.race = race
    roomCoord = random.choice(os.listdir('../data/rooms/'))[4:-4]
    mob.location = [int(roomCoord[: len(roomCoord)//2]), int(roomCoord[(len(roomCoord)//2) + 1 :])]
    mob.level = random.randint(0, 5)
    mob.save()
    return loadNpc(name, "mob")

#------------------------------------------------------------------------------

def move(self, direction):
        exec('possibleDirections = ' + 'room' + str(self.location[0]) + '_' + str(self.location[1]) + '.possibleDirections')
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

def loadNpcs():
    '''
    returns all npc objects
    '''
    npcL = []
    for fIterator in os.listdir("../data/npcs/"):
        npcL.append(fIterator[4:-4])
    return npcL

def loadNpc(name, kind):
    '''
    takes the npc name and kind,
    returns the npc object
    '''
    try:
        f = open("../data/npcs/" + kind + "_" + name + ".txt", "rb")
    except FileNotFoundError:
        print("NPC file not found. Unable to load progress. \n")
        print("Please enter a valid NPC name or kind.")
        loadNpc(name, kind)
    npc = Unpickler(f).load()
    f.close()
    return npc
