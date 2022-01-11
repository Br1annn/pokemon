#pokemon game
import random
import math
#pick starter
starter = input('Choose your starter: \nCharmander\nBulbasaur\nSquirtle\n')
health = 100
dmg = 0
starter_health = 100
dmg_inc = 1
ran_dmg = random.randint(1,3)

#attribute assignment
if starter.lower() == 'charmander':
    attribute = 'fire'
    moveset = ['1. Scratch', '2. Growl', '3. Ember', '4. Fire Fang']
    print('\nYou have encountered a wild Pokemon!\n')

    print('A wild Pidgeot has appeared!')
    print('\nGo ' + starter.capitalize() + '!\n')
    
    #for dmg in health:
    while True:
        print('What is',starter.capitalize(),'going to use?')
        attack = input('\n'.join(moveset) + '\n') 
        print (dmg_inc,'dmg increase')
        if attack == '1':
            dmg = random.randint(8,10)
            print('You did', dmg, 'damage with Scratch!')
            health = health - (dmg + (dmg*dmg_inc))
            
        if attack == '2':
            dmg_inc = dmg_inc * ran_dmg
            print('Your damage has increased',ran_dmg/10,'%')

        if attack == '3':
            dmg = random.randint(10,15)
            print('You did ', dmg, ' damage with Ember!')
            health = health - (dmg + (dmg*dmg_inc))

        if attack == '4':
            dmg = random.randint(18,22)
            print('You did ', dmg, ' damage with Fire Fang!')
            health = health - (dmg + (dmg*dmg_inc))
        print('Pidgeot has ', health , ' health left!\n')

        if health < 0:
            health == 0
            print('Pidgeot has fainted.')
            break

        #pidgeot damage
        starter_dmg = random.randint(1,15)
        print('Pidgeot has done', starter_dmg, 'damage to your', starter)
        starter_health = starter_health - starter_dmg
        print(starter.capitalize(),' has', starter_health, ' health left!\n')
        
        if starter_health <= 0:
            print('Oh no',starter.capitalize(),'has fainted.')
            break

            







