import random
##словари
punchline_1 = {
    'id': 1,
    'bars': 'У меня есть Гуччи глок, ты - прилизаный грибок',
    'theme': 'gangsta',
    'points': 5,
    'synnergy': 2
}
punchline_2 = {
    'id': 2,
    'bars': 'Гуччи бенкролл - это смысл жизни. Я не ЧСВ, просто нет корысти',
    'theme': 'million',
    'points': 5,
    'synnergy': 1
}
punchline_3 = {
    'id': 3,
    'bars': 'Новый ламборгини, новые цацки. Моя жизнь - это Каноха, ты в ней Акацке',
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
    'bars': 'Твоя жопа прошита, как и мой ИксБокс. У тебя бомбит, ведь я здесь босс',
    'theme': 'elephant',
    'points': 5
}
punchline_8 = {
    'id': 8,
    'bars': 'Твоя жопа прошита, как и мой ИксБокс. У тебя бомбит, ведь я здесь босс',
    'theme': 'elephant',
    'points': 5
}
yungleo = {
    'id': 50,
    'name': 'Yung Leo',
    'bars': [punchline_2]
}
fiftydraem = {
    'id': 51,
    'name': 'Fifty Draem',
    'bars': [punchline_1]
}
creeper = {
    'id': 52,
    'name': 'Kriper95',
    'bars': [punchline_3]
}
lich = {
    'id': 53,
    'name': 'Lichinus',
    'bars': [punchline_4]

}
GucciGlock = {
    'id': '100',
    'name': 'GucciGlock',
    'bars': 'У меня есть Гуччи глок, ты - прилизаный грибок',
    'cost': 50
}
GucciBankroll = {
    'id': '101',
    'name': 'GucciBankroll',
    'bars': 'Гуччи бенкролл - это смысл жизни. Я не ЧСВ, просто нет корысти',
    'cost': 75
}
NewLamborgini = {
    'id': '102',
    'name': 'NewLamborgini',
    'bars': 'Новый ламборгини, новые цацки. Моя жизнь - это Каноха, ты в ней Акацке',
    'cost': 320
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
    'bars': [punchline_3, punchline_4, punchline_5, punchline_6, punchline_7, punchline_8],
    'bg': 'none',
    'title': 'none',
    'money': 3000
}
def battle():
    global rBars
    print('\n''$$$$$$$$$$$$$$$$$$$$$$')
    print("You have: ")
    rBars = urRapper['bars'].copy()
    r1Y = []
    r2Y = []
    r3Y = []
    r1E = []
    r2E = []
    r3E = []
    battle_bars()
    ansBars = int(input("Choose a punchline: "))
    if ansBars == matchBars[ansBars - 1][0]:
        r1Y.append(matchBars[0][1]['points'])
        rBars.pop(matchBars[ansBars - 1][0] - 1)
    eRandom = random.randint(0, len(enemy['bars'])-1)
    r1E.append(enemy['bars'][eRandom]['points'])
    print(enemy['bars'][eRandom]['bars'])

    if len(r1Y) and len(r1E) == 1:
        battle_bars()
        ansBars = int(input("Choose a punchline: "))
        if ansBars == matchBars[ansBars - 1][0]:
            r2Y.append(matchBars[0][1]['points'])
            rBars.pop(matchBars[ansBars - 1][0] - 1)
        eRandom = random.randint(0, len(enemy['bars'])-1)
        r2E.append(enemy['bars'][eRandom]['points'])
        print(enemy['bars'][eRandom]['bars'])

        if len(r2Y) and len(r2E) == 1:
            battle_bars()
            ansBars = int(input("Choose a punchline: "))
            if ansBars == matchBars[ansBars - 1][0]:
                r3Y.append(matchBars[0][1]['points'])
                rBars.pop(matchBars[ansBars - 1][0] - 1)
            eRandom = random.randint(0, len(enemy['bars'])-1)
            r3E.append(enemy['bars'][eRandom]['points'])
            print(enemy['bars'][eRandom]['bars'])

            if len(r3Y) and len(r3E) == 1:
                battleSummY = sum(r1Y) + sum(r2Y) + sum(r3Y)
                battleSummE = sum(r1E) + sum(r2E) + sum(r3E)
                if battleSummY > battleSummE:
                    print("You win!")
                elif battleSummY == battleSummE:
                    print("Sosi jopy")
                else:
                    print("You lose")

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

def shop_loop():
    while True:
        print('\n''Выберите вещи для покупки!')
        print('1.', shop['slot1']['name'])
        print('2.', shop['slot2']['name'])
        print('3.', shop['slot3']['name'])
        print('0. Выход') ##А выхода то нет!

        buy = int(input('Введите число: '))
        if buy == 1:
            if urRapper['money'] >= shop['slot1']['cost']:
                urRapper['inv'].append(shop['slot1'])
                shop['slot1'] = blank
            else:
                print('пошёл в жопу')
        elif buy == 2:
            if urRapper['money'] >= shop['slot2']['cost']:
                urRapper['inv'].append(shop['slot2'])
                shop['slot2'] = blank
            else:
                print('пошёл в жопу')
        elif buy == 3:
            if urRapper['money'] >= shop['slot3']['cost']:
                urRapper['inv'].append(shop['slot3'])
                shop['slot3'] = blank
        else:
            print('что ты делаешь?')
            break

gangstaTheme = [punchline_1, punchline_4]
millionTheme = [punchline_2, punchline_3]
minecraftTheme = [punchline_3, punchline_2]
elephantTheme = [punchline_4, punchline_1]

loot = [GucciGlock, GucciBankroll, NewLamborgini]
day_count = 0
studio_count = 0
goal = 5
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
    # s = 1
    # for i in urRapper['inv']:
    #     print(" >[", s, "]: ", i['bars'])
    #     s += 1

    print('\n''===========================')
    print('Настал новый день... Что будем делать сегодня? ;)')
    print(' >1. Записаться на Рэп баттл')
    print(' >2. Отдыхать')
    print(' >3. Пойти в магазин')
    print(' >4. Сделать суицид')
    print(' >5. Арендовать студию звукозаписи')
    print('Готовых треков:', studio_count)
    print('День', day_count)
    daily_action = int(input('Ну что будем делать?: '))

    if daily_action == 1:
        enemy_roll = random.randint(50,53)
        if enemy_roll == yungleo['id']:
            enemy = yungleo
            battle()
        elif enemy_roll == fiftydraem['id']:
            enemy = fiftydraem
            battle()
        elif enemy_roll == Lich['id']:
            enemy = Lich
            battle()
        elif enemy_roll == creeper['id']:
            enemy = creeper
            battle()
        elif enemy_roll == lich['id']:
            enemy = lich
            battle()

    elif daily_action == 3:
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
            # print('\n''===========================')
            # print("Магазин пуст, пошел в сраку")
            # print('===========================')

    elif daily_action == 4:
        print('\n' 'ну и нахрена ты это сделал?')
        quit()
    if daily_action == 5:
        if urRapper['money'] < 300:
            print('Не хватает у тебя баблишка...')
        if urRapper['money'] > 300:
            studio_count += 1
        print('\n''Вы успешно записали трек! Треков до победы:', goal - studio_count)
    if studio_count == goal:
        print('Вы записали свой ПЕРВЫЙ альбом, Красава!!!')
        print('Игра пройдена, не забудьте оставить фидбек и поделиться с нами вашими деньгами! Удачи!')
        exit()
