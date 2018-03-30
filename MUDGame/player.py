import os
from pickle import Pickler
from pickle import Unpickler

class Player:
    def __init__(self, name, pw):
        self.username = name
        self.admin = False
        self.passwd = pw

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
    print()
    authenticate = False
    if authenticate == False:
        username = input("Username: " + colors.fg.orange)
        print(colors.reset , end = '')
        usernameL = []
        for fIterator in os.listdir("../data/players/"):
            usernameL.append(fIterator[:-4])

        if username in usernameL:
            player = loadPlayer(username)
            password = ""
            passwd = player.passwd
            while password != passwd:
                password = input("Password: " + colors.invisible)
                print(colors.reset , end = '')
                if password == passwd:
                    authenticate = True
                    return loadPlayer(username)
                elif password == "q":
                    return login()
                else:
                    print("Wrong password. Please try again. (q to abort)")
                    continue
        else:
            print("That user doesn't seem to exist. Please try again.")
            return login()
    else:
        print("You are already logged in...")


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
