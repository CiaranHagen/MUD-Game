import os
from pickle import Pickler
from pickle import Unpickler

class Room:
    def __init__(self, x, y):
        self.location = (x,y)
        self.possibleDirections = []
        self.description = ''
        self.stuffDescription = set()
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
