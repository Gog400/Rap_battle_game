##Описание айтемов
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
    'bars': 'Я сосу бибу'
    'theme': 'gangsta'
}
punchline_2 = {
    'id': 2,
    'bars': 'Я сосу бибу'
    'theme': 'million'
}
punchline_3 = {
    'id': 3,
    'bars': 'Я сосу бибу'
    'theme': 'minecraft'
}
punchline_4 = {
    'id': 4,
    'bars': 'Я сосу бибу'
    'theme': 'elephant'
}

name = input('Введите свой реперский ник: ')
print('''
1. Одинокий Гангстер
2. Миллионер из трущоб
3. Любитель игры в Майнкрафт
4. Ценитель К/Ф Зелёный Слоник
''')

background = input('Выберите своё прошлое: ')
if background == 1:
    urRapper['bars'].append()

##Описание основного персонажа
urRapper = {
    'inv': [],
    'bars': []
}

##Добавление(лут) айтемов в инвентарь
urRapper['inv'].append(GucciGlock)
urRapper['inv'].append(GucciBankroll)
urRapper['inv'].append(NewLamborgini)

s = 1
for i in urRapper['inv']:
    print(" >[", s, "] :", i['bars'])
    s += 1

a = int(input('Выбери панчлайн: '))
