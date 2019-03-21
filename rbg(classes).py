import random

class punchline:
    def __init__(self, id, bars, mindBars, points, synergy):
        self.id = id
        self.bars = bars
        self.points = points
        self.synergy = synergy
        self.mindBars = mindBars

class bStats:
    def __init__(self, win, lose, draw):
        self.win = win
        self.lose = lose
        self.draw = draw

class counts:
    def __init__(self, studio, day, goal, battle, lvl, diffBattle):
        self.studio = studio
        self.day = day
        self.goal = goal
        self.battle = battle
        self.lvl = lvl
        self.diffBattle = diffBattle

    def day_skip_check():
        if urRapper.regged == False:
                count.day += 1
                count.battle += 1
        elif count.day - count.battle <= 6:
            count.day += 1
        else:
            print("Иди сначала на батл, чмо. Потом поспишь у своей параши")

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
    def __init__(self, slot1, slot2, slot3, loot):
        self.slot1 = slot1
        self.slot2 = slot2
        self.slot3 = slot3
        self.loot = loot

    def shop_loop(self):
        while True:
            print('\n''Ваше баблишко: ', urRapper.money, '$')
            print('\n''Выберите вещи для покупки!')
            print('1.', self.slot1.name)
            print('2.', self.slot2.name)
            print('3.', self.slot3.name)
            print('0. Выход')

            buy = int(input('Введите число: '))
            if buy == 1:
                if self.slot1 == blank:
                    print("Покупай что-нибудь или сваливай. Нечего тут смотреть просто!")
                else:
                    if urRapper.money >= self.slot1.cost:
                        urRapper.inv.append(self.slot1)
                        urRapper.money -= self.slot1.cost
                        self.slot1 = blank
                    else:
                        print('пошёл в жопу')
            elif buy == 2:
                if self.slot2 == blank:
                    print("Покупай что-нибудь или сваливай. Нечего тут смотреть просто!")
                else:
                    if urRapper.money >= self.slot2.cost:
                        urRapper.inv.append(self.slot2)
                        urRapper.money -= self.slot2.cost
                        self.slot2 = blank
                    else:
                        print('пошёл в жопу')
            elif buy == 3:
                if self.slot3 == blank:
                    print("Покупай что-нибудь или сваливай. Нечего тут смотреть просто!")
                else:
                    if urRapper.money >= self.slot3.cost:
                        urRapper.inv.append(self.slot3)
                        urRapper.money -= self.slot3.cost
                        self.slot3 = blank
            else:
                break

    def shop_pull(self):
        if len(self.loot) == 0:
            self.shop_loop()
        else:
            a = random.randint(0, len(self.loot)-1)
            self.slot1 = self.loot[a]
            self.loot.pop(a)

            b = random.randint(0, len(self.loot)-1)
            self.slot2 = self.loot[b]
            self.loot.pop(b)

            c = random.randint(0, len(self.loot)-1)
            self.slot3 = self.loot[c]
            self.loot.pop(c)
            self.shop_loop()

class char:
    def __init__(self, name, inv, bars, money, genres, fame, lvl, regged):
        self.name = name
        self.inv = inv
        self.bars = bars
        self.money = money
        self.genres = genres
        self.fame = fame
        self.lvl = lvl
        self.regged = regged

    def statCheck(self):
        print('===========================')
        print('Ник: ', self.name)
        print('Уровень: ', self.lvl, 'из', count.lvl)
        print('Баблишко: ', self.money, '$')
        print('Известность: ', self.fame)
        if self.regged == True:
            print('Батловый статус: Зарегистрирован (Через ', count.diffBattle - (count.day - count.battle), 'дней)')
            print('===========================''\n')
        else:
            print('Батловый статус:  Не зарегистрирован')
            print('===========================''\n')

count = counts(0, 0, 5, 0, 10, 7)

punch1 = punchline(1, "У меня есть Гуччи глок", "", 5, [2])
punch2 = punchline(2, "Ты - прилизаный грибок", "", 5, [1])
punch3 = punchline(3, "Гуччи бенкролл - это смысл жизни", "", 5, [4])
punch4 = punchline(4, "Я не ЧСВ, просто нет корысти", "", 5, [3])
punch5 = punchline(5, "Новый ламборгини, новые цацки", "", 5, [6])
punch6 = punchline(6, "Моя жизнь - Каноха, а ты в ней Акацке", "", 5, [5])
punch7 = punchline(7, "Потерял все признаки туриста", "", 5, [8])
punch8 = punchline(8, "Теперь гуляю по Европе, будто призрак коммунизма", "", 5, [7])

item1 = item(100, "Gucci Glock", [punch1, punch2], 5, 100)
item2 = item(101, "New NewLamborgini", [punch3, punch4], 5, 125)
item3 = item(102, "Gucci Bankroll", [punch5, punch6], 5, 200)
blank = item(999, "Пусто", [], 0, 0)

shop1 = shop(blank, blank, blank, [item1, item2, item3])

urEnemy = enemy(999, "", [], 1)
enemy1 = enemy(50, "Yung Leo", [punch1, punch2], 1)
enemy2 = enemy(51, "Fifty draem", [punch3, punch4], 1)
enemy3 = enemy(52, "Creeper95", [punch5, punch6], 1)
enemy4 = enemy(53, "Lichinus", [punch7, punch8], 1)

urRapper = char('urName', [item1, item2], [punch7, punch8], 1120, [], 0, 1, False)

class possRange:
    def __init__(self, itemsR, possR):
        self.itemsR = itemsR
        self.possR = possR

    def possEnemy(self):
        for it in self.itemsR:
            if it.lvl == urRapper.lvl:
                self.possR.append(it)

possibleEnemy = possRange([enemy1, enemy2, enemy3, enemy4], [])

class round:
    def __init__(self, enemy, urRnd, urTotalPoints, enRnd, enTotalPoints, possEnemy ):
        self.enemy = enemy
        self.urRnd = urRnd
        self.urTotalPoints = urTotalPoints
        self.enRnd = enRnd
        self.enTotalPoints = enTotalPoints

    rBars = urRapper.bars.copy()
    eBars = urEnemy.bars.copy()

    def urRound(self):
        matchBars_1 = []
        matchBars_2 = []
        iBars = 1
        for bar in rBars:
            matchBars_1.append(iBars)
            matchBars_2.append(bar)
            print(" >[", iBars, "]: ", bar.bars)
            iBars += 1
        global matchBars
        matchBars = list(zip(matchBars_1, matchBars_2))

        ansBars = int(input("Выбери одну из твоих строчек: "))
        if ansBars == matchBars[ansBars - 1][0]:
            self.urRnd.append(matchBars[0][1])
            rBars.pop(matchBars[ansBars - 1][0] - 1)

    def urSyn(self):
        self.urTotalPoints = self.urRnd[0].points + self.urRnd[1].points
        if self.urRnd[0].id in self.urRnd[1].synergy:
            self.urTotalPoints *= 1.5
            print("Ого, отличная комбинация строчек!")
        self.urRnd.clear()

    def enRound(self):
        eRandom = random.randint(0, len(urEnemy.bars)-1)
        self.enRnd.append(eBars.bars[eRandom])
        print(eBars[eRandom].bars)
        eBars.pop(enemy.bars[eRandom])

    def enSyn(self):
        self.enTotalPoints = self.enRnd[0].points + self.enRnd[1].points
        if self.enRnd[0].id in self.enRnd[1].synergy:
            self.enTotalPoints *= 1.5
            print("Ого, смотри какая у него отличная комбинация строчек! Ты реально обосрался...")
        self.enRnd.clear()

def battle():
    pass

while True:
    print('\n''===========================')
    print('Настал', count.day, 'день... Что будем делать сегодня? ;)')
    print('===========================''\n')
    urRapper.statCheck()

    print(' >1. Записаться на Рэп баттл')
    print(' >2. Отдыхать')
    print(' >3. Пойти в магазин')
    print(' >4. Арендовать студию звукозаписи')
    print(' >5. Придумать новые строчки')
    print(' >6. Выйти на улицу''\n')
    daily_action = int(input('Ну что будем делать?: '))

    if daily_action == 1:
        if urRapper.regged == False:
            possibleEnemy.possEnemy()
            global enemy_roll
            enemy_roll = random.randint(0, len(possibleEnemy.possR)-1)
            urEnemy = possibleEnemy.possR[enemy_roll]
            count.battle = count.day
            print('\n'"Вы зарегестрировались на батл. Ваш батл с ", urEnemy.name, "состоится через 7 дней")
            urRapper.regged = True

        elif counts.day - counts.battle >= 7:
            print()
            print("=> А Ф И Ш А <=".center(40, "-"))
            print(urRapper.name.center(40))
            print("X".center(40))
            print(urEnemy.name.center(40))
            battle()
            urRapper.regged = False
            count.battle = 0

        elif urRapper.regged == True:
            print('\n'"Молодой, чо приперся? Твой батл с ", urEnemy.name, "через ", count.diffBattle - (count.day - count.battle), "дней"'\n')

    elif daily_action == 2:
        pass

    elif daily_action == 3:
        shop1.shop_pull()

    else:
        quit()
