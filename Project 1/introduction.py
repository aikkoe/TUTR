import random


print('####################')
print('#     RPG GAME     #')
print('####################')
# ИНФОРМАЦИЯ О ИГРОКЕ
USER_NAME = input('\nПриветсвую! Введите своё имя: ')
hp = 100  # healt
invent = []  # inventory

# СПИСОК ЛОКАЦИЙ
LOCATIONS = ['Anor-Londo', 'Jopa-boli', 'Bolotishko']

# СПИСОК СОБЫЙТИЙ
events = ['Засада!', 'Найден предмет!', 'Ты встретил костёр и отдыхаешь.']

# СПИСОК ПРЕДМЕТОВ
items = ["Эстус", "Осколок титанита", "Кусок мха", "Ключ от клетки", "Меч"]


def game(user_hp, user_invent):
    while True:
        # ТЕЛО ИГРЫ
        print(
            f'\n{USER_NAME}, перед тобой следующие места: \n1.{LOCATIONS[0]} \n2.{LOCATIONS[1]} \n3.{LOCATIONS[2]}')

        while True:  # выбор локации
            user_choice = input('\nВыбери куда отправишься(1, 2 или 3): ')
            if user_choice in ['1', '2', '3']:
                break
            else:
                print('Введи число 1, 2 или 3!')

        print(f'\nТы прибыл в {LOCATIONS[int(user_choice)-1]}\n')

        event = random.choice(events)
        print(event)
        print()

        if event == events[1]:  # выпадение рандомного предмета
            item = random.choice(items)
            user_invent.append(item)
            print(f'Ты нашёл {item}!\n')

        if event == events[0]:
            user_hp -= 20
            print('Ты получил 20 урона!\n')
            if user_hp <= 0:
                print('...YOU DIED...')
                break

        if event == events[2]:
            user_hp = 100
            print('Ты восстановил здоровье!\n')

        print(f'HP: {user_hp}')
        print(f'Инвентарь: {user_invent}\n')

        while True:  # проверка для продолжения или выхода
            user_choice_v2 = input('Хотите продолжить?(да или нет): ')
            if user_choice_v2.lower() == 'нет':
                print('\nПокойся с миром...')
                exit()
            elif user_choice_v2 not in ['да', 'нет']:
                print('Нужно ввести да или нет!\n')
            break

    return user_hp, user_invent


game(hp, invent)
