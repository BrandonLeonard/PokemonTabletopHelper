# from tkinter import *
#
# window = Tk()
# window.title = "Pokemon Tabletop Helper"
#
# pkmnlabel = Label(window, text="Pokemon 1")
# atklabel = Label(window, text="Atk")
# button = Button(window, text="Attack")
# atkInput = Entry(window, width=15)
#
# pkmnlabel.grid(column=0, row=0)
# atklabel.grid(column=0, row=1)
# atkInput.grid(column=2, row=1)
# button.grid(column=3, row=1)
#
#
# window.mainloop()


def modifier(targets=False, weather=1, critical=False, roll=12, STAB=False, typeEff=1, other=1):
    targetnum = 1
    criticalnum = 1
    STABnum = 1
    rollNum = roll/20.0

    if targets:
        targetnum = .75

    if weather > 1:
        weather = 1.5
    elif weather < 1:
        weather = .5

    if critical:
        criticalnum = 1.5

    if STAB:
        STABnum = 1.5

    if typeEff > 2:
        typeEff = 4
    elif typeEff > 1 and typeEff <= 2:
        typeEff = 2
    elif typeEff < .5:
        typeEff = .25
    elif typeEff < 1 and typeEff >= .5:
        typeEff = .5

    return targetnum * weather * criticalnum * rollNum * STABnum * typeEff * other

class Trainer():
    def __init__(self):
        self.name = ''
        self.pokemon = {}
        self.items = []

    def addItem(self, item=''):
        self.items.append(item)

    def useItem(self, item=''):
        self.items.remove(item)

    def addPokemon(self, species = '', nickname='', ability=''):
        poke = Pokemon(species=species, nickname=nickname, ability=ability)
        self.pokemon.update({species: poke})

class Pokemon(object):
    """docstring for Pokemon"""

    def __init__(self, species = '', nickname = '', ability = ''):
        super(Pokemon, self).__init__()
        self.species = species
        self.nickname = nickname
        self.ability = ability
        self.stats = Stats()
        self.ivs = Stats()
        self.totalHp = 1
        self.currentHp = 1

    def updateStats (self, hp=0, atk=0, defn=0, spAtk=0, spDefn=0, spd=0):
        self.stats = Stats(hp=hp, atk=atk, defn=defn, spAtk=spAtk, spDefn=spDefn, spd=spd)
        percent = self.currentHp / self.totalHp

    def updateIVs (self, hp=0, atk=0, defn=0, spAtk=0, spDefn=0, spd=0):
        self.ivs = Stats(hp=hp, atk=atk, defn=defn, spAtk=spAtk, spDefn=spDefn, spd=spd)


class Stats(object):
    """docstring for Stats"""

    def __init__(self, hp=0, atk=0, defn=0, spAtk=0, spDefn=0, spd=0):
        super(Stats, self).__init__()
        self.hp = hp
        self.atk = atk
        self.defn = defn
        self.spAtk = spAtk
        self.spDefn = spDefn
        self.spd = spd
