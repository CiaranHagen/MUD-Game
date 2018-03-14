import os, random, string
from pickle import Pickler
from pickle import Unpickler

class Npc:
    def __init__(self, name):
        self.race = ''
        self.name = name
        self.inventory = []
        self.location = (0,0)
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
            f = open("../npcs/"+ self.name + ".txt", "wb")
        except FileNotFoundError:
            print('NPC file not found. Unable to save progress.')
            print()
            return
        Pickler(f).dump(self)
        f.close()
        return

#------------------------------------------------------------------------------

class Mob(Npc):
    def __init__(self):
        Npc.__init__(self)
        return

    def attack():
        print('AAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHH...')

    def save(self):
        try:
            f = open("../npcs/mob_"+ self.name + ".txt", "wb")
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
    letters = string.ascii_uppercase.split()
    for i in random(3, 8):
        name += random.choice(letters)
    mob = Mob()
    mob.race = race
    mob.name = name
    roomCoord = random.choice(os.listdir('../rooms/'))[4,]
    mob.location = (int(roomCoord[0, len(roomCoord)%2 - 1]), int(roomCoord[len(roomCoord)%2, ]))
    mob.level = random(5)

    mob.save()
    return loadNpc(name)

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
    returns aall npc objects
    '''
    npcL = []
    for fIterator in os.listdir("../npcs/"):
        try:
            f = open("../npcs/" + fIterator, "rb")
        except FileNotFoundError:
            print('Room folder for ' + fIterator + ' not found. Unable to load rooms.')
            print()
            return

        npcL.append(Unpickler(f).load())

        f.close()
    return npcL

def loadNpc(name, kind):
    '''
    takes the npc name and kind,
    returns the npc object
    '''
    try:
        f = open("../npcs/" + kind + "_" + name + ".txt", "rb")
    except FileNotFoundError:
        print("NPC file not found. Unable to load progress. \n")
        print("Please enter a valid NPC name or kind.")
        loadNpc(name, kind)
    npc = Unpickler(f).load()
    f.close()
    return npc
