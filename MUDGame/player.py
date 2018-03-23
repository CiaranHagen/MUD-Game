import os
from pickle import Pickler
from pickle import Unpickler

class Player:
    def __init__(self):
        self.username = input("Please enter your desired username: " + colors.fg.orange)
        print(colors.reset , end = '')
        self.setPw()
        self.admin = False

    def setPw(self):
        pw = input("Please enter a password: " + colors.invisible)
        print(colors.reset , end = '')
        pwCheck = input("Please enter the password again: " + colors.invisible)
        print(colors.reset , end = '')
        if pw == pwCheck:
            self.passwd = pw
        else:
            print("Passwords don't match. Please try again...")
            print()
            setPw(self)

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

class colors:
    '''Colors class:reset all colors with colors.reset; two 
    sub classes fg for foreground 
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
