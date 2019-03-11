import random

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

print("1. Одинокий Гангстер")
print("2. Миллионер из трущоб")
print("3. Любитель игры в Майнкрафт")
print("4. Ценитель Х/Ф Зелёный Слоник")

background = int(input('Выберите своё прошлое: '))
if background == 1:
    urRapper['bg'] = 'gangsta'
    urRapper['bars'].append(gangstaTheme[random.randint(0, len(gangstaTheme)-1)]['bars'])
elif background == 2:
    urRapper['bg'] = 'million'
    urRapper['bars'].append(millionTheme[random.randint(0, len(millionTheme)-1)]['bars'])
elif background == 3:
    urRapper['bg'] = 'minecraft'
    urRapper['bars'].append(minecraftTheme[random.randint(0, len(minecraftTheme)-1)]['bars'])
elif background == 4:
    urRapper['bg'] = 'elephant'
    urRapper['bars'].append(elephantTheme[random.randint(0, len(elephantTheme)-1)]['bars'])

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
