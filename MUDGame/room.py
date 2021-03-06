import os
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

class Room:
    def __init__(self, x, y):
        self.location = (x,y)
        self.possibleDirections = {}
        self.description = ''
        self.stuffDescription = {}
        self.inventory = {}
        return

    def save(self):
        try:
            f = open("../data/rooms/room"+ str(self.location[0]) + '_' + str(self.location[1]) + ".txt", "wb")
        except FileNotFoundError:
            print('Room file not found. Unable to save room.')
            print()
            return
        Pickler(f).dump(self)
        f.close()
        return

#-------------------------------------------------------------------------

def newRoom(x, y):
    room = Room(x, y)

    print("Add directions to be reached from this room: (q to stop)")
    while True:
        direction = input("> ")
        if direction == "q":
            break
        else:
            lead = input("Whereto: ")
            room.possibleDirections[direction] = lead

    room.description = input("Description: ")

    print("Add objects to be looked at in this room: (q to stop)")
    while True:
        obj = input("> ")
        if obj == "q":
            break
        else:
            descr = input("Description: ")
            room.stuffDescription[obj] = descr
            qst = input("Add it to inventory? (y/n)")
            if qst == "y":
                room.inventory[obj] = descr

    room.save()
    return loadRoom('room' + str(x) + '_' + str(y))

#-------------------------------------------------------------------------

def loadRooms():
    '''
    returns a list of all room objects
    '''
    roomL = []
    for fIterator in os.listdir("../data/rooms/"):
        roomL.append(fIterator[:-4]) # Unpickler(f).load())
    return roomL

def loadRoom(name):
    '''
    takes the room name,
    returns the room object
    '''
    try:
        f = open("../data/rooms/"+ name + ".txt", "rb")
    except FileNotFoundError:
        print('Room file not found. Unable to load object.')
        print()
        return
    room = Unpickler(f).load()
    f.close()
    return room
