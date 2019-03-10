import random
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
    'money': 3000
}
shop = {
'slot1': 'none',
'slot2': 'none',
'slot3': 'none'
}

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
            print('пошёл в жопу')
    else:
        break
    s = 1
    for i in urRapper['inv']:
        print('\n'" >[", s, "]: ", i['bars'])
        s += 1
