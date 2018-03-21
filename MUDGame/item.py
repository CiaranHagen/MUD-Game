class Item:
    def __init__(self, name, level, cost, description):
        self.name = name
        self.level = level
        self.cost = cost,
        self.description = description
        self.giver = giver

    def save(self, kind):
        try:
            f = open("../data/items/"+ kind +"_"+ self.name + ".txt", "wb")
        except FileNotFoundError:
            print('NPC file not found. Unable to save progress.')
            print()
            return
        Pickler(f).dump(self)
        f.close()
        return
        
class Weapon(Item):
    def __init__(self, name, level, cost, description, attackValue, giver, handed):
        Item.__init__(self, name, level, cost, description, giver)
        self.attackValue = attackValue
        self.handed = handed

class Shield(Item):
    def __init__(self, name, level, cost, description, defenceValue, giver):
        Item.__init__(self, name, level, cost, description, giver)
        self.defenceValue = defenceValue

class Armor(Item):
    def __init__(self, name, level, cost, description, defenceValue, giver):
        Item.__init__(self, name, level, cost, description, giver)
        self.defenceValue = defenceValue

def newWeapon():
    name = input()
    level = input()
    cost = input()
    description = input()
    attackValue = input()
    giver = input()
    handed = input()
    weapon = Weapon(name, level, cost, description, attackValue, giver, handed)
    weapon.save("wpn")

def newShield():
    name = input()
    level = input()
    cost = input()
    description = input()
    defenceValue = input()
    giver = input()
    shield = Shield(name, level, cost, description, defenceValue, giver)
    shield.save("shd")

def newArmor():
    name = input()
    level = input()
    cost = input()
    description = input()
    defenceValue = input()
    giver = input()
    armor = Armor(name, level, cost, description, defenceValue, giver)
    armor.save("arm")
    
