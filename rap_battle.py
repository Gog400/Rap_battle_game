import random

GucciGlock = {
    'name': 'GucciGlock',
    'bars': 'У меня есть Гуччи глок, ты - прилизаный пидарок'
}

GucciBankroll = {
    'name': 'GucciBankroll',
    'bars': 'Гуччи бенкролл - это смысл жизни. Я не ЧСВ, просто нет корысти'
}

NewLamborgini = {
    'name': 'NewLamborgini',
    'bars': 'Новый ламборгини, новые цацки. Моя жизнь - это Каноха, ты в ней Акацке'
}
punchline_1 = {
    'id': 1,
    'bars': 'Я сос',
    'theme': 'gangsta'
}
punchline_2 = {
    'id': 2,
    'bars': 'Я сосу',
    'theme': 'million'
}
punchline_3 = {
    'id': 3,
    'bars': 'Я сосу би',
    'theme': 'minecraft'
}
punchline_4 = {
    'id': 4,
    'bars': 'Я сосу бибу',
    'theme': 'elephant'
}
urRapper = {
    'inv': [],
    'bars': [],
    'theme': []
}

gangstaTheme = [punchline_1]
millionTheme = [punchline_2]
minecraftTheme = [punchline_3]
elephantTheme = [punchline_4]

print("1. Одинокий Гангстер")
print("2. Миллионер из трущоб")
print("3. Любитель игры в Майнкрафт")
print("4. Ценитель Х/Ф Зелёный Слоник")

background = input('Выберите своё прошлое: ')
if background == 1:
    urRapper['theme'] = gangstaTheme['theme']
    urRapper['bars'].append(gangstaTheme[random.randint(0, len(gangstaTheme)-1)]['bars'])
elif background == 2:
    urRapper['theme'] = millionTheme['theme']
    urRapper['bars'].append(millionTheme[random.randint(0, len(millionTheme)-1)]['bars'])
elif background == 3:
    urRapper['theme'] = minecraftTheme['theme']
    urRapper['bars'].append(minecraftTheme[random.randint(0, len(minecraftTheme)-1)]['bars'])
elif background == 4:
    urRapper['theme'] = elephantTheme['theme']
    urRapper['bars'].append(elephantTheme[random.randint(0, len(elephantTheme)-1)]['bars'])
    print(urRapper['bars'])
    print(urRapper['theme'])


urRapper['inv'].append(GucciGlock)
urRapper['inv'].append(GucciBankroll)
urRapper['inv'].append(NewLamborgini)

s = 1
for i in urRapper['inv']:
    print(" >[", s, "]: ", i['bars'])
    s += 1

a = int(input('Выбери панчлайн: '))
