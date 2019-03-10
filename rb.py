import random

urRaper = {
    'inv': [],
    'bars': [],
    'class': 'none'
}

print("1. Одинокий Гангстер")
print("2. Миллионер из трущоб")
print("3. Любитель игры в Майнкрафт")
print("4. Ценитель Х/Ф Зелёный Слоник")

background = int(input)
===========================================
import random
while True:
    GucciGlock = {
        'id': '100',
        'name': 'GucciGlock',
        'bars': 'У меня есть Гуччи глок, ты - прилизаный пидарок'
}

    GucciBankroll = {
        'id': '101',
        'name': 'GucciBankroll',
        'bars': 'Гуччи бенкролл - это смысл жизни. Я не ЧСВ, просто нет корысти'
}

    NewLamborgini = {
        'id': '102',
        'name': 'NewLamborgini',
        'bars': 'Новый ламборгини, новые цацки. Моя жизнь - это Каноха, ты в ней Акацке'
}
    shop = {
    'slot1': 'none',
    'slot2': 'none',
    'slot3': 'none'
    }
    loot = [GucciGlock, GucciBankroll, NewLamborgini]
    a = random.randint(0, len(loot)-2)
    shop['slot1'] = loot[a]
    loot.remove(loot[a])
    b = random.randint(0, len(loot)-1)
    shop['slot2'] = loot[b]
    loot.remove(loot[b])
    c = random.randint(0, len(loot)-1)
    print('Выберите вещи для покупки!')
    print('1.', shop['slot1'])
    print('2.', shop['slot2'])
    print('3.', shop['slot3'])
    buy = input('Введите число: ')
    if buy == '1':
        if money >= '50':
            urRapper['inv'].append(GucciGlock)
        elif money <= '50':
            print('пошёл в жопу') ##вещи пишем в самом начале
    if buy == '2': ##urraper условное обозначение потом поменяем
        if money >= '10':
            urRapper['inv'].append(GucciBankroll)
        elif money <= '10':
            print('пошёл в жопу')
    if buy == '3':
        if money >= '20':
            urRapper['inv'].append(NewLamborgini)
        elif money <= '20':
            print('пошёл в жопу')
    if buy == '0':
        break
