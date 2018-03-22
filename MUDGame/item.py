from pickle import Pickler
from pickle import Unpickler

class Item:
    def __init__(self, name, level, cost, description, giver, health):
        self.name = name
        self.level = level
        self.cost = cost,
        self.description = description
        self.giver = giver
        self.health = health

    def save(self, kind):
        try:
            f = open("../data/items/"+ kind +"_"+ self.name + ".txt", "wb")
        except FileNotFoundError:
            print('Item file not found. Unable to save progress.')
            print()
            return
        Pickler(f).dump(self)
        f.close()
        return
        
class Weapon(Item):
    def __init__(self, name, level, cost, description, attackValue, giver, handed, health):
        Item.__init__(self, name, level, cost, description, giver, health)
        self.attackValue = attackValue
        self.handed = handed

class Shield(Item):
    def __init__(self, name, level, cost, description, defenceValue, giver, health):
        Item.__init__(self, name, level, cost, description, giver, health)
        self.defenceValue = defenceValue

class Armor(Item):
    def __init__(self, name, level, cost, description, defenceValue, giver, health):
        Item.__init__(self, name, level, cost, description, giver, health)
        self.defenceValue = defenceValue

def newWeapon():
    name = input("Name: ")
    level = int(input("Level: "))
    cost = int(input("Cost: "))
    description = input("Description: ")
    attackValue = int(input("Attack Value: "))
    health = int(input("Health: "))
    giver = {"strength":0, "agility":0, "wit":0, "luck":0}
    print("Effects on stats:")
    for key in giver:
        giver[key] = int(input(key + ": "))
    handed = input("One-handed (1) or Two-handed (2)? ")
    weapon = Weapon(name, level, cost, description, attackValue, giver, handed, health)
    weapon.save("wpn")
    print("New weapon created.")

def newShield():
    name = input("Name: ")
    level = int(input("Level: "))
    cost = int(input("Cost: "))
    description = input("Description: ")
    defenceValue = int(input("Defence Value: "))
    health = int(input("Health: "))
    giver = {"strength":0, "agility":0, "wit":0, "luck":0}
    print("Effects on stats:")
    for key in giver:
        giver[key] = int(input(key + ": "))
    shield = Shield(name, level, cost, description, defenceValue, giver, health)
    shield.save("shd")
    print("New shield created.")

def newArmor():
    name = input("Name: ")
    level = int(input("Level: "))
    cost = int(input("Cost: "))
    description = input("Description: ")
    defenceValue = int(input("Defence Value: "))
    health = int(input("Health: "))
    giver = {"strength":0, "agility":0, "wit":0, "luck":0}
    print("Effects on stats:")
    for key in giver:
        giver[key] = int(input(key + ": "))
    armor = Armor(name, level, cost, description, defenceValue, giver, health)
    armor.save("arm")
    print("New armor created.")

def loadItem(name, kind):
        '''
        takes the npc name and kind,
        returns the npc object
        '''
        try:
            f = open("../data/items/" + kind + "_" + name + ".txt", "rb")
        except FileNotFoundError:
            print("Item file not found. Unable to load progress. \n")
            print("Please enter a valid Item name or kind.")
        item = Unpickler(f).load()
        f.close()
        return item
    
