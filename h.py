import random

enemy {}

name = input('Введите свой реперский ник: ')
print('''
1. Одинокий Гангстер
2. Миллионер из трущоб
3. Любитель игры в Майнкрафт
4. Ценитель К/Ф Зелёный Слоник
''')
background = input('Выберите своё прошлое: ')

if background == '1':
    print('Вы опасный человече и каждому дадите по жопе, если на то заблагорассудится...')
elif background == '2':
    print('Вы богатый человече и каждому славному друже купите холодный чай Nestea и дадите новый ламборгини')
elif background == '3':
    print('\n''Вы фанат одной замечательной игры, где можно строить механизмы, и вообщемто говоря, ксожалению недооцененной игры...')
    print('----------------')
    print('''
    1. Вьетнамская ловушка
    2. Раздатчик с воронкой
    3. Ферма тростника
    4. Ферма эндерменов
    ''')
    background1 = input('Выберите свой любимый механизм: ')
elif background == '4':
    print('Вы фанат одного замечательного фильма, где подробнейшим образом изучается анатомия человека, а так же социологическая обстановка в военной тюрьме')
    print('-----------------')
    print('''
    1. Пахом
    2. Епифанцев
    3. Полковник
    ''')
    background1 = input('Выберите своего любимого перса: ')
