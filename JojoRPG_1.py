import random

enemy = {}

frostbolt = {
    'name': 'Frostbolt',
    'damage': 10,
    'heal': 0,
    'manacost': 10,
    'statusEffectE': 'freezed',
    'statusEffectC': 'none',
    'timing': 2
}

repel = {
    'name': 'Repel',
    'damage': 0,
    'heal': 3,
    'manacost': 5,
    'statusEffectE': 'none',
    'statusEffectC': 'blessed',
    'timing': 3
}

wolf = {
    'id': 1,
    'lvl': 1,
    'type': 'Beast',
    'name': 'Wild wolf',
    'hp': 15,
    'damage': 5,
    'mp': 0,
    'mpMax': 0,
    'bounty': 5,
    'statusEffect': [],
    'exp': 5
}
sheep = {
    'id': 2,
    'lvl': 1,
    'type': 'Beast',
    'name': 'Golden sheep',
    'hp': 50,
    'hpMax': 50,
    'damage': 1,
    'mp': 0,
    'mpMax': 0,
    'bounty': 50,
    'statusEffect': [],
    'exp': 5
}
earthworm = {
    'id': 3,
    'lvl': 1,
    'type': 'Beast',
    'name': 'Earthworm Jimm',
    'hp': 2,
    'hpMax': 2,
    'damage': 10,
    'mp': 0,
    'mpMax': 0,
    'bounty': 10,
    'statusEffect': [],
    'exp': 5
}
pigbenis = {
    'id': 4,
    'lvl': 2,
    'type': 'Beast',
    'name': 'Pig Benis',
    'hp': 30,
    'hpMax': 30,
    'damage': 10,
    'mp': 0,
    'mpMax': 0,
    'bounty': 70,
    'statusEffect': [],
    'exp': 30
}
char = {
    'name': 'Jojo',
    'race': 'Kadjit',
    'type': 'Warrior',
    'hp': 20,
    'hpMax': 20,
    'damage': 5,
    'mp': 20,
    'mpMax': 20,
    'gold': 0,
    'mstrength': 1,
    'spells': [ frostbolt, repel ],
    'statusEffect': [],
    'exp': 0,
    'lvl': 1
}

def enemy_loot():
    char['gold'] += enemy['bounty']
    char['exp'] += enemy['exp']
    enemy['hp'] = eshp[0]
    enemy['statusEffect'].clear()
    print("\n- - - - - - - - - - - - - - - - -")
    print("You killed ", enemy['name'])
    print("Bounty awarded: ", enemy['bounty'], " gold")
    print("- - - - - - - - - - - - - - - - -\n")

def enemy_check():
    print("\n- / - / - / - / - / - / - / - / -")
    print("Your enemy is: ")
    print('Level: ', enemy['lvl'])
    print('Type: ', enemy['type'])
    print('Name: ', enemy['name'])
    print('Health: ', enemy['hp'])
    print('Damage: ', enemy['damage'])
    print('Mana: ', enemy['mp'])
    print('Bounty: ', enemy['bounty'])
    print('Status Effect: ', enemy['statusEffect'])
    print("- / - / - / - / - / - / - / - / -\n")

def char_check():
    if char['exp'] == char['lvl']*10:
        char['exp'] -= char['lvl']*10
        char['lvl'] += 1
    print("\n- / - / - / - / - / - / - / - / -")
    print("Your character: ")
    print('Level: ', char['lvl'])
    print('Experience: ', char['exp'])
    print('Name: ', char['name'])
    print('Race: ', char['race'])
    print('Health: ', char['hp'], "/", char['hpMax'])
    print('Damage: ', char['damage'])
    print('Mana: ', char['mp'], "/", char['mpMax'])
    print('Magic strength: ', char['mstrength'])
    print('Gold: ', char['gold'])
    ##print('Available spells: ', char['spells'])
    print("- / - / - / - / - / - / - / - / -\n")

while char['hp'] >= 0:
    e = random.randint(1, 3)
    eshp = [ 0, char['hp'], char['mp'] ]
    if e == wolf['id']:
        enemy = wolf
        eshp.insert(0, enemy['hp'])

    elif e == sheep['id']:
        enemy = sheep
        eshp.insert(0, enemy['hp'])

    elif e == earthworm['id']:
        enemy = earthworm
        eshp.insert(0, enemy['hp'])

    while True:
        enemy_check()
        char_check()
        print(" >[1]: Attack")
        print(" >[2]: Heal")
        print(" >[3]: Restore mana")
        print(" >[4]: Cast a spell")
        a = int(input("Choose your action: "))

        if a == 1:
            enemy['hp'] -= char['damage']
            if enemy['hp'] > 0:
                char['hp'] -= enemy['damage']
                if char['hp'] <= 0:
                    print()
                    print("You've been gnomed!")
                    break
            else:
                enemy_loot()
                break

        elif a == 2:
            char['hp'] += 10 * char['mstrength']
            char['mp'] -= 6
            if char['hp'] > char['hpMax']:
                char['hp'] = char['hpMax']
            char['hp'] -= enemy['damage']
            if char['hp'] <= 0:
                print()
                print("You've been gnomed!")
                break

        elif a == 3:
            char['mp'] += 5
            if char['mp'] > char['mpMax']:
                char['mp'] = char['mpMax']
            char['hp'] -= enemy['damage']
            if char['hp'] <= 0:
                print()
                print("You've been gnomed!")
                break

        elif a == 4:
            print("You have: ")
            cSpell_1 = []
            cSpell_2 = []
            iSpell = 1
            for spell in range(0, len(char['spells'])):
                cSpell_1.append(iSpell)
                cSpell_2.append(char['spells'][spell])
                print(" >[",iSpell,"]: ", char['spells'][spell]['name'])
                iSpell += 1
            cSpell = list(zip(cSpell_1, cSpell_2))

            ansSpell = int(input("Choose a spell for cast: "))
            if ansSpell == cSpell[ansSpell - 1][0]:
                enemy['hp'] -= cSpell[ansSpell - 1][1]['damage']
                char['hp'] += cSpell[ansSpell - 1][1]['heal']
                char['mp'] -= cSpell[ansSpell - 1][1]['manacost']
                if enemy['hp'] > 0:
                    char['hp'] -= enemy['damage']
                    if cSpell[ansSpell - 1][1]['statusEffectE'] != 'none':
                        if cSpell[ansSpell - 1][1]['statusEffectE'] in enemy['statusEffect']:
                            pass
                        else:
                            enemy['statusEffect'].append(cSpell[ansSpell - 1][1]['statusEffectE'])
                    elif cSpell[ansSpell - 1][1]['statusEffectC'] != 'none':
                        if cSpell[ansSpell - 1][1]['statusEffectC'] in char['statusEffect']:
                            pass
                        else:
                            char['statusEffect'].append(cSpell[ansSpell - 1][1]['statusEffectC'])

                else:
                    enemy_loot()
