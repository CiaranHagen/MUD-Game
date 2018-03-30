import character, room, npc, player, attack, os, operator, random, item, job, race, time, mapmod, look, go
from admin import adminer

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


def mapper(litX, bigX, litY, bigY, mapL, cRoom):
    drawL = []
    distX = (-1) * litX
    distY = (-1) * litY
    for j in range(litY, bigY+1):
        drawL.append([])
        for i in range(litX, bigX+1):
            if (i,j) in mapL:
                drawL[j + distY].append("O")
            else:
                drawL[j + distY].append(" ")
    dis = (bigX - litX - 2)//2
    if dis < 2:
        dis = 2
    print(dis*"=" + " MAP " + dis*"=")
    print()
    for j in range(bigY, litY-1, -1):
        spaceLine = " "
        print(" ", end="")
        for i in range(litX, bigX+1):
            if cRoom.location == (i,j):
                print(colors.fg.red, end='')
            else:
                print(colors.fg.cyan, end='')
            print(drawL[j + distY][i + distX], end='')
            print(colors.fg.cyan, end='')
            if (drawL[j + distY][i + distX] == "O") and ((i + distX) != (len(drawL[j+distY])-1)):
                if "east" in room.loadRoom("room" + str(i) + "_" + str(j)).possibleDirections.values():
                    print(colors.fg.cyan + "--", end='')
                else:
                    print("  ", end='')
            else:
                print("  ", end='')

            if (drawL[j + distY][i + distX] == "O") and ((j + distY) != 0):
                if "south" in room.loadRoom("room" + str(i) + "_" + str(j)).possibleDirections.values():
                    spaceLine += "|  "
                else:
                    spaceLine += "   "
            else:
                spaceLine += "   "

        print("", end="\n")
        print(spaceLine)
    print(colors.reset , end = '')
    print(dis*"=" + " MAP " + dis*"=")
