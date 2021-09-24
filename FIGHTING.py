character = "Knight"
character_base_stats = { 'dexterity': 3 , 'strength': 8 , 'luck': 5 }
character_weapon = 'Sword of the Galiant'
character_weapon_stats = { 'defense': 30 , 'attack': 60, 'speed': 80 }
character_health = 100

enemy = "Wolf"
enemy_base_stats = { 'dexterity': 5 , 'strength': 3 , 'luck': 2 }
enemy_weapon = 'Death Mace'
enemy_weapon_stats = { 'defense': 70 , 'speed': 40 , 'attack': 50 }
enemy_health = 100

print('Battle Begins!')
#print('(use space bar to attack!' + input())
print('The wolf growls and readys attack. What do you want to do?')
print('a) ATTACK!')
print('b) BLOCK!')
print('c) RUN!')
answer = input()
if answer == 'a':
    
    
    character_attack = ( character_weapon_stats['attack'] * character_base_stats['strength'] )
    enemy_block = (enemy_weapon_stats['defense'] * enemy_base_stats['strength'])
    #print(character_attack)
    #print(enemy_block)
    outcome = (character_attack - enemy_block)//10
    #print(outcome)
    enemy_health = enemy_health - outcome
    print('Success!')
    print('Your health is: ' + str(character_health))
    print('Your enemy health is: ' + str(enemy_health))
    input()
else:
    pass



