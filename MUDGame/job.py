import character, npc, player, attack, os, operator, random, item, time

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

def chooseJob(currentPlayer):

    jobList = ["warrior", "rogue", "beggar"]

    def choice(charJob):
        print("Do you wish to choose " + colors.fg.cyan + str(charJob.upper()) + colors.reset + " as your class ? \n["
                  + colors.fg.green + "y" + colors.reset + "/" + colors.fg.red + "n" + colors.reset , end = ''  + "]")
        answer = input('> ' + colors.fg.cyan).lower()
        print(colors.reset , end = '')
        if answer == 'y':
            print()
            print('congraz, you are now officialy a ' + colors.fg.cyan + str(charJob.upper()) + colors.reset)
            return str(charJob)
        if answer == 'n':
            return Job()
        else:
            print ("this is not a valid input, try again ... \n")
            return choice(charJob)
    def Job():
        if currentPlayer.admin == False:
            charJob = str(input("What class do you choose? \n"
                        "You can choose from:  "+ colors.fg.cyan +"{}\n> ".format(jobList)).lower())
            print(colors.reset , end = '')

            if charJob in jobList:
                if charJob == "warrior":
                    print('warriors are a heavy class known for their strength and proficiency with swords & shields\n')
                    print('you get a bonus of ' + colors.fg.cyan + '+5 on strength' + colors.reset , end = '' + ', proficiency with swords & shields and bonus on any armor')
                    print('but as a heavy skullmasher you have ' + colors.fg.red + '-1 wit and -1 agility' + colors.reset , end = '')
                    return choice(charJob)
                if charJob == "rogue":
                    print('rogues are a nimble class known for their agility and proficiency with daggers\n')
                    print('you get a bonus of ' + colors.fg.cyan + '+3 on agility ' + colors.reset , end = '' + ', proficiency with daggers and bonus on light armor')
                    return choice(charJob)
                if charJob == "beggar":
                    print('beggars are beggars, nothing special .... what did you expect ?\n')
                    print('you get a non-existant bonus of ' + colors.fg.orange + '+999' + colors.reset + ' on everything,\n'
                          'proficiency in begging and an additional amount of ' + colors.fg.orange + 'self-pity' + colors.reset , end = '')
                    return choice(charJob)
            else:
                print("This class is not known to me.. Try again.\n")
                return Job()
        return Job()
        if currentPlayer.admin == True:
            charJob = str(input("What class do you choose? \n"
                        "You can choose from:  "+ colors.fg.cyan +"{}" + colors.fg.purple + " or ADMIN (anything else is fine too)" "\n> ".format(jobList)).lower())
            print(colors.reset , end = '')
            if charJob == "ADMIN":
                print(colors.fg.purple + 'ADMINS are the ruler of all, the übermenschen')
                print('ADMIN gets an existant bonus of +666 on all stats ... is there any need to say more ?')
                return choice(charJob)
            if charJob == "warrior":
                print('warriors are a heavy class known for their strength and proficiency with swords & shields\n')
                print('you get a bonus of ' + colors.fg.cyan + '+5 on strength' + colors.reset , end = '' + ', proficiency with swords & shields and bonus on any armor')
                print('but as a heavy skullmasher you have ' + colors.fg.red + '-1 wit and -1 agility' + colors.reset , end = '')
                return choice(charJob)
            if charJob == "rogue":
                print('rogues are a nimble class known for their agility and proficiency with daggers\n')
                print('you get a bonus of ' + colors.fg.cyan + '+3 on agility ' + colors.reset , end = '' + ', proficiency with daggers and bonus on light armor')
                return choice(charJob)
            if charJob == "beggar":
                print('beggars are beggars, nothing special .... what did you expect ?\n')
                print('you get a non-existant bonus of ' + colors.fg.orange + '+999' + colors.reset + ' on everything,\n'
                    'proficiency in begging and an additional amount of ' + colors.fg.orange + 'self-pity' + colors.reset , end = '')
                return choice(charJob)
        return Job()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def jobStrength(charJob,strength):

    if charJob == "ADMIN":
        strength = int(strength)+666
        return str(strength)

    if charJob == 'warrior':
        strength = int(strength)+5
        return str(strength)

    if charJob == 'rogue':
        strength = int(strength)
        return str(strength)

    if charJob == 'beggar':
        strength = int(strength)
        return str(strength)

def jobAgility(charJob,agility):

    if charJob == "ADMIN":
        strength = int(agility)+666
        return str(agility)

    if charJob == 'warrior':
        agility = int(agility)-1
        return str(agility)

    if charJob == 'rogue':
        agility = int(agility)+3
        return str(agility)

    if charJob == 'beggar':
        agility = int(agility)
        return str(agility)

def jobWit(charJob,wit):

    if charJob == "ADMIN":
        strength = int(wit)+666
        return str(wit)

    if charJob == 'warrior':
        wit = int(wit)-1
        return str(wit)

    if charJob == 'rogue':
        wit = int(wit)+1
        return str(wit)

    if charJob == 'beggar':
        wit = int(wit)+2
        return str(wit)

def jobLuck(charJob,luck):

    if charJob == "ADMIN":
        strength = int(luck)+666
        return str(luck)

    if charJob == 'warrior':
        luck = int(luck)
        return str(luck)

    if charJob == 'rogue':
        luck = int(luck)+1
        return str(luck)

    if charJob == 'beggar':
        luck = int(luck)+2
        return str(luck)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def jobLevelUp(char):
    print('!!!!!!!!!!!!!!! TADAAAAAAAAAAA !!!!!!!!!!!')
    time.sleep(1)
    print()
    print('Congraz, you have gained a level !')
    time.sleep(1)
    print()
    print('Your '+ colors.fg.cyan + str(char.job) + colors.reset + ' is now level ' + colors.fg.cyan + str(char.level) + colors.reset, end='')
    time.sleep(1)
    print()
    if char.job == 'warrior' and char.level % 2 == 1:
        print('Your stats have improved !')
        print()
        char.stats['strength'] += 2
        char.health += 120
        print('you gained' + colors.fg.cyan + ' +2 strength' + colors.reset + ' / ' + colors.fg.cyan + '+120 health' + colors.reset, end='')
    elif char.job == 'warrior' and char.level % 2 == 0:
        print('Your stats have improved !')
        print()
        char.stats['strength'] += 2
        char.stats['agility'] += 1
        char.health += 120
        print('you gained' + colors.fg.cyan + ' +2 strength' + colors.reset + ' / ' + colors.fg.cyan + '+1 agility' + colors.reset + ' / ' + colors.fg.cyan + '+120 health' + colors.reset, end='')
    if char.job == 'rogue' and char.level % 2 == 0:
        print('Your stats have improved !')
        print()
        char.stats['agility'] += 2
        char.stats['strength'] += 1
        char.health += 75
        print('you gained' + colors.fg.cyan + ' +2 agility' + colors.reset + ' / ' + colors.fg.cyan + '+1 strength' + colors.reset + ' / ' + colors.fg.green + '+75 health' + colors.reset, end='')
    elif char.job == 'rogue' and char.level % 2 == 1:
        print('Your stats have improved !')
        print()
        char.stats['agility'] += 2
        char.health += 75
        print('you gained' + colors.fg.cyan + ' +2 agility' + colors.reset + ' / ' + colors.fg.cyan + '+75 health' + colors.reset, end='')
    if charJob == "ADMIN":
        print('You have become even more awesome and undying !')
        print()
        char.health += 666 * char.level
    print()
    time.sleep(1)
    print(colors.fg.cyan + str(char.stats) + colors.reset, end='' )
    print(colors.fg.cyan + 'Health = ' + colors.fg.green + str(char.health) + colors.reset, end='')
    print()
