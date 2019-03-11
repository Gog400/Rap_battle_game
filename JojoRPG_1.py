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
    'heal': 0,
    'manacost': 5,
    'statusEffectE': 'none',
    'statusEffectC': 'blessed',
    'timing': 3
}

wolf = {
    'id': 1,
    'type': 'Beast',
    'name': 'Wild wolf',
    'hp': 10,
    'damage': 5,
    'mp': 0,
    'bounty': 5,
    'statusEffect': []
}
sheep = {
    'id': 2,
    'type': 'Beast',
    'name': 'Golden sheep',
    'hp': 1,
    'damage': 1,
    'mp': 0,
    'bounty': 50,
    'statusEffect': []
}
earthworm = {
    'id': 3,
    'type': 'Beast',
    'name': 'Earthworm Jimm',
    'hp': 2,
    'damage': 10,
    'mp': 0,
    'bounty': 10,
    'statusEffect': []
}
char = {
    'name': 'Jojo',
    'race': 'Kadjit',
    'type': 'Warrior',
    'hp': 20,
    'damage': 5,
    'mp': 20,
    'gold': 0,
    'mstrength': 1,
    'spells': [ frostbolt, repel ],
    'statusEffect': []
}

def enemy_loot():
    char['gold'] += enemy['bounty']
    enemy['hp'] = eshp[0]
    enemy['statusEffect'].clear()
    print("\n- - - - - - - - - - - - - - - - -")
    print("You killed ", enemy['name'])
    print("Bounty awarded: ", enemy['bounty'], " gold")
    print("- - - - - - - - - - - - - - - - -\n")

def enemy_check():
    print("\n- / - / - / - / - / - / - / - / -")
    print("Your enemy is: ")
    print('Type: ', enemy['type'])
    print('Name: ', enemy['name'])
    print('Health: ', enemy['hp'])
    print('Damage: ', enemy['damage'])
    print('Mana: ', enemy['mp'])
    print('Bounty: ', enemy['bounty'])
    print('Status Effect: ', enemy['statusEffect'])
    print("- / - / - / - / - / - / - / - / -\n")

def char_check():
    print("\n- / - / - / - / - / - / - / - / -")
    print("Your character: ")
    print('Name: ', char['name'])
    print('Race: ', char['race'])
    print('Health: ', char['hp'])
    print('Damage: ', char['damage'])
    print('Mana: ', char['mp'])
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
            char['hp'] += 4 * char['mstrength']
            char['mp'] -= 6
            char['hp'] -= enemy['damage']
            if char['hp'] <= 0:
                print()
                print("You've been gnomed!")
                break

        elif a == 3:
            char['mp'] += 5
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
                char['hp'] += cSpell[ansSpell - 1][1]['damage']
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
