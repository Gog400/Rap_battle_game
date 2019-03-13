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
    'battle': ''
}
punchline_1 = {
    'id': 1,
    'bars': 'У меня есть Гуччи глок, ты - прилизаный грибок',
    'theme': 'gangsta',
    'points': 5,
    'synergy': 1
}
punchline_2 = {
    'id': 2,
    'bars': 'Гуччи бенкролл - это смысл жизни. Я не ЧСВ, просто нет корысти',
    'theme': 'million',
    'points': 5,
    'synergy': 1
}
punchline_3 = {
    'id': 3,
    'bars': 'Новый ламборгини, новые цацки. Моя жизнь - Каноха, а ты в ней Акацке',
    'theme': 'minecraft',
    'points': 5
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
urRapper = {
    'inv': [],
    'bars': [punchline_1, punchline_2, punchline_3, punchline_4, punchline_9],
    'bg': 'none',
    'title': 'none',
    'money': 3000,
    'fame': 0,
    'lvl': '1'
}
def battle():
    global r1Y
    global r2Y
    global r3Y
    global r1E
    global r2E
    global r3E
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
    battle_bars()
    r1Ybattle()
    battle_bars()
    r1Ybattle()
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
                battleSummY = sum(r1Y) + sum(r2Y) + sum(r3Y)
                battleSummE = sum(r1E) + sum(r2E) + sum(r3E)
                if battleSummY > battleSummE:
                    print("You win!")
                    urRapper['fame'] += enemy['lvl'] * 15
                    urRapper['money'] += enemy['lvl'] * 100
                    enemies[urRapper['lvl']].pop(enemy_roll)

                elif battleSummY == battleSummE:
                    print("Sosi jopy")
                else:
                    print("You lose")
                    urRapper['fame'] -= enemy['lvl'] * 15

def r1Ybattle():
    ansBars = int(input("Choose a punchline: "))
    if ansBars == matchBars[ansBars - 1][0]:
        r1Y.append(matchBars[0][1]['points'])
        rBars.pop(matchBars[ansBars - 1][0] - 1)
def r1Ebattle():
    eRandom = random.randint(0, len(enemy['bars'])-1)
    r1E.append(enemy['bars'][eRandom]['points'])
    print(enemy['bars'][eRandom]['bars'])
def r2Ybattle():
    ansBars = int(input("Choose a punchline: "))
    if ansBars == matchBars[ansBars - 1][0]:
        r2Y.append(matchBars[0][1]['points'])
        rBars.pop(matchBars[ansBars - 1][0] - 1)
def r2Ebattle():
    eRandom = random.randint(0, len(enemy['bars'])-1)
    r2E.append(enemy['bars'][eRandom]['points'])
    print(enemy['bars'][eRandom]['bars'])
def r3Ybattle():
    ansBars = int(input("Choose a punchline: "))
    if ansBars == matchBars[ansBars - 1][0]:
        r3Y.append(matchBars[0][1]['points'])
        rBars.pop(matchBars[ansBars - 1][0] - 1)
def r3Ebattle():
    eRandom = random.randint(0, len(enemy['bars'])-1)
    r3E.append(enemy['bars'][eRandom]['points'])
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
    if counts['battle'] - 7 == 0:
        print("Иди сначала на батл, чмо. Потом поспишь у своей параши")
    elif counts['battle'] != '':
        counts['day'] += 1
        counts['battle'] += 1

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
    print(' >5. Арендовать студию звукозаписи''\n')

    daily_action = int(input('Ну что будем делать?: '))

    if daily_action == 1:
        enemy_roll = random.randint(0, len(enemies[urRapper['lvl']])-1)
        enemy = enemies[urRapper['lvl']][enemy_roll]

        if counts['battle'] == '':
            counts.update({'battle': 0})
            print('\n'"Вы зарегестрировались на батл. Ваш батл с ", enemy['name'], "состоится через 7 дней")

        elif counts['battle'] - 7 == 0:
            print()
            print("=> А Ф И Ш А <=".center(40, "-"))
            print(name.center(40))
            print("X".center(40))
            print(enemy['name'].center(40))
            battle()

        else:
            print('\n'"Молодой, чо приперся? Твой батл с ", enemy['name'], "через ", 7 - counts['battle'], "дней"'\n')

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

    if daily_action == 5:
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
                r1Ybattle()

                if len(r1Y) == 2:
                    battle_bars()
                    r2Ybattle()
                    r2Ybattle()

                    studio_summ = sum(r1Y) + sum(r2Y)
                    if studio_summ > 20:
                        print('\n''Нормальный трек получился!!!')
                    if studio_summ == 20:
                        print('\n''Сойдёт.')
                    if studio_summ < 20:
                        print('\n''Ну и что за говно ты высрал?')
                    counts['studio'] += 1
                    print('Вы записали свой', counts['studio'], 'песню! Так держать!')
                    print('Песен до записи альбома:', counts['goal'] - counts['studio'])
            elif studio_action == 2:
                statCheck()
            else:
                break
