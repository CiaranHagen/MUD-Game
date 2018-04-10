import character, npc, player, attack, os, operator, random, item, race, time

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


def chooseRace(currentPlayer):
    raceList = ['orc', 'dwarf', 'elf', 'troll', 'succubus', 'gelfling', 'gockcobbler', 'shinigami', 'hickdead', 'thraal']
    if currentPlayer.admin == False:
        while True:
            charRace = input("What is your race?\nYou can choose from: " + colors.fg.cyan + "orc, dwarf, elf, troll, succubus, gelfling, gockcobbler, shinigami and hickdead" + colors.reset + ".\n> " + colors.fg.cyan)
            print(colors.reset , end = '')
            if charRace in raceList:
                break
            else:
                print("This race is not known to me.. Try again.")
    elif currentPlayer.admin == True:
        answer = ''
        while not answer in ['yes', 'y']:
            charRace = input("What is your race?\nYou can choose from: " + colors.fg.cyan + "orc, dwarf, elf, troll, succubus, gelfling, gockcobbler, shinigami and hickdead" + colors.fg.purple + " or something else entirely " + colors.reset + ".\n> " + colors.fg.cyan)
            print(colors.reset , end = '')
            if not charRace == '':
                if answer in ['no', 'n']:
                    answer = ''
                while not answer in ['yes', 'y','no', 'n']:
                    print('Are you sure you want to have: '+ colors.fg.cyan + str(charRace) + colors.reset, end = '' + ' as your race ?\n')
                    print("["+ colors.fg.green + "yes" + colors.reset + "/" + colors.fg.red + "no" + colors.reset + "]" + colors.fg.cyan)
                    answer = input('>').lower()
                    print(colors.reset , end = '')
                    if answer in ['yes', 'y', 'no', 'n']:
                        continue
                    else:
                        print('This is not a valid input, try again ...\n')
    return charRace
