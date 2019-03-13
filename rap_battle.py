import random
##словари

battle_stats = {
    'win': 0,
    'lose': 0,
    'draw': 0,
}
counts = {
    'studio': 0,
    'day': 0,
    'goal': 5,
    'battle': 0
}
punchline_1 = {
    'id': 1,
    'bars': 'У меня есть Гуччи глок, ты - прилизаный грибок',
    'mind_bars': 'У меня есть ~$%@&*! глок, ты - прилизаный $%@#&!~ок',
    'theme': 'gangsta',
    'points': 5,
    'synY': 1,
    'synergy': [2]
}
punchline_2 = {
    'id': 2,
    'bars': 'Гуччи бенкролл - это смысл жизни. Я не ЧСВ, просто нет корысти',
    'mind_bars': '?%№@#& @$№?*! - это смысл жизни. Я не ЧСВ, просто нет %№?@',
    'theme': 'million',
    'points': 5,
    'synY': 2,
    'synergy': [1]
}
punchline_3 = {
    'id': 3,
    'bars': 'Новый ламборгини, новые цацки. Моя жизнь - Каноха, а ты в ней Акацке',
    'mind_bars': 'Новый %@#$%?, новые цацки. Моя жизнь - Каноха, а ты в ней %$#@&№!',
    'theme': 'minecraft',
    'points': 5,
}
punchline_4 = {
    'id': 4,
    'bars': 'Я биссексуал',
    'theme': 'elephant',
    'points': 5
}
punchline_5 = {
    'id': 5,
    'bars': 'Потерял все признаки туриста, теперь гуляю по Европе, будто призрак коммунизма',
    'theme': 'elephant',
    'points': 5
}
punchline_6 = {
    'id': 6,
    'bars': 'Я тебе кипу тку, на плите кипятку нагреваю, заливаю тебе в рот - Keep it cool!',
    'theme': 'elephant',
    'points': 5
}
punchline_7 = {
    'id': 7,
    'bars': 'Занимаюсь спортом я',
    'theme': 'elephant',
    'points': 5
}
punchline_8 = {
    'id': 8,
    'bars': 'Твоя жопа прошита, как и мой ИксБокс. У тебя бомбит, ведь я здесь босс',
    'theme': 'elephant',
    'points': 5
}
punchline_9 = {
    'id': 9,
    'bars': 'Голые шреки и ослы',
    'theme': 'elephant',
    'points': 5
}
punchline_10 = {
    'id': 10,
    'bars': 'Как бывает приятно на природе',
    'theme': 'elephant',
    'points': 5
}
punchline_11 = {
    'id': 11,
    'bars': 'Деньги мне плати',
    'theme': 'elephant',
    'points': 5
}
punchline_12 = {
    'id': 12,
    'bars': 'Опа опа опа-па',
    'theme': 'elephant',
    'points': 5
}
punchline_13 = {
    'id': 13,
    'bars': 'От тебя пахнет дерьмом',
    'theme': 'elephant',
    'points': 5
}
punchline_14 = {
    'id': 14,
    'bars': 'Быть правым с зелеными наклонностями - как быть другом гитлера',
    'theme': 'elephant',
    'points': 5
}
punchline_15 = {
    'id': 15,
    'bars': 'Как эти комбо сраные сделать',
    'theme': 'elephant',
    'points': 5
}
punchline_16 = {
    'id': 16,
    'bars': 'И баффы еще...',
    'theme': 'elephant',
    'points': 5
}

yungleo = {
    'id': 50,
    'name': 'Yung Leo',
    'bars': [punchline_5, punchline_6, punchline_7],
    'lvl': 1
}
fiftydraem = {
    'id': 51,
    'name': 'Fifty Draem',
    'bars': [punchline_8, punchline_9, punchline_10],
    'lvl': 1
}
creeper = {
    'id': 52,
    'name': 'Kriper95',
    'bars': [punchline_11, punchline_12, punchline_13],
    'lvl': 1
}
lich = {
    'id': 53,
    'name': 'Lichinus',
    'bars': [punchline_14, punchline_15, punchline_16],
    'lvl': 1
}
GucciGlock = {
    'id': '100',
    'name': 'GucciGlock',
    'bars': 'У меня есть Гуччи глок, ты - прилизаный грибок',
    'points': 5,
    'cost': 50
}
GucciBankroll = {
    'id': '101',
    'name': 'GucciBankroll',
    'bars': 'Гуччи бенкролл - это смысл жизни. Я не ЧСВ, просто нет корысти',
    'points': 5,
    'cost': 75
}
NewLamborgini = {
    'id': '102',
    'name': 'NewLamborgini',
    'bars': 'Новый ламборгини, новые цацки. Моя жизнь - Каноха, а ты в ней Акацке',
    'points': 5,
    'cost': 320
}
enemies = {
    '1': [yungleo, fiftydraem, creeper, lich]
}
blank = {
    'id': '999',
    'name': 'none',
    'bars': 'none',
    'cost': 0
}
shop = {
    'slot1': blank,
    'slot2': blank,
    'slot3': blank
}
rap = {
    'name': 'Рэп',
    'synergy': [2,7],
    'synY': '1'
}
grime = {
    'name': 'Грайм',
    'synergy': [1],
    'synY': '2'
}
trap = {
    'name': 'Трэп Музыка',
    'synergy': [4],
    'synY': '3'
}
minimalistic = {
    'name': 'Минималистик',
    'synergy': [3],
    'synY': '4'
}
jumpup = {
    'name': 'Джамп-Ап',
    'synergy': [6],
    'synY': '5'
}
drum = {
    'name': 'Дрэм',
    'synergy': [5],
    'synY': '6'
}
diss = {
    'name': 'Дисс',
    'synergy': [1],
    'synY': '7'
}
pop = {
    'name': 'Поп',
    'synergy': [1],
    'synY': '9'
}
reggie = {
    'name': 'Рэгги',
    'synergy': [1,3,4,5,6,7,9],
    'synY': '10'
}
music_addons = {
    'genres': [rap, grime, trap, minimalistic, jumpup, drum, diss],
}
knowledge_shop = {
    'slot1': 'blank'
}
urRapper = {
    'inv': [],
    'bars': [],
    'bg': 'none',
    'title': 'none',
    'money': 3000,
    'genres': [],
    'fame': 0,
    'lvl': '1',
    'regged': False
}

def battle():
    global r1Y
    global r2Y
    global r3Y
    global r1E
    global r2E
    global r3E
    global r1YS
    global r2YS
    global r3YS
    global r1ES
    global r2ES
    global r3ES
    global rBars
    print()
    print("Выбери одну из твоих строчек: ")
    rBars = urRapper['bars'].copy()
    r1Y = []
    r2Y = []
    r3Y = []
    r1E = []
    r2E = []
    r3E = []
    r1YS = []
    r2YS = []
    r3YS = []
    r1ES = []
    r2ES = []
    r3ES = []
    battle_bars()
    r1Ybattle()
    battle_bars()
    r1Ybattle()
    r1SynY()
    print('\n'"Раунд противника: ")
    r1Ebattle()
    r1Ebattle()
    print()
    if len(r1Y) and len(r1E) == 2:
        battle_bars()
        r2Ybattle()
        battle_bars()
        r2Ybattle()
        print('\n'"Раунд противника: ")
        r2Ebattle()
        r2Ebattle()
        print()
        if len(r2Y) and len(r2E) == 2:
            battle_bars()
            r3Ybattle()
            battle_bars()
            r3Ybattle()
            print('\n'"Раунд противника: ")
            r3Ebattle()
            r3Ebattle()
            print()
            if len(r3Y) and len(r3E) == 2:
                battleSummY = total1Y + total2Y + total3Y
                battleSummE = total1E + total2E + total3E
                if battleSummY > battleSummE:
                    print("You win!")
                    urRapper['fame'] += enemy['lvl'] * 15
                    urRapper['money'] += enemy['lvl'] * 100
                elif battleSummY == battleSummE:
                    print("Sosi jopy")
                else:
                    print("You lose")
                    urRapper['fame'] -= enemy['lvl'] * 15
def r1SynY():
    global total1Y
    if r1YS[0]['synY'] in r1YS[1]['synergy']:
        print("Ого, отличная комбинация строчек!")
        total1Y = sum(r1Y)
        total1Y *= 1.5
    else:
        total1Y = sum(r1Y)

def r2SynY():
    global total2Y
    if r2YS[0]['synY'] in r2YS[1]['synergy']:
        print("Ого, отличная комбинация строчек!")
        total2Y = sum(r2Y)
        total2Y *= 1.5
    else:
        total2Y = sum(r2Y)

def r3SynY():
    global total3Y
    if r3YS[0]['synY'] in r3YS[1]['synergy']:
        print("Ого, отличная комбинация строчек!")
        total3Y = sum(r3Y)
        total3Y *= 1.5
    else:
        total3Y = sum(r3Y)

def r1SynE():
    global total1E
    if r1ES[0]['synY'] in r1ES[1]['synergy']:
        print("Ого, смотри какая у него отличная комбинация строчек! Ты реально обосрался...")
        total1E = sum(r1E)
        total1E *= 1.5
    else:
        total1E = sum(r1E)

def r2SynE():
    global total2E
    if r2ES[0] == r2ES[1]:
        print("Ого, смотри какая у него отличная комбинация строчек! Ты реально обосрался...")
        total2E = sum(r2E)
        total2E *= 1.5
    else:
        total2E = sum(r2E)

def r3SynE():
    global total3E
    if r3ES[0] == r3ES[1]:
        print("Ого, смотри какая у него отличная комбинация строчек! Ты реально обосрался...")
        total3E = sum(r3E)
        total3E *= 1.5
    else:
        total3E = sum(r3E)

def r1Ybattle():
    ansBars = int(input("Choose a punchline: "))
    if ansBars == matchBars[ansBars - 1][0]:
        r1Y.append(matchBars[0][1]['points'])
        r1YS.append(matchBars[0][1])
        rBars.pop(matchBars[ansBars - 1][0] - 1)

def r1Ebattle():
    eRandom = random.randint(0, len(enemy['bars'])-1)
    r1E.append(enemy['bars'][eRandom]['points'])
    r1ES.append(enemy['bars'][eRandom])
    print(enemy['bars'][eRandom]['bars'])

def r2Ybattle():
    ansBars = int(input("Choose a punchline: "))
    if ansBars == matchBars[ansBars - 1][0]:
        r2Y.append(matchBars[0][1]['points'])
        r2YS.append(matchBars[0][1]['synergy'])
        rBars.pop(matchBars[ansBars - 1][0] - 1)

def r2Ebattle():
    eRandom = random.randint(0, len(enemy['bars'])-1)
    r2E.append(enemy['bars'][eRandom]['points'])
    r2ES.append(enemy['bars'][eRandom]['synergy'])
    print(enemy['bars'][eRandom]['bars'])

def r3Ybattle():
    ansBars = int(input("Choose a punchline: "))
    if ansBars == matchBars[ansBars - 1][0]:
        r3Y.append(matchBars[0][1]['points'])
        r3YS.append(matchBars[0][1]['synergy'])
        rBars.pop(matchBars[ansBars - 1][0] - 1)

def r3Ebattle():
    eRandom = random.randint(0, len(enemy['bars'])-1)
    r3E.append(enemy['bars'][eRandom]['points'])
    r3ES.append(enemy['bars'][eRandom]['synergy'])
    print(enemy['bars'][eRandom]['bars'])

def battle_bars():
    global matchBars_1
    global matchBars_2
    global matchBars
    matchBars_1 = []
    matchBars_2 = []
    iBars = 1
    for bar in rBars:
        matchBars_1.append(iBars)
        matchBars_2.append(bar)
        print(" >[", iBars, "]: ", bar['bars'])
        iBars += 1
    matchBars = list(zip(matchBars_1, matchBars_2))

def day_skip_check():
    if urRapper['regged'] == False:
            counts['day'] += 1
            counts['battle'] += 1
    elif counts['day'] - counts['battle'] <= 6:
        counts['day'] += 1
    else:
        print("Иди сначала на батл, чмо. Потом поспишь у своей параши")


def statCheck():
    print('===========================')
    print('Готовых треков:', counts['studio'])
    print('Ваше баблишко: ', urRapper['money'], '$')
    print('Известность: ', urRapper['fame'])
    print('===========================''\n')

def shop_loop():
    while True:
        statCheck()
        print('\n''Выберите вещи для покупки!')
        print('1.', shop['slot1']['name'])
        print('2.', shop['slot2']['name'])
        print('3.', shop['slot3']['name'])
        print('0. Выход')

        buy = int(input('Введите число: '))
        if buy == 1:
            if urRapper['money'] >= shop['slot1']['cost']:
                urRapper['inv'].append(shop['slot1'])
                urRapper['money'] -= shop['slot1']['cost']
                shop['slot1'] = blank
            else:
                print('пошёл в жопу')
        elif buy == 2:
            if urRapper['money'] >= shop['slot2']['cost']:
                urRapper['inv'].append(shop['slot2'])
                urRapper['money'] -= shop['slot2']['cost']
                shop['slot2'] = blank
            else:
                print('пошёл в жопу')
        elif buy == 3:
            if urRapper['money'] >= shop['slot3']['cost']:
                urRapper['inv'].append(shop['slot3'])
                urRapper['money'] -= shop['slot3']['cost']
                shop['slot3'] = blank
        else:
            print('что ты делаешь?')
            break

gangstaTheme = [punchline_1, punchline_4]
millionTheme = [punchline_2, punchline_3]
minecraftTheme = [punchline_3, punchline_2]
elephantTheme = [punchline_4, punchline_1]


loot = [GucciGlock, GucciBankroll, NewLamborgini]
knowledge_loot = [punchline_1, punchline_2,punchline_3,punchline_4,punchline_9]
name = input('Введите своё имя: ')

print('====================')
print("1. Одинокий Гангстер")
print("2. Миллионер из трущоб")
print("3. Любитель игры в Майнкрафт")
print("4. Ценитель Х/Ф Зелёный Слоник")

background = int(input('Выберите своё прошлое: '))
if background == 1:
    urRapper['bg'] = 'gangsta'
    urRapper['title'] = 'старым гангстером.'
    urRapper['bars'].append(gangstaTheme[random.randint(0, len(gangstaTheme)-1)])
elif background == 2:
    urRapper['bg'] = 'million'
    urRapper['title'] = 'миллионером из трущоб.'
    urRapper['bars'].append(millionTheme[random.randint(0, len(millionTheme)-1)])
elif background == 3:
    urRapper['bg'] = 'minecraft'
    urRapper['title'] = 'любителем игры Minecraft.'
    urRapper['bars'].append(minecraftTheme[random.randint(0, len(minecraftTheme)-1)])
elif background == 4:
    urRapper['bg'] = 'elephant'
    urRapper['title'] = 'любителем реального дерьма.'
    urRapper['bars'].append(elephantTheme[random.randint(0, len(elephantTheme)-1)])
else:
    print('\n''Что ты делаешь?')

character_result = urRapper['title']
print('\n''Вы', name, 'и являетесь', character_result)
    # urRapper['inv'].append(GucciGlock)
    # urRapper['inv'].append(GucciBankroll)
    # urRapper['inv'].append(NewLamborgini)

while True:
    print('\n''===========================')
    print('Настал', counts['day'], 'день... Что будем делать сегодня? ;)')
    print('===========================''\n')
    statCheck()

    print(' >1. Записаться на Рэп баттл')
    print(' >2. Отдыхать')
    print(' >3. Пойти в магазин')
    print(' >4. Сделать суицид')
    print(' >5. Арендовать студию звукозаписи')
    print(' >6. Выйти на улицу')
    print(' >7. Придумать новые строчки''\n')
    daily_action = int(input('Ну что будем делать?: '))

    if daily_action == 1:
        if urRapper['regged'] == False:
            global enemy_roll
            global enemy
            enemy_roll = random.randint(0, len(enemies[urRapper['lvl']])-1)
            enemy = enemies[urRapper['lvl']][enemy_roll]
            counts['battle'] = counts['day']
            print('\n'"Вы зарегестрировались на батл. Ваш батл с ", enemy['name'], "состоится через 7 дней")
            urRapper['regged'] = True

        elif counts['day'] - counts['battle'] >= 7:
            print()
            print("=> А Ф И Ш А <=".center(40, "-"))
            print(name.center(40))
            print("X".center(40))
            print(enemy['name'].center(40))
            battle()
            urRapper['regged'] = False
            counts['battle'] = 0

        elif urRapper['regged'] == True:
            print('\n'"Молодой, чо приперся? Твой батл с ", enemy['name'], "через ", 7 - (counts['day'] - counts['battle']), "дней"'\n')

    elif daily_action == 2:
        day_skip_check()

    elif daily_action == 3:
        day_skip_check()
        if len(loot) == 0:
            shop_loop()

        else:
            a = random.randint(0, len(loot)-1)
            shop['slot1'] = loot[a]
            loot.pop(a)

            b = random.randint(0, len(loot)-1)
            shop['slot2'] = loot[b]
            loot.pop(b)

            c = random.randint(0, len(loot)-1)
            shop['slot3'] = loot[c]
            loot.pop(c)
            shop_loop()

    elif daily_action == 4:
        print('\n' 'ну и нахрена ты это сделал?')
        quit()

    elif daily_action == 5:
        day_skip_check()
        while True:
            print('\n''===========================')
            print('Добро пожаловать в студию звукозаписи!''\n')
            print(' >1. Записать песню')
            print(' >2. Посмотреть статистику')
            print(' >0. Выход')
            studio_action = int(input('Введите число: '))
            if studio_action == 1:
                r1Y = []
                r2Y = []
                print()
                print("Выбери строчки для песни: ")
                rBars = urRapper['bars'].copy()
                battle_bars()
                r1Ybattle()
                battle_bars()
                r1Ybattle()
                r1SynY()

<<<<<<< HEAD
            if len(r1Y) == 2:
                battle_bars()
                r2Ybattle()
                r2Ybattle()
                if r1Y[0] == r2Y[1]:
                    studio_summ = sum(r1Y) + sum(r2Y)
                    print(studio_summ)
                if studio_summ > 20:
                    print('\n''Нормальный трек получился!!!')
                elif studio_summ == 20:
                    print('\n''Сойдёт.')
                elif studio_summ < 20:
                    print('\n''Ну и что за говно ты высрал?')
                counts['studio'] += 1
                print('Вы записали свой', counts['studio'], 'песню! Так держать!')
                print('Песен до записи альбома:', counts['goal'] - counts['studio'])
            elif studio_action == 2:
                statCheck()
            else:
                break
=======
                if len(r1Y) == 2:
                    battle_bars()
                    r2Ybattle()
                    battle_bars()
                    r2Ybattle()
                    r2SynY()

                    studio_summ = total1Y + total2Y
                    if studio_summ > 20:
                        print('\n''Нормальный трек получился!!!')
                    elif studio_summ == 20:
                        print('\n''Сойдёт.')
                    elif studio_summ < 20:
                        print('\n''Ну и что за говно ты высрал?')
                    print('Вы записали свой', counts['studio'], 'песню! Так держать!')
                    print('Песен до записи альбома:', counts['goal'] - counts['studio'])
        elif studio_action == 2:
            statCheck()
        else:
            break
>>>>>>> e03f59ce55fd3082d7b41dfa2786ad0f99025652
    elif daily_action == 6:
        print('Вы вышли на улицу. Тут холодно.')
        print(' >1. Идти на пары')
        print(' >2. Идти на завод')
        print(' >3. Зайти обратно домой')
        street_action = int(input('Куда направляемся: '))
        if street_action == 1:
            day_skip_check()
            print('\n''Вы пошли на пары. Там с вами кое-что произошло.')
            university_var = ['good', 'bad', 'normal']
            university_roll = random.choices(university_var, weights = [30,20,50])
            if university_roll == 0:
                print('Ловя приход от университетских голубцов с яйцом, вы открываете новый жанр')
                a = random.randint(0,7)
                urRapper['genres'].append(music_addons['genres'][a])
                music_addons['genres'].pop(a)
                continue
            elif university_roll == 1:
                print('От голода в университетской столовке у вас происходит инсульт и вы забываете жанр')
                b = random.randint(0, len(urRapper['genres'])-1)
                urRapper['genres'].pop(b)
                print(urRapper['genres'])
                continue
            elif university_roll == 2:
                print('Вы проучились весь день и даже получили 5 по математике.')
                continue
        elif street_action == 2:
            day_skip_check()
            print('\n''Вы пошли на завод. Нормально так собрали мебель из IKEA, но кое-что с вами произошло.')
            factory_var = ['good', 'bad', 'normal']
            factory_roll = random.choices(factory_var, weights = [30,20,50])
            if factory_roll == ['good']:
                print('===========================')
                print('Прораб, отсутствовавший в течении 6 месяцев, рассказал о каком-то "топ-донатере"')
                print('который проспонсировал его на первой работе. На радостях, прораб даёт 1% вам.')
                urRapper['money'] += 1000
                continue
            elif factory_roll == ['bad']:
                print('===========================')
                print('Недавно объявившийся прораб что-то бубнил про некий "бан",')
                print('из-за которого его основной заработок прекратился.')
                print('Собственно, поэтому он и задержал вам зарплату до лучших дней, а также одолжил несколько долларов.')
                urRapper['money'] -= 500
                continue
            elif factory_roll == ['normal']:
                print('===========================')
                print('Я пошутил, ничего не произошло. Вы отработали смену и получили деньги.')
                urRapper['money'] += 500
                continue
        elif street_action == 3:
            print('Вы решили вернуться домой. На улице слишком холодно')
            continue
    elif daily_action == 7:
        while True:
            a1 = random.randint(0, len(knowledge_loot)-1)
            knowledge_shop['slot1'] = knowledge_loot[a1]
            statCheck()
            print('\n''Выберите строку для изучения!')
            print('1.', knowledge_shop['slot1']['bars'])
            print('2. Выйти')
            knowledge_action = int(input('Выберите уже знание: '))
            if knowledge_action == 1:
                urRapper['bars'].append(knowledge_shop['slot1'])
                day_skip_check()
                break
            if knowledge_action == 2:
                break
