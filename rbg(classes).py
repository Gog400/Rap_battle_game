class punchline:
    def __init__(self, id, bars, points, synnergy):
        self.id = id
        self.bars = bars
        self.points = points
        self. synnergy = synnergy

class count:
    def __init__(self, win, lose, draw):
        self.win = win
        self.lose = lose
        self.draw = draw

class bStats:
    def __init__(self, studio, day, goal, battle):
        self.studio = studio
        self.day = day
        self.goal = goal
        self.battle = battle

class enemy:
    def __init__(self, id, name, bars, lvl):
        self.id = id
        self.name = name
        self.bars = bars
        self.lvl = lvl

class item:
    def __init__(self, id, name, bars, points, cost):
        self.id = id
        self.name = name
        self.bars = bars
        self.points = points
        self.cost = cost

class shop:
    def __init__(self, slot1, slot2, slot3):
        self.slot1 = slot1
        self.slot2 = slot2
        self.slot3 = slot3

class char:
    def __init__(self, inv, bars, money, genres, fame, lvl, regged):
        self.inv = inv
        self.bars = bars
        self.money = money
        self.genres = genres
        self.fame = fame
        self.lvl = lvl
        self.regged = regged
