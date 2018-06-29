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


def nick():
    nick = Trainer('Nick')
    createStandardPokes(nick)

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


def createStandardPokes(trainer):
    gengar = Pokemon(species='Gengar', ability='Incorporeal Movement - Can Move through Objects as though it were difficult terrain.')
    gengar.updateIVs(hp=15, atk=15, defn=15, spAtk=15, spDefn=15, spd=15)
    gengar.updateStats(hp=245, atk=135, defn=140, spAtk=280, spDefn=170, spd=264)
    blastoise = Pokemon(species='Blastoise',
                     ability='Withdraw - This pokemon can retreat into its shell as its move. This will decrease damage taken by 1/2.')
    blastoise.updateIVs(hp=15, atk=15, defn=15, spAtk=15, spDefn=15, spd=15)
    blastoise.updateStats(hp=283, atk=167, defn=220, spAtk=209, spDefn=230, spd=176)
    charizard = Pokemon(species='Charizard',
                     ability='Inner Fire - Fire moves get an extra 10 feet of effectiveness')
    charizard.updateIVs(hp=15, atk=15, defn=15, spAtk=15, spDefn=15, spd=15)
    charizard.updateStats(hp=283, atk=167, defn=220, spAtk=209, spDefn=230, spd=176)
    venusaur = Pokemon(species='Venusaur',
                     ability='Vine Dexterity - This pokemon may move an object or entity (within reason) up to 30 feet if it is within 30 feet of reach as its move.')
    venusaur.updateIVs(hp=15, atk=15, defn=15, spAtk=15, spDefn=15, spd=15)
    venusaur.updateStats(hp=285, atk=165, defn=186, spAtk=220, spDefn=242, spd=180)
    chansey = Pokemon(species='Chansey',
                     ability='Healing Aura - All friendly creatures within 30ft gain 1/8 total health at end of the turn')
    chansey.updateIVs(hp=15, atk=15, defn=15, spAtk=15, spDefn=15, spd=15)
    chansey.updateStats(hp=625, atk=27, defn=33, spAtk=90, spDefn=230, spd=120)
    gyarados = Pokemon(species='Gyarados',
                     ability='Rampage - Gyarados may choose to attack with 50% extra damage, at the cost of losing the next turn. (cumulative)')
    gyarados.updateIVs(hp=15, atk=15, defn=15, spAtk=15, spDefn=15, spd=15)
    gyarados.updateStats(hp=315, atk=270, defn=178, spAtk=126, spDefn=220, spd=200)
    alakazam = Pokemon(species='Alakazam',
                     ability='Telekinesis - This pokemon may move any object or entity (within reason) up to 30ft, within 30ft of you.')
    alakazam.updateIVs(hp=15, atk=15, defn=15, spAtk=15, spDefn=15, spd=15)
    alakazam.updateStats(hp=315, atk=270, defn=178, spAtk=126, spDefn=220, spd=200)
    lapras = Pokemon(species='Lapras',
                     ability='Ferry - This pokemon can carry two pokemon on its back at full speed, three to four at 1/2 speed')
    lapras.updateIVs(hp=15, atk=15, defn=15, spAtk=15, spDefn=15, spd=15)
    lapras.updateStats(hp=385, atk=171, defn=180, spAtk=209, spDefn=210, spd=140)
    snorlax = Pokemon(species='Snorlax',
                     ability='Snore - While asleep, this pokemon will snore so loudly that any pokemon within 20 ft take 1/8 hp damage.')
    snorlax.updateIVs(hp=15, atk=15, defn=15, spAtk=15, spDefn=15, spd=15)
    snorlax.updateStats(hp=445, atk=240, defn=150, spAtk=150, spDefn=240, spd=80)
    arcanine = Pokemon(species='Arcanine',
                     ability='Flash Fire - if hit with a fire type move, this pokemon takes no damage, if the next move used is a fire type, it does 50% more damage')
    arcanine.updateIVs(hp=15, atk=15, defn=15, spAtk=15, spDefn=15, spd=15)
    arcanine.updateStats(hp=305, atk=264, defn=180, spAtk=198, spDefn=180, spd=210)
    magneton = Pokemon(species='Magneton',
                       ability='Analytical - If this pokemon moves last, it gains 25% increase to attacks.')
    magneton.updateIVs(hp=15, atk=15, defn=15, spAtk=15, spDefn=15, spd=15)
    magneton.updateStats(hp=225, atk=126, defn=210, spAtk=260, spDefn=160, spd=176)

    trainer.addPokemon(poke=gengar)
    trainer.addPokemon(poke=charizard)
    trainer.addPokemon(poke=blastoise)
    trainer.addPokemon(poke=venusaur)
    trainer.addPokemon(poke=chansey)
    trainer.addPokemon(poke=gyarados)
    trainer.addPokemon(poke=alakazam)
    trainer.addPokemon(poke=lapras)
    trainer.addPokemon(poke=snorlax)
    trainer.addPokemon(poke=arcanine)
    trainer.addPokemon(poke=magneton)
    return trainer


class Trainer(object):
    def __init__(self, name):
        self.name = name
        self.pokemon = {}
        self.items = []

    def addItem(self, item=''):
        self.items.append(item)

    def useItem(self, item=''):
        self.items.remove(item)

    def addPokemon(self, poke):
        self.pokemon.update({poke.species: poke})


class Pokemon(object):
    """docstring for Pokemon"""

    def __init__(self, species = '', type1='', type2='', nickname = '', ability = ''):
        super(Pokemon, self).__init__()
        self.species = species
        self.nickname = nickname
        self.type1 = type1
        self.type2 = type2
        self.ability = ability
        self.stats = Stats()
        self.ivs = Stats()
        self.totalHp = 1
        self.currentHp = 1
        self.moveset = Moveset()

    def updateStats (self, hp=0, atk=0, defn=0, spAtk=0, spDefn=0, spd=0):
        self.stats = Stats(hp=hp, atk=atk, defn=defn, spAtk=spAtk, spDefn=spDefn, spd=spd)
        percent = self.currentHp / self.totalHp
        self.totalHp = hp
        self.currentHp = hp * percent

    def updateIVs (self, hp=0, atk=0, defn=0, spAtk=0, spDefn=0, spd=0):
        self.ivs = Stats(hp=hp, atk=atk, defn=defn, spAtk=spAtk, spDefn=spDefn, spd=spd)

    def damage(self, pokemon, dmg=0):
        self.currentHp -= dmg


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


class Moveset (object):
    def __init__(self):
        self.one = Move()
        self.two = Move()
        self.three = Move()
        self.four = Move()


class Move (object):
    def __init__(self, name='', power=0, accuracy=0, pp=0, type1='', effect=''):
        self.name = name
        self.power = power
        self.accuracy = accuracy
        self.pp = pp
        self.type1 = type1
        self.effect = effect