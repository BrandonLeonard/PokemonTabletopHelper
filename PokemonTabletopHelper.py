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


def createStandardPokes(trainer):
    gengar = Pokemon(species='Gengar', ability='Incorporeal Movement - Can Move through Objects as though it were difficult terrain.', level=100)
    gengar.updateIVs(hp=15, atk=15, defn=15, spAtk=15, spDefn=15, spd=15)
    gengar.updateStats(hp=245, atk=135, defn=140, spAtk=280, spDefn=170, spd=264)
    gengar.moveset.one = Move('Shadow Ball', 80, 100, 15, 'Ghost', 'Pokemon hurls a shadowy blob at the target.')
    gengar.moveset.two = Move('Sludge Bomb', 90, 100, 10, 'Poison', 'Unsanitary Sludge is hurled at the target. 30% chance poison')
    gengar.moveset.three = Move('Hypnosis', 0, 60, 20, 'Psychic', 'User employs hypnotic suggestion to put target to sleep')
    gengar.moveset.four = Move('Dream Eater', 100, 100, 15, 'Ghost', 'User eats targets dream. Regains half of damage as HP. Only works on sleeping foes.')

    blastoise = Pokemon(species='Blastoise',
                        ability='Withdraw - This pokemon can retreat into its shell as its move. This will decrease damage taken by 1/2.',
                        level=100, type1='Water')
    blastoise.updateIVs(hp=15, atk=15, defn=15, spAtk=15, spDefn=15, spd=15)
    blastoise.updateStats(hp=283, atk=167, defn=220, spAtk=209, spDefn=230, spd=176)
    blastoise.moveset.one = Move('Surf', 95, 100, 15, 'Water', '')
    blastoise.moveset.two = Move('Water Pulse', 60, 100, 20, 'Water', '20% Confusion')
    blastoise.moveset.three = Move('Ice Beam', 90, 100, 10, 'Ice', '10% Freeze')
    blastoise.moveset.four = Move('Rapid Spin', 20, 100, 40, 'Normal', 'Can be used to free itself from wrap, telekinesis, etc.')

    charizard = Pokemon(species='Charizard',
                     ability='Inner Fire - Fire moves get an extra 10 feet of effectiveness',
                        level=100, type1='Fire', type2='Flying')
    charizard.updateIVs(hp=15, atk=15, defn=15, spAtk=15, spDefn=15, spd=15)
    charizard.updateStats(hp=283, atk=167, defn=220, spAtk=209, spDefn=230, spd=176)
    charizard.moveset.one = Move('Flamethrower', 90, 100, 15, 'Fire', '10% Burn')
    charizard.moveset.two = Move('Dragon Claw', 80, 100, 15, 'Dragon', '')
    charizard.moveset.three = Move('Earthquake', 100, 100, 15, 'Ground', '')
    charizard.moveset.four = Move('Roost', 0, 100, 10, 'Flying', 'User gains 50% hp')

    venusaur = Pokemon(species='Venusaur',
                     ability='Vine Dexterity - This pokemon may move an object or entity (within reason) up to 30 feet if it is within 30 feet of reach as its move.',
                        level=100, type1='Grass', type2='Poison')
    venusaur.updateIVs(hp=15, atk=15, defn=15, spAtk=15, spDefn=15, spd=15)
    venusaur.updateStats(hp=285, atk=165, defn=186, spAtk=220, spDefn=242, spd=180)
    venusaur.moveset.one = Move('Giga Drain', 75, 100, 15, 'Grass', 'User gains 50% of damage as hp')
    venusaur.moveset.two = Move('Sludge Bomb', 90, 100, 15, 'Poison', '30% Poison')
    venusaur.moveset.three = Move('Synthesis', 0, 100, 15, 'Grass', 'User Gains 50% hp')
    venusaur.moveset.four = Move('Toxic', 0, 100, 15, 'Poison', 'User Becomes Badly Poisoned')


    chansey = Pokemon(species='Chansey',
                     ability='Healing Aura - All friendly creatures within 30ft gain 1/8 total health at end of the turn',
                        level=100, type1='Normal')
    chansey.updateIVs(hp=15, atk=15, defn=15, spAtk=15, spDefn=15, spd=15)
    chansey.updateStats(hp=625, atk=27, defn=33, spAtk=90, spDefn=230, spd=120)
    chansey.moveset.one = Move('Toxic', 0, 100, 15, 'Poison', 'User Becomes Badly Poisoned')
    chansey.moveset.two = Move('Soft-Boiled', 0, 100, 15, 'Normal', 'User Gains 50% hp')
    chansey.moveset.three = Move('Heal-Pulse', 0, 100, 15, 'Normal', 'Target Gains 50% hp')
    chansey.moveset.four = Move('Sing', 0, 55, 15, 'Normal', 'Target falls asleep')

    gyarados = Pokemon(species='Gyarados',
                     ability='Rampage - Gyarados may choose to attack with 50% extra damage, at the cost of losing the next turn. (cumulative)',
                        level=100, type1='Water', type2='Flying')
    gyarados.updateIVs(hp=15, atk=15, defn=15, spAtk=15, spDefn=15, spd=15)
    gyarados.updateStats(hp=315, atk=270, defn=178, spAtk=126, spDefn=220, spd=200)
    gyarados.moveset.one = Move('Bounce', 85, 90, 15, 'Flying', 'two turn move, 30% paralysis')
    gyarados.moveset.two = Move('Waterfall', 80, 100, 15, 'Water', '20% Flinch')
    gyarados.moveset.three = Move('Hyper Beam', 150, 90, 15, 'Normal', 'User must rest on next turn')
    gyarados.moveset.four = Move('Aqua Tail', 90, 90, 15, 'Water', '')

    alakazam = Pokemon(species='Alakazam',
                     ability='Telekinesis - This pokemon may move any object or entity (within reason) up to 30ft, within 30ft of you.',
                        level=100, type1='Psychic')
    alakazam.updateIVs(hp=15, atk=15, defn=15, spAtk=15, spDefn=15, spd=15)
    alakazam.updateStats(hp=315, atk=270, defn=178, spAtk=126, spDefn=220, spd=200)
    alakazam.moveset.one = Move('Psychic', 90, 90, 15, 'Psychic', '')
    alakazam.moveset.two = Move('Focus Blast', 120, 100, 15, 'Fighting', '')
    alakazam.moveset.three = Move('Shadow Ball', 80, 100, 15, 'Ghost', '')
    alakazam.moveset.four = Move('Future Sight', 120, 100, 15, 'Psychic', '')

    lapras = Pokemon(species='Lapras',
                     ability='Ferry - This pokemon can carry two pokemon on its back at full speed, three to four at 1/2 speed',
                        level=100, type1='Water', type2='Ice')
    lapras.updateIVs(hp=15, atk=15, defn=15, spAtk=15, spDefn=15, spd=15)
    lapras.updateStats(hp=385, atk=171, defn=180, spAtk=209, spDefn=210, spd=140)
    lapras.moveset.one = Move('Freeze-Dry', 70, 90, 15, 'Ice', '10% Freeze, super effective on Water Types')
    lapras.moveset.two = Move('Hydro Pump', 110, 100, 15, 'Water', '')
    lapras.moveset.three = Move('Body Slam', 85, 100, 15, 'Normal', '30% Paralysis')
    lapras.moveset.four = Move('Brine', 65, 100, 15, 'Water', 'This move does double damage if target hp is <50%')

    snorlax = Pokemon(species='Snorlax',
                     ability='Snore - While asleep, this pokemon will snore so loudly that any pokemon within 20 ft take 1/8 hp damage.',
                        level=100, type1='Normal')
    snorlax.updateIVs(hp=15, atk=15, defn=15, spAtk=15, spDefn=15, spd=15)
    snorlax.updateStats(hp=445, atk=240, defn=150, spAtk=150, spDefn=240, spd=80)
    lapras.moveset.one = Move('Rollout', 30, 90, 15, 'Rock', 'Damage multiplied every consecutive turn, lasts five turns or until miss.')
    lapras.moveset.two = Move('Rest', 0, 100, 15, 'Flying', 'User goes to sleep for two turns. Fully restores HP and status.')
    lapras.moveset.three = Move('Body Slam', 85, 100, 15, 'Normal', '30% Paralysis')
    lapras.moveset.four = Move('Yawn', 0, 100, 15, 'Normal', 'This move does double damage if target hp is <50%')

    arcanine = Pokemon(species='Arcanine',
                     ability='Flash Fire - if hit with a fire type move, this pokemon takes no damage, if the next move used is a fire type, it does 50% more damage',
                        level=100, type1='Fire')
    arcanine.updateIVs(hp=15, atk=15, defn=15, spAtk=15, spDefn=15, spd=15)
    arcanine.updateStats(hp=305, atk=264, defn=180, spAtk=198, spDefn=180, spd=210)
    arcanine.moveset.one = Move('Flare Blitz', 120, 90, 15, 'Fire', '10% chance burn, damages user by half damage done to target.')
    arcanine.moveset.two = Move('Extreme Speed', 80, 100, 15, 'Normal', 'This move always goes first.')
    arcanine.moveset.three = Move('Wild Charge', 90, 100, 15, 'Electric', 'Receives recoil 1/4 damage done to the target.')
    arcanine.moveset.four = Move('Heat Wave', 90, 100, 15, 'Fire', '10% Burn')

    magneton = Pokemon(species='Magneton',
                       ability='Analytical - If this pokemon moves last, it gains 25% increase to attacks.',
                        level=100, type1='Electric', type2='Steel')
    magneton.updateIVs(hp=15, atk=15, defn=15, spAtk=15, spDefn=15, spd=15)
    magneton.updateStats(hp=225, atk=126, defn=210, spAtk=260, spDefn=160, spd=176)
    arcanine.moveset.one = Move('Thunderbolt', 120, 90, 15, 'Fire', '10% Paralysis')
    arcanine.moveset.two = Move('Flash Cannon', 80, 100, 15, 'Normal', '')
    arcanine.moveset.three = Move('Tri Attack', 80, 100, 15, 'Electric', '20% chance of freeze, burn, or paralysis')
    arcanine.moveset.four = Move('ThunderWave', 0, 100, 15, 'Fire', 'Paralyzes target.')

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
    print(trainer)
    return trainer


class Trainer(object):
    def __init__(self, name):
        self.name = name
        self.pokemon = {}
        self.items = []

    def __str__(self):
        return """name: {}
        pokemon: {}
        items: {}""".format(self.name, self.pokemon.keys(), self.items)

    def addItem(self, item=''):
        self.items.append(item)
        print('added ' + item)

    def useItem(self, item=''):
        self.items.remove(item)
        print('removed ' + item)

    def addPokemon(self, poke):
        self.pokemon.update({poke.species: poke})
        print('added ' + poke.species)


class Pokemon(object):
    """docstring for Pokemon"""

    def __init__(self, species = '', type1='', type2='', nickname = '', ability = '', level = 1):
        super(Pokemon, self).__init__()
        self.species = species
        self.nickname = nickname
        self.type1 = type1
        self.type2 = type2
        self.level = level
        self.ability = ability
        self.stats = Stats()
        self.ivs = Stats()
        self.totalHp = 1
        self.currentHp = 1
        self.moveset = Moveset()

    def __str__(self):
        return """{} - {}
        Lvl: {}
        HP: {}
        Type: {} {}
        Ability: {}
        Stats:  {}
        IVs:  {}
        Moves: 
        {}
        """.format(self.species, self.nickname, self.level, self.healthBar(), self.type1, self.type2, self.ability, self.stats, self.ivs, self.moveset)

    def healthBar(self):
        percent = self.currentHp / self.totalHp * 100
        fill = int(percent/5)
        fillstr = '     /'
        for i in range(0, fill):
            fillstr = fillstr + '#'
        for i in range (fill, 20):
            fillstr = fillstr + '='
        fillstr = str(self.currentHp) + '/' + str(self.totalHp) + fillstr + '/   ' + str(percent) + '%'
        print(fillstr)
        return fillstr

    def updateStats (self, hp=1, atk=1, defn=1, spAtk=1, spDefn=1, spd=1):
        self.stats = Stats(hp=hp, atk=atk, defn=defn, spAtk=spAtk, spDefn=spDefn, spd=spd)
        percent = self.currentHp / self.totalHp
        self.totalHp = hp
        self.currentHp = hp * percent
        print("""Hp: {} / {}    Stats: {}""".format(self.currentHp, self.totalHp, self.stats))

    def updateIVs (self, hp=0, atk=0, defn=0, spAtk=0, spDefn=0, spd=0):
        self.ivs = Stats(hp=hp, atk=atk, defn=defn, spAtk=spAtk, spDefn=spDefn, spd=spd)
        print(self.ivs)

    def physicalDamage(self, pokemon, dmg=0, modifier=1):
        levelMod = (2*self.level/5)+2
        statCalc = (levelMod * dmg * pokemon.stats.atk / self.stats.defn)
        loss = ((statCalc / 50) + 2) * modifier
        self.currentHp -= loss
        print('{} lost {} hp!'.format(self.species, loss))
        print(self)

    def specialDamage(self, pokemon, dmg=0, modifier=1):
        levelMod = (2*self.level/5)+2
        statCalc = (levelMod * dmg * pokemon.stats.spAtk / self.stats.spDefn)
        loss = ((statCalc / 50) + 2) * modifier
        self.currentHp -= loss
        print('{} lost {} hp!'.format(self.species, loss))
        print(self)

    def percentDamage(self, percent=12.5):
        loss = percent * self.totalHp/100
        self.currentHp -= loss
        print('{} lost {} hp!'.format(self.species, loss))
        print(self)

    def percentHealth(self, percent=12.5):
        gain = percent * self.totalHp/100
        self.currentHp += gain
        print('{} gained {} hp!'.format(self.species, gain))
        print(self)

    def healthFromDamage(self, damage=0):
        gain = damage/2
        self.currentHp += gain
        print('{} gained {} hp!'.format(self.species, gain))
        print(self)


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

    def __str__(self):
        return 'hp-{}  atk-{}  defn-{}  spAtk-{}  spDefn-{}  spd-{}'.format(self.hp, self.atk, self.defn, self.spAtk, self.spDefn, self.spd)


class Moveset (object):
    def __init__(self):
        self.one = Move()
        self.two = Move()
        self.three = Move()
        self.four = Move()

    def __str__(self):
        return """{}
        {}
        {}
        {}""".format(self.one, self.two, self.three, self.four)

class Move (object):
    def __init__(self, name='', power=0, accuracy=0, pp=0, type1='', effect=''):
        self.name = name
        self.power = power
        self.accuracy = accuracy
        self.pp = pp
        self.type1 = type1
        self.effect = effect

    def __str__(self):
        return """{}  pow:{}  type:{}  acc:{}  pp:{}  desc:{}""".format(self.name, self.power, self.type1, self.accuracy, self.pp, self.effect)

