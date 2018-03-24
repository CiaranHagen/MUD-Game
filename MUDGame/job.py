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

def chooseJob(currentPlayer):
    job = 1
    choice = 0
    while job == 1:

        jobList = ["warrior", "rogue", "beggar"]

<<<<<<< Updated upstream
        if currentPlayer.admin == False:
            charJob = str(input("What class do you choose? \n"
                        "You can choose from:  "+ colors.fg.cyan +"{}\n> ".format(jobList)).lower())
            print(colors.reset , end = '')

            if charJob in jobList:
                if charJob == "warrior":
                    print('warriors are a heavy class known for their strength and proficiency with swords & shields\n')
                    print('you get a bonus of ' + colors.fg.cyan + '+5 on strength' + colors.reset , end = '' + ', proficiency with swords & shields and bonus on any armor')
                    print('but as a heavy skullmasher you have ' + colors.fg.red + '-1 wit and -1 agility' + colors.reset , end = '')
                    choice = 1
                if charJob == "rogue":
                    print('rogues are a nimble class known for their agility and proficiency with daggers\n')
                    print('you get a bonus of ' + colors.fg.cyan + '+3 on agility ' + colors.reset , end = '' + ', proficiency with daggers and bonus on light armor')
                    choice = 1
                if charJob == "beggar":
                    print('beggars are beggars, nothing special .... what did you expect ?\n')
                    print('you get a non-existant bonus of ' + colors.fg.orange + '+999' + colors.reset + ' on everything,\n'
                          'proficiency in begging and an additional amount of ' + colors.fg.orange + 'self-pity' + colors.reset , end = '')
                    choice = 1
=======
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
    def Job(currentPlayer):

        jobList = ["warrior", "rogue", "beggar"]

        if currentPlayer.admin == False:
            charJob = str(input("What class do you choose? \n"
                                "You can choose from:  "+ colors.fg.cyan +"warrior, rogue, beggar\n>" + colors.reset , end = '').lower()

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
>>>>>>> Stashed changes
            else:
                print("This class is not known to me.. Try again.\n")

        elif currentPlayer.admin == True:
            charJob = str(input("What class do you choose? \n"
<<<<<<< Updated upstream
                        "You can choose from:  "+ colors.fg.purple + " admin (anything else is fine too) or standard: "+ colors.fg.cyan +"{}\n> ".format(jobList)).lower())
            print(colors.reset , end = '')
            if charJob == "admin":
=======
                                "You can choose from:  "+ colors.fg.cyan +"warrior, rogue, beggar" + colors.fg.purple + " or ADMIN ... (anything else is fine too)" "\n>" +colors.reset , end = '')
            if charJob == "ADMIN":
>>>>>>> Stashed changes
                print(colors.fg.purple + 'ADMINS are the ruler of all, the übermenschen')
                print('ADMIN gets an existant bonus of +666 on all stats ... is there any need to say more ?')
                choice = 1
            if charJob == "warrior":
                print('warriors are a heavy class known for their strength and proficiency with swords & shields\n')
                print('you get a bonus of ' + colors.fg.cyan + '+5 on strength' + colors.reset , end = '' + ', proficiency with swords & shields and bonus on any armor')
                print('but as a heavy skullmasher you have ' + colors.fg.red + '-1 wit and -1 agility' + colors.reset , end = '')
                choice = 1
            if charJob == "rogue":
                print('rogues are a nimble class known for their agility and proficiency with daggers\n')
                print('you get a bonus of ' + colors.fg.cyan + '+3 on agility ' + colors.reset , end = '' + ', proficiency with daggers and bonus on light armor')
                choice = 1
            if charJob == "beggar":
                print('beggars are beggars, nothing special .... what did you expect ?\n')
                print('you get a non-existant bonus of ' + colors.fg.orange + '+999' + colors.reset + ' on everything,\n'
                    'proficiency in begging and an additional amount of ' + colors.fg.orange + 'self-pity' + colors.reset , end = '')
<<<<<<< Updated upstream
                choice = 1
            else:
                choice = 1

        while choice == 1:
            print(colors.reset + "Do you wish to choose " + colors.fg.cyan + str(charJob.upper()) + colors.reset + " as your class ? \n["
                    + colors.fg.green + "yes" + colors.reset + "/" + colors.fg.red + "no" + colors.reset , end = ''  + "]\n")
            answer = input('> ' + colors.fg.cyan).lower()
            print(colors.reset , end = '')
            if answer in ['y', 'yes']:
                print()
                print('congraz, you are now officialy a ' + colors.fg.cyan + str(charJob.upper()) + colors.reset)
                choice = 0
                job = 0
            elif answer in ['n', 'no']:
                choice = 0
                job = 1
            elif answer not in ['y', 'yes', 'n', 'no']:
                print ("this is not a valid input, try again ... \n")
                choice = 1
                job = 0

    if choice == 0 and job == 0:
        return charJob
    else:
        print('Something went wrong !')
        return chooseJob(currentPlayer)
=======
                return choice(charJob)
            else:
                print(colors.fg.purple + str(charJob) + colors.reset , end = '' + ' is an interesting choice ... have fun I guess')
    return Job(currentPlayer)
>>>>>>> Stashed changes

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def jobStrength(charJob,strength):

    if charJob == "admin":
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

    else:
        strength = int(strength) + random.randint(0,10)
        return str(strength)

def jobAgility(charJob,agility):

    if charJob == "admin":
        agility = int(agility)+666
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

    else:
        agility = int(agility) + random.randint(0,10)
        return str(agility)

def jobWit(charJob,wit):

    if charJob == "admin":
        wit = int(wit)+666
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

    else:
        wit = int(wit) + random.randint(0,3)
        return str(wit)

def jobLuck(charJob,luck):

    if charJob == "admin":
        luck = int(luck)+666
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

    else:
        luck = int(luck) + random.randint(0,3)
        return str(luck)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def jobLevelUp(char):
    print('!!!!!!!!!!!!!!! TADAAAAAAAAAAA !!!!!!!!!!!')
    time.sleep(1)
    print()
    print('Congratz, you have gained a level !')
    time.sleep(1)
    print()
    print('Your '+ colors.fg.cyan + str(char.job) + colors.reset + ' is now level ' + colors.fg.cyan + str(char.level) + colors.reset, end='')
    time.sleep(1)
    print()
    if char.job == 'warrior':
        print('Your stats have improved !')
        print()
        strBonus = random.randint(2,4)
        agiBonus = random.randint(0,2)
        witBonus = random.randint(-5,2)
        if witBonus < 0:
            witBonus = 0
        luckBonus = random.randint(-10,2)
        if luckBonus < 0:
            luckBonus = 0
        hpBonus = random.randint(0,201)
        char.stats['strength'] += int(strBonus)
        char.stats['agility'] += int(agiBonus)
        char.stats['wit'] += int(witBonus)
        char.stats['luck'] += int(luckBonus)
        char.maxhealth += hpBonus
        char.health = char.maxhealth
        print('you gained :\n'
              + colors.fg.cyan + ' +' + str(strBonus) + ' strength' + colors.reset + '\n'
              + colors.fg.cyan + ' +' + str(agiBonus) + ' agility' + colors.reset + '\n'
              + colors.fg.cyan + ' +' + str(witBonus) + ' wit' + colors.reset + '\n'
              + colors.fg.cyan + ' +' + str(luckBonus) + ' luck' + colors.reset + '\n'
              + colors.fg.cyan + '+' + str(hpBonus) + ' maxhealth' + colors.reset, end='')
    if char.job == 'rogue':
        print('Your stats have improved !')
        print()
        strBonus = random.randint(0,2)
        agiBonus = random.randint(2,4)
        witBonus = random.randint(-5,2)
        if witBonus < 0:
            witBonus = 0
        luckBonus = random.randint(-10,2)
        if luckBonus < 0:
            luckBonus = 0
        hpBonus = random.randint(0,101)
        char.stats['strength'] += int(strBonus)
        char.stats['agility'] += int(agiBonus)
        char.stats['wit'] += int(witBonus)
        char.stats['luck'] += int(luckBonus)
        char.maxhealth += hpBonus
        char.health = char.maxhealth
        print('you gained :\n'
              + colors.fg.cyan + ' +' + str(strBonus) + ' strength' + colors.reset + '\n'
              + colors.fg.cyan + ' +' + str(agiBonus) + ' agility' + colors.reset + '\n'
              + colors.fg.cyan + ' +' + str(witBonus) + ' wit' + colors.reset + '\n'
              + colors.fg.cyan + ' +' + str(luckBonus) + ' luck' + colors.reset + '\n'
              + colors.fg.cyan + '+' + str(hpBonus) + ' maxhealth' + colors.reset, end='')
    if char.job == "admin":
        print('You have become even more awesome and undying !')
        print()
        strBonus = random.randint(0,10)
        agiBonus = random.randint(0,10)
        witBonus = random.randint(0,10)
        luckBonus = random.randint(0,10)
        hpBonus = random.randint(0,1001)
        char.stats['strength'] += int(strBonus)
        char.stats['agility'] += int(agiBonus)
        char.stats['wit'] += int(witBonus)
        char.stats['luck'] += int(luckBonus)
        char.maxhealth += hpBonus
        char.health = char.maxhealth
        print('you gained :\n'
              + colors.fg.cyan + ' +' + str(strBonus) + ' strength' + colors.reset + '\n'
              + colors.fg.cyan + ' +' + str(agiBonus) + ' agility' + colors.reset + '\n'
              + colors.fg.cyan + ' +' + str(witBonus) + ' wit' + colors.reset + '\n'
              + colors.fg.cyan + ' +' + str(luckBonus) + ' luck' + colors.reset + '\n'
              + colors.fg.cyan + '+' + str(hpBonus) + ' maxhealth' + colors.reset, end='')
    if char.job not in ['warrior', 'rogue', 'beggar', 'admin']:
        print('Your random class will gain random stat bonuses')
        print()
        strBonus = random.randint(0,10)
        agiBonus = random.randint(0,10)
        witBonus = random.randint(0,6)
        luckBonus = random.randint(0,3)
        hpBonus = random.randint(0,501)
        char.stats['strength'] += int(strBonus)
        char.stats['agility'] += int(agiBonus)
        char.stats['wit'] += int(witBonus)
        char.stats['luck'] += int(luckBonus)
        char.maxhealth += hpBonus
        char.health = char.maxhealth
        print('you gained :\n'
              + colors.fg.cyan + ' +' + str(strBonus) + ' strength' + colors.reset + '\n'
              + colors.fg.cyan + ' +' + str(agiBonus) + ' agility' + colors.reset + '\n'
              + colors.fg.cyan + ' +' + str(witBonus) + ' wit' + colors.reset + '\n'
              + colors.fg.cyan + ' +' + str(luckBonus) + ' luck' + colors.reset + '\n'
              + colors.fg.cyan + '+' + str(hpBonus) + ' maxhealth' + colors.reset, end='')
    print()
    time.sleep(1)
    print('Your upgraded stats are:\n')
    print(colors.fg.cyan + str(char.stats) + colors.reset, end = '' '\n')
    print(colors.fg.cyan + 'Health = ' + colors.fg.green + str(char.health) + colors.reset, end='')
    print()
