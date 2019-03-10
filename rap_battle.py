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
##Описание основного персонажа
urRapper = {
    'inv': []
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
