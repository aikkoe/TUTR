import random


print('####################')
print('#     RPG GAME     #')
print('####################')
# ИНФОРМАЦИЯ О ИГРОКЕ
USER_NAME = input('\nПриветсвую! Введите своё имя: ')
USER_HP = 100  # healt
USER_MP = 100  # mana
USER_INVENT = []  # inventory

# СПИСОК ЛОКАЦИЙ
LOCATIONS = ['Anor-Londo', 'Jopa-boli', 'Bolotishko']

# СПИСОК СОБЫЙТИЙ
event = ['Засада!', 'Найден предмет!', 'Ты встретил костёр и отдыхаешь.']


def game():
    while True:
        # ТЕЛО ИГРЫ
        print(
            f'\n{USER_NAME}, перед тобой следующие места: \n1.{LOCATIONS[0]} \n2.{LOCATIONS[1]} \n3.{LOCATIONS[2]}')

        while True:
            user_choice = input('\nВыбери куда отправишься(1, 2 или 3): ')
            if user_choice in ['1', '2', '3']:
                break
            else:
                print('Введи число 1, 2 или 3!')

        print(f'\nТы прибыл в {LOCATIONS[int(user_choice)-1]}\n')

        print(random.choice(event))
        print()

        user_choice_v2 = input('Хотите продолжить?(да или нет): ')
        if user_choice_v2.lower() == 'нет':
            print('\nПокойся с миром...')
            break


game()
