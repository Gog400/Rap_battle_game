import random

class counts:
    def __init__(self, studio, day, goal, battle, lvl, diffBattle, hype, urTotalPoints, enTotalPoints):
        self.studio = studio
        self.day = day
        self.goal = goal
        self.battle = battle
        self.lvl = lvl
        self.diffBattle = diffBattle
        self.hype = hype
        self.urTotalPoints = urTotalPoints
        self.enTotalPoints = enTotalPoints

count = counts(0, 0, 5, 0, 10, 7, 0, 0, 0)


class punchline:
    def __init__(self, id, bars, mindBars, points, synergy):
        self.id = id
        self.bars = bars
        self.points = points
        self.synergy = synergy
        self.mindBars = mindBars

punch1 = punchline(1, "У меня есть Гуччи глок", "", 5, [2])
punch2 = punchline(2, "Ты - прилизаный грибок", "", 5, [1])

punch3 = punchline(3, "Гуччи бенкролл - это смысл жизни", "", 5, [4])
punch4 = punchline(4, "Я не ЧСВ, просто нет корысти", "", 5, [3])

punch5 = punchline(5, "Новый ламборгини, новые цацки", "", 5, [6])
punch6 = punchline(6, "Моя жизнь - Каноха, а ты в ней Акацке", "", 5, [5])

punch7 = punchline(7, "Потерял все признаки туриста", "", 5, [8])
punch8 = punchline(8, "Теперь гуляю по Европе, будто призрак коммунизма", "", 5, [7])

punch9 = punchline(9, "Твоя жопа прошита, как и мой ИксБокс", "", 5, [10])
punch10 = punchline(10, "У тебя бомбит, ведь я здесь босс", "", 5, [9])

punch11 = punchline(11, "Я тебе кипу тку, на плите кипятку", "", 5, [12])
punch12 = punchline(12, "Нагреваю, заливаю в рот тебе: keep it cool!", "", 5, [11])

punch13 = punchline(13, "Ты, по-моему, грозился мне драками, но куш мой", "", 5, [14])
punch14 = punchline(14, "Я помою свой член в твоей раковине ушной", "", 5, [13])

punch15 = punchline(15, "Твои слова это пиздёж и враки", "", 5, [16])
punch16 = punchline(16, "Ты как глисты у Обамы - ты живешь в бараке", "", 5, [15])

punch17 = punchline(17, "Это ноль-ноль-восемь, помни памятную дату", "", 5, [18])
punch18 = punchline(18, "Мы вас разносим, будто в цирке сахарную вату", "", 5, [17])

punch19 = punchline(19, "Твоя карьера, как тетрадка - серая и краткая", "", 5, [20])
punch20 = punchline(20, 'Её первая буква "x", последняя - и-краткое', "", 5, [19])

punch21 = punchline(21, "Ты не с улицы парень, ты просто суицидален", "", 5, [22])
punch22 = punchline(22, "От того, что вы мне двадцать первый целуете палец", "", 5, [21])

punch23 = punchline(23, "Ты читаешь про богов, про саги и легенды", "", 5, [24])
punch24 = punchline(24, "Перестань выпендриваться, сын, ты сосал на weekend'ах", "", 5, [23])

punch25 = punchline(25, "Я пуленепробиваемый, в буре не потомляемый", "", 5, [26])
punch26 = punchline(26, "Дурень, тебя пинали мы! Хули вы залупались, блин", "", 5, [25])

punch27 = punchline(27, "Вот и сорвана резьба, думал замес, будет резня", "", 5, [28])
punch28 = punchline(28, "Помни, одна моя пешка пизже твоего ферзя", "", 5, [27])

punch29 = punchline(29, "В тебе грайма нет, бро, ты - говноед", "", 5, [30])
punch30 = punchline(30, "Твой флоу рогатка - мой арбалет", "", 5, [29])


class item:
    def __init__(self, id, name, bars, points, cost):
        self.id = id
        self.name = name
        self.bars = bars
        self.points = points
        self.cost = cost

item1 = item(100, "Gucci Glock", [punch1, punch2], 5, 100)
item2 = item(101, "New NewLamborgini", [punch3, punch4], 5, 125)
item3 = item(102, "Gucci Bankroll", [punch5, punch6], 5, 200)
blank = item(999, "Пусто", [], 0, 0)


class char:
    def __init__(self, name, inv, bars, songlist, money, genres, fame, lvl, regged, beats, exp):
        self.name = name
        self.inv = inv
        self.bars = bars
        self.songlist = songlist
        self.money = money
        self.genres = genres
        self.fame = fame
        self.lvl = lvl
        self.regged = regged
        self.beats = beats
        self.exp = exp

    def statCheck(self):
        if self.exp == self.lvl*10:
            self.exp -= self.lvl*10
            self.lvl += 1
        print('===========================')
        print('Ник: ', self.name)
        print('Уровень: ', self.lvl, 'из', count.lvl, '[', self.exp, '/', self.lvl*10, ']')
        print('Баблишко: ', self.money, '$')
        print('Известность: ', self.fame)
        if self.regged == True:
            print('Батловый статус: Зарегистрирован (Через ', count.diffBattle - (count.day - count.battle), 'дней)')
            print('===========================''\n')
        else:
            print('Батловый статус:  Не зарегистрирован')
            print('===========================''\n')

urRapper = char('urName', [item1, item2], [punch25, punch26, punch27, punch28, punch29, punch30], [], 1120, [], 0, 1, False, [], 0)


class track:
    hype = int(urRapper.fame/(count.diffBattle*3))
    def __init__(self, bars, points, rating, hype, name, authName, genre):
        self.bars = bars
        self.points = points
        self.rating = rating
        self.hype = hype
        self.name = name
        self.authName = authName
        self.genre = genre

    def trackIncome(self):
        urRapper.fame += (self.points / self.rating) * self.hype
        global icn
        icn = (urRapper.fame / (count.diffBattle / 2)) * self.hype
        urRapper.money += icn

    def ratingSort(self):
        trackRange.itemsR.extend(trackRange.possR)
        trackRange.itemsR.sort(key=self.points)

    def hypeIncome(self):
        a = count.hype + count.diffBattle * 2 - count.day
        if count.day <= count.hype + count.diffBattle * 2:
            self.hype = -0.5*a^2 + count.diffBattle * 2
            count.hype += 1
        else:
            self.hype = 0

    def songlistIncome():
        for tr in urRapper.songlist:
            tr.trackIncome()

    def day_skip_check():
        if urRapper.regged == False:
                count.day += 1
                count.battle += 1
                track.songlistIncome()
        elif count.day - count.battle <= 6:
            count.day += 1
            track.songlistIncome()
        else:
            print("Иди сначала на батл, чмо. Потом поспишь у своей параши")

class beat:
    def __init__(self, name):
        self.name = name

beat1 = beat("Grime beat")
beat2 = beat("Minimalistic beat")
beat3 = beat("Trap beat")
beat4 = beat("Old school beat")

class genre:
    def __init__(self, name, beatCombo):
        self.name = name
        self.beatCombo = beatCombo

genre1 = genre("Grime", beat1)
genre2 = genre("Cloud rap", beat2)
genre3 = genre("New school", beat3)
genre4 = genre("Old school", beat4)

class bStats:
    def __init__(self, wins, lose, draw):
        self.wins = wins
        self.lose = lose
        self.draw = draw

class enemy:
    def __init__(self, id, name, bars, lvl):
        self.id = id
        self.name = name
        self.bars = bars
        self.lvl = lvl

urEnemy = enemy(999, "", [], 1)
enemy1 = enemy(50, "Yung Leo", [punch1, punch2, punch3, punch4, punch5, punch6], 1)
enemy2 = enemy(51, "Fifty draem", [punch7, punch8, punch9, punch10, punch11, punch12], 1)
enemy3 = enemy(52, "Creeper95", [punch13, punch14, punch15, punch16, punch17, punch18], 1)
enemy4 = enemy(53, "Lichinus", [punch19, punch20, punch21, punch22, punch23, punch24], 1)


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
            print('1.', self.slot1.cost, "$ -", self.slot1.name)
            print('2.', self.slot2.cost, "$ -", self.slot2.name)
            print('3.', self.slot3.cost, "$ -", self.slot3.name)
            print('0. Выход')

            buy = int(input('Введите число: '))
            if buy == 1:
                if self.slot1 == blank:
                    print("Покупай что-нибудь или сваливай. Нечего тут смотреть просто!")
                else:
                    if urRapper.money >= self.slot1.cost:
                        urRapper.inv.append(self.slot1)
                        urRapper.bars.append(self.slot1.bars[0])
                        urRapper.bars.append(self.slot1.bars[1])
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
                        urRapper.bars.append(self.slot2.bars[0])
                        urRapper.bars.append(self.slot2.bars[1])
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
                        urRapper.bars.append(self.slot3.bars[0])
                        urRapper.bars.append(self.slot3.bars[1])
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

shop1 = shop(blank, blank, blank, [item1, item2, item3])


class possRange:
    def __init__(self, itemsR, possR):
        self.itemsR = itemsR
        self.possR = possR

    def possEnemy(self):
        for it in self.itemsR:
            if it.lvl == urRapper.lvl:
                self.possR.append(it)

enemyRange = possRange([enemy1, enemy2, enemy3, enemy4], [])
genreRange = possRange([genre1, genre2, genre3], []) ##!!!!!!!
beatRange = possRange([beat1, beat2, beat3], []) ##!!!!!!!
trackRange = possRange([], [])
possTrackInd = possRange([enemy1, enemy2, enemy3, enemy4], ['Dick', 'Cock', 'Max'])

class round:
    def __init__(self, urRnd, enRnd, numCounter, barCounter):
        self.urRnd = urRnd
        self.enRnd = enRnd
        self.numCounter = numCounter
        self.barCounter = barCounter

    def urRound(self):
        for it in range(2):
            self.numCounter.clear()
            self.barCounter.clear()
            iBars = 1
            for bar in rBars:
                self.numCounter.append(iBars)
                self.barCounter.append(bar)
                print(" >[", iBars, "]: ", bar.bars)
                iBars += 1

            ansBars = int(input("Выбери одну из доступных строчек: "))
            if ansBars == self.numCounter[ansBars - 1]:
                self.urRnd.append(self.barCounter[ansBars - 1])
                rBars.remove(self.barCounter[ansBars - 1])
        print('\n''Ваш раунд: ')
        print(self.urRnd[0].bars)
        print(self.urRnd[1].bars)

    def urSyn(self):
        if self.urRnd[0].id in self.urRnd[1].synergy:
            count.urTotalPoints += (self.urRnd[0].points + self.urRnd[1].points)*2
            print('\n'"-Ого, отличная комбинация строчек! (У вас", count.urTotalPoints, 'очков)')
        else:
            count.urTotalPoints += (self.urRnd[0].points + self.urRnd[1].points)
            print('\n'"-В следующий раз постарайся зарифмовать сторчки! (У вас", count.urTotalPoints, 'очков)')
        self.urRnd.clear()

    def enRound(self):
        print('\n'"Раунд вашего противника: ")
        for it in range(2):
            eRandom = random.randint(0, len(eBars)-1)
            self.enRnd.append(eBars[eRandom])
            print(eBars[eRandom].bars)
            eBars.remove(eBars[eRandom])
        print()

    def enSyn(self):
        if self.enRnd[0].id in self.enRnd[1].synergy:
            count.enTotalPoints += (self.enRnd[0].points + self.enRnd[1].points)*2
            print('\n'"-Ого, смотри какая у него отличная комбинация строчек! Ты реально обосрался... (У него", count.enTotalPoints, 'очков)')
        else:
            count.enTotalPoints += (self.enRnd[0].points + self.enRnd[1].points)
            print("Ахаха, этот чел походу не знает, что строчки можно рифмовать! (У него", count.enTotalPoints, 'очков)')
        self.enRnd.clear()

    def battleResults(self):
        if count.urTotalPoints > count.enTotalPoints:
            print("Красава, я всегда знал, что у тебя есть талант! -Сказал Перфоратор и протянул вам ваш обещанный гонорар")
            print("Приходи еще, мы найдем для тебя кого-то по сильнее")
            print("Известность повышена: ", urRapper.fame, "->", urRapper.fame + urEnemy.lvl * 30)
            print("Деньги получены: ", urRapper.money, "->", urRapper.money + urEnemy.lvl * 30)
            urRapper.fame += urEnemy.lvl * 30
            urRapper.money += urEnemy.lvl * 100
            urRapper.exp += urEnemy.lvl* 2
        elif self.urTotalPoints == self.enTotalPoints:
            print("Я думал ты норм пацан, а в итоге ты просто дефолтный челик... -Сказал Постмодернатор и направился к бару")
            urRapper.exp += urEnemy.lvl
        else:
            print("После батла к вам вышел Псевдоинтеллектуатор и публично вас унизил")
            print("Известность понижена: ", urRapper.fame, "->", urRapper.fame - urEnemy.lvl * 15)
            urRapper.fame -= urEnemy.lvl * 15
        count.urTotalPoints = 0
        count.enTotalPoints = 0

    def battle():
                round1.urRound()
                round1.urSyn()
                round1.enRound()
                round1.enSyn()
                round2.urRound()
                round2.urSyn()
                round2.enRound()
                round2.enSyn()
                round3.urRound()
                round3.urSyn()
                round3.enRound()
                round3.enSyn()
                round3.battleResults()

round1 = round([], [], [], [])
round2 = round([], [], [], [])
round3 = round([], [], [], [])

class xActions:
    def __init__(self, pr1, pr2, pr3):
        self.pr1 = pr1
        self.pr2 = pr2
        self. pr3 = pr3

    def Original_printing1(self):
        orig = random.randint(0, len(self.pr1.prints)-1)
        print(self.pr1.prints[orig])

    def Original_printing2(self):
        orig = random.randint(0, len(self.pr2.prints)-1)
        print(self.pr2.prints[orig])

    def Original_printing3(self):
        orig = random.randint(0, len(self.pr3.prints)-1)
        print(self.pr3.prints[orig])

class action:
    def __init__(self, prints):
        self.prints = prints

uni1 = action(['Ловя приход от университетских голубцов с яйцом, вы открываете новый жанр',
                'Сидя в туалете, пукая, вы придумали новую ритмику. Новый жанр открыт',
                'Царапая вилкой по тарелке, вы услышали новый звук и придумали новый жанр'])

uni2 = action(['От голода в университетской столовке у вас происходит инсульт и вы забываете жанр',
                'Подскальзнувишь, вы разбили туалетную плитку и забыли жанр',
                'Вы отупели настолько, что просто забыли жанр'])

uni3 = action(['Вы проучились весь день и даже получили 5 по математике.',
                'Нормальный денёк сегодня был, эхх',
                'Просидя 5 пар вы осознаёте, что учебный день окончился и решаете пойти домой'])

fac1 = action(['Прораб, отсутствовавший в течении 6 месяцев, рассказал о каком-то "топ-донатере". На радостях, прораб даёт 1% вам.',
                '"Нихуево ты отбатрачил сегодня!" -Сказал прараб и дал вам вашу зарплату',
                'С ухмылкой на лице, вы крадёте туалетную бумагу из туалета, с мыслью потом ее продать. Вы чувствуете профитанычи'])

fac2 = action(['Из-за некого "бана" основной заработок прараба прекратился. Собственно, поэтому он и задержал вам зарплату до лучших дней, а также одолжил несколько долларов.',
                'Сегодня вы сломали станок. Вас оштрафовали на 40 Долларов',
                'С криками "СЮДА, ШНЫРКУРЬЕРЫЧ!!!" вас оглушает прараб. На следующее утро вы просыпаетесь с отсутствующими 40 Долларами'])

fac3 = action(['Я пошутил, ничего не произошло. Вы отработали смену и вас не уволили.',
                'Прораб отказался вам платить зарплату из-за вашего смешного "реперского" внешнего вида',
                'Вы хорошо поспали сегодня. Пора идти домой'])

uniAction = xActions(uni1, uni2, uni3)
facAction = xActions(fac1, fac2, fac3)

while True:
    print('\n''===========================')
    print('Настал', count.day, 'день... Что будем делать сегодня? ;)')
    print('===========================''\n')
    urRapper.statCheck()

    print(' >1. Записаться на Рэп баттл')
    print(' >2. Отдыхать')
    print(' >3. Пойти в магазин')
    print(' >4. Арендовать студию звукозаписи')
    print(' >5. Выйти на улицу''\n')
    daily_action = int(input('Ну что будем делать?: '))

    if daily_action == 1:
        if urRapper.regged == False:
            enemyRange.possEnemy()
            global enemy_roll
            enemy_roll = random.randint(0, len(enemyRange.possR)-1) #len(enemyRange.possR)-1
            urEnemy = enemyRange.possR[enemy_roll]
            count.battle = count.day
            print('\n'"Вы зарегестрировались на батл. Ваш батл с ", urEnemy.name, "состоится через 7 дней")
            urRapper.regged = True

        elif count.day - count.battle >= count.diffBattle:
            print()
            print("=> А Ф И Ш А <=".center(40, "-"))
            print(urRapper.name.center(40))
            print("X".center(40))
            print(urEnemy.name.center(40))
            global eBars
            global rBars
            eBars = urEnemy.bars.copy()
            rBars = urRapper.bars.copy()
            round.battle()
            urRapper.regged = False
            count.battle = 0

        elif urRapper.regged == True:
            print('\n'"Молодой, чо приперся? Твой батл с ", urEnemy.name, "через ", count.diffBattle - (count.day - count.battle), "дней"'\n')

    elif daily_action == 2:
        track.day_skip_check()

    elif daily_action == 3:
        track.day_skip_check()
        shop1.shop_pull()

    elif daily_action == 4:
        track.day_skip_check()
        while True:
            print('\n''===========================')
            print('Добро пожаловать в студию звукозаписи!''\n')
            print(' >1. Записать песню')
            print(' >2. Посмотреть топ чарты')
            print(' >3. Заказать новый бит')
            print(' >4. Посмотреть свои навыки')
            print(' >0. Выход')
            studio_action = int(input('Введите число: '))
            if studio_action == 1:
                round1.urRound()
                round1.urSyn()
            elif studio_action == 2:
                track.ratingSort()
                sng = 0
                for song in trackRange:
                    print('(', sng + 1, ')', trackRange[sng].name)

            elif studio_action == 3:
                print('\n''===========================')
                print('Вы решили пополнить коллекцию своих битов!''\n')
                print(' >1. Заказать у кореша(бесплатно)')
                print(' >2. Заказать у норм битмейкера(100$)')
                print(' >0. Назад')

                beat_action = int(input('Введите число: '))
                if beat_action == 1:
                    if beatRange.itemsR != []:
                        beat_roll = random.randint(0, len(beatRange.itemsR)-1)
                        beatRange.possR.append(beatRange.itemsR[beat_roll])
                        urRapper.beats.append(beatRange.itemsR[beat_roll])
                        print('Кореш вам сделал ', beatRange.itemsR[beat_roll].name)
                        beatRange.itemsR.pop(beat_roll)

                    else:
                        print(' >Вы изучили все возможные биты')

                elif beat_action == 2:
                    if beatRange.itemsR != []:
                        print('Вам жопа!')
                    else:
                        print('\n'' >Вы изучили все возможные биты')

                else:
                    pass

            elif studio_action == 4:
                print('\n''===========================')
                print('Ваши жанры: ')
                for i in urRapper.genres:
                    print(" -", i.name)

                print('\n''===========================')
                print('Ваши биты: ')
                for i in urRapper.beats:
                    print(" -", i.name)

            else:
                break

    elif daily_action == 5:

        print('\n''Вы вышли на улицу. Тут холодно.''\n')
        print(' >1. Идти на пары')
        print(' >2. Идти на завод')
        print(' >3. Зайти обратно домой')
        street_action = int(input('Куда направляемся: '))

        while True:
            if street_action == 1:
                track.day_skip_check()
                print('\n''Вы пошли на пары. Там с вами кое-что произошло.')
                university_roll = random.choices([0, 1, 2], weights = [30, 20, 50])

                if university_roll == [0]:
                    if genreRange.itemsR != []:
                        genre_roll = random.randint(0, len(genreRange.itemsR)-1)
                        genreRange.possR.append(genreRange.itemsR[genre_roll])
                        urRapper.genres.append(genreRange.itemsR[genre_roll])
                        print('===========================')
                        xActions.Original_printing1(uniAction)
                        print("Жанр получен: ", genreRange.itemsR[genre_roll].name)
                        genreRange.itemsR.pop(genre_roll)
                        break
                    else:
                        print('Ёба, нафиг ты сюда ходишь? Ты тут всё уже изучил')

                elif university_roll == [1]:
                    if urRapper.genres != []:
                        genre_roll = random.randint(0, len(urRapper.genres)-1)
                        genreRange.itemsR.append(urRapper.genres[genre_roll])
                        print('===========================')
                        xActions.Original_printing2(uniAction)
                        print("Жанр потерян: ", urRapper.genres[genre_roll].name)
                        urRapper.genres.remove(urRapper.genres[genre_roll])
                        genreRange.possR.pop(genre_roll)

                        break
                    else:
                        print('Ёбать... Ты настолько тупой, что тебе нечего забывать')

                elif university_roll == [2]:
                    print('===========================')
                    xActions.Original_printing3(uniAction)
                    print("Опыт увеличен: ", urRapper.exp, "->", urRapper.exp * 1.1)
                    urRapper.exp *= 1.1
                    break

            elif street_action == 2:
                track.day_skip_check()
                print('\n''Вы пошли на завод. Нормально так собрали мебель из IKEA, но кое-что с вами произошло.')
                factory_roll = random.choices([0, 1, 2], weights = [30, 20, 50])

                if factory_roll == [0]:
                    print('===========================')
                    xActions.Original_printing1(facAction)
                    print("Деньги получены: ", urRapper.money, "->", urRapper.money + 100)
                    urRapper.money += 100
                    break

                elif factory_roll == [1]:
                    print('===========================')
                    xActions.Original_printing2(facAction)
                    print("Деньги потеряны: ", urRapper.money, "->", urRapper.money - 40)
                    urRapper.money -= 40
                    break

                elif factory_roll == [2]:
                    print('===========================')
                    xActions.Original_printing3(facAction)
                    print("Деньги получены: ", urRapper.money, "->", urRapper.money + 10)
                    break

            elif street_action == 3:
                print('Вы решили вернуться домой. На улице слишком холодно')
                break

    else:
        quit()
