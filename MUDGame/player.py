import os
from pickle import Pickler
from pickle import Unpickler

class Player:
    def __init__(self):
        self.username = input("Please enter your desired username: ")
        self.setPw()

    def setPw(self):
        pw = input("Please enter a password: ")
        pwCheck = input("Please enter the password again: ")
        if pw == pwCheck:
            self.passwd = pw
        else:
            print("Passwords don't match. Please try again...")
            print()
            setPw()

    def save(self):
        try:
            f = open("../data/players/"+ self.username + ".txt", "wb")
        except FileNotFoundError:
            print('Player file not found. Unable to save progress.')
            print()
            return
        Pickler(f).dump(self)
        f.close()
        return

#-------------------------------------------------------------------------

def login():
    authenticate = False
    if authenticate == False:
        username = input("Username: ")
        usernameL = []
        for fIterator in os.listdir("../data/players/"):
            usernameL.append(fIterator[:-4])

        if username in usernameL:
            player = loadPlayer(username)
            password = ""
            passwd = player.passwd
            while password != passwd:
                password = input("Password: ")
                if password == passwd:
                    authenticate = True
                    return loadPlayer(username)
                else:
                    print("Wrong password. Please try again.")
                    continue
        else:
            print("That user doesn't seem to exist. Please try again.")
            login()
    else:
        print("You are already logged in...")


def newPlayer():
    player = Player()
    username = player.username
    player.save()
    return loadPlayer(username)

#-------------------------------------------------------------------------

def loadPlayer(username):
    '''
    takes the character name,
    returns the character object
    '''
    try:
        f = open("../data/players/"+ username + ".txt", "rb")
    except FileNotFoundError:
        print('Player file not found. Unable to load progress.')
        print()
        return
    player = Unpickler(f).load()
    f.close()
    return player
