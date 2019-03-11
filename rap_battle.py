import random
while True:
    GucciGlock = {
        'id': '100',
        'name': 'GucciGlock',
        'bars': 'У меня есть Гуччи глок, ты - прилизаный пидарок',
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
    urRapper = {
        'inv': [],
        'bars': [],
        'bg': 'none',
        'title': 'none',
        'money': 3000
    }
    shop = {
    'slot1': 'none',
    'slot2': 'none',
    'slot3': 'none'
    }

    punchline_1 = {
        'id': 1,
        'bars': 'У меня есть Гуччи глок, ты - прилизаный пидарок',
        'theme': 'gangsta'
    }
    punchline_2 = {
        'id': 2,
        'bars': 'Гуччи бенкролл - это смысл жизни. Я не ЧСВ, просто нет корысти',
        'theme': 'million'
    }
    punchline_3 = {
        'id': 3,
        'bars': 'Новый ламборгини, новые цацки. Моя жизнь - это Каноха, ты в ней Акацке',
        'theme': 'minecraft'
    }
    punchline_4 = {
        'id': 4,
        'bars': 'Я биссексуал',
        'theme': 'elephant'
    }
    urRapper = {
        'inv': [],
        'bars': [],
        'bg': 'none',
        'money': 3000
    }

    gangstaTheme = [punchline_1, punchline_4]
    millionTheme = [punchline_2, punchline_3]
    minecraftTheme = [punchline_3, punchline_2]
    elephantTheme = [punchline_4, punchline_1]
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
        urRapper['bars'].append(gangstaTheme[random.randint(0, len(gangstaTheme)-1)]['bars'])
    elif background == 2:
        urRapper['bg'] = 'million'
        urRaper['title'] = 'миллионером из трущоб.'
        urRapper['bars'].append(millionTheme[random.randint(0, len(millionTheme)-1)]['bars'])
    elif background == 3:
        urRapper['bg'] = 'minecraft'
        urRapper['title'] = 'любителем игры Minecraft.'
        urRapper['bars'].append(minecraftTheme[random.randint(0, len(minecraftTheme)-1)]['bars'])
    elif background == 4:
        urRapper['bg'] = 'elephant'
        urRapper['title'] = 'любителем реального дерьма.'
        urRapper['bars'].append(elephantTheme[random.randint(0, len(elephantTheme)-1)]['bars'])
    else:
        print('\n''Что ты делаешь?')
        continue
    character_result = urRapper['title']
    print('Вы', name, 'и являетесь', character_result)
    # urRapper['inv'].append(GucciGlock)
    # urRapper['inv'].append(GucciBankroll)
    # urRapper['inv'].append(NewLamborgini)

    while True:
        print("You have: ")
        matchBars_1 = []
        matchBars_2 = []
        iBars = 1
        for bar in urRapper['bars']:
            matchBars_1.append(iBars)
            matchBars_2.append(bar)
            print(" >[", iBars, "]: ", bar)
            iBars += 1
        matchBars = list(zip(matchBars_1, matchBars_2))
        ansBars = int(input("Choose a punchline: "))
        break

    print('===========================')
    print('Настал новый день... Что будем делать сегодня? ;)')
    print('1. Записаться на Рэп баттл')
    print('2. Пойти в стриптиз бар') ##https://youtu.be/ielVW4MVOrM
    print('3. Пойти в магазин')
    print('4. Сделать суицид')
    daily_action = int(input('Ну что будем делать?: '))
    if daily_action == 3:
        while True:
            loot = [GucciGlock, GucciBankroll, NewLamborgini]

            a = random.randint(0, len(loot)-1)
            shop['slot1'] = loot[a]
            loot.remove(loot[a])

            b = random.randint(0, len(loot)-1)
            shop['slot2'] = loot[b]
            loot.remove(loot[b])

            c = random.randint(0, len(loot)-1)
            shop['slot3'] = loot[c]

            print('\n''Выберите вещи для покупки!')
            print('1.', (shop['slot1']['bars']))
            print('2.', (shop['slot2']['bars']))
            print('3.', (shop['slot3']['bars']))
            print('0. Выход') ##А выхода то нет!

            buy = int(input('Введите число: '))
            if buy == 1:
                if urRapper['money'] >= shop['slot1']['cost']:
                    urRapper['inv'].append(shop['slot1'])
                else:
                    print('пошёл в жопу')
            elif buy == 2:
                if urRapper['money'] >= shop['slot2']['cost']:
                    urRapper['inv'].append(shop['slot2'])
                else:
                    print('пошёл в жопу')
            elif buy == 3:
                if urRapper['money'] >= shop['slot3']['cost']:
                    urRapper['inv'].append(shop['slot3'])
            else:
                print('что ты делаешь?')
            s = 1
            for i in urRapper['inv']:
                print('\n'" >[", s, "]: ", i['bars'])
                s += 1
    if daily_action == 4:
        print('\n' 'ну и нахрена ты это сделал?')
        exit()
