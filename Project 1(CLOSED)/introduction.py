import random
import copy
import time
import sys
import re
from colorama import init, Fore, Style


#  Инициализирую библеотеку
#  Это нужно, так как модуль colorama работает в терминале для вывода цветного текста
init(autoreset=True)


# функция медленного вывода текста
def slow_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


print('####################')
slow_print('#     RPG GAME     #')
print('####################')

# ИНФОРМАЦИЯ О ИГРОКЕ
USER_NAME = input('\nПриветствую! Введите своё имя: ')
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
        slow_print(
            f'\n{USER_NAME}, перед тобой следующие места: \n1.{LOCATIONS[0]} \n2.{LOCATIONS[1]} \n3.{LOCATIONS[2]}')

        while True:  # выбор локации
            user_choice = input('\nВыбери куда отправишься(1, 2 или 3): ')
            if user_choice in ['1', '2', '3']:
                break
            else:
                print('Введи число 1, 2 или 3!')

        slow_print(f'\nТы прибыл в {LOCATIONS[int(user_choice)-1]}\n')

        event = random.choice(events)
        slow_print(event)
        print()

        if event == events[1]:  # выпадение рандомного предмета
            item = random.choice(items)
            user_invent.append(item)
            slow_print(f'Ты нашёл:')
            print(Fore.YELLOW + item)
            print()
        elif event == events[0]:  # инвент с боем
            random_enemy = random.choice(enemies)
            enemy_copy = copy.deepcopy(random_enemy)
            user_hp, user_invent = fight(enemy_copy, user_hp, user_invent)
        elif event == events[2]:  # ивент коста
            user_hp = 100
            slow_print('Ты восстановил здоровье!\n')

        print(f'HP: {user_hp}')
        print(f'Инвентарь: {user_invent}\n')

        while True:  # проверка для продолжения или выхода
            choice = input('Хотите продолжить?(да или нет): ').lower()
            if choice == 'нет':
                slow_print('\nПокойся с миром...')
                exit()
            elif choice == 'да':
                break
            else:
                print('Нужно ввести да или нет!\n')

    return user_hp, user_invent


# ПРОТИВНИКИ
enemy_zombie = {
    "name": "Zombie",
    "hp": 25,
    "damage": 10
}

enemy_solder = {
    "name": "Solder",
    "hp": 40,
    "damage": 15
}

enemy_king = {
    "name": "King",
    "hp": 100,
    "damage": 20
}

# Список противников
enemies = [enemy_zombie, enemy_solder, enemy_king]


def fight(enemy, user_hp, user_invent):  # БОЕВАЯ СИСТЕМА
    slow_print(f"Ты встретил {enemy['name']}!")
    while enemy['hp'] > 0 and user_hp > 0:
        slow_print(f'Он приближается к тебе...\n')
        slow_print(f'Ты 1.Атакуешь или 2.Бежишь?')
        user_choice = input()
        if user_choice == '1':
            slow_print(f"\nТы атакуешь {enemy['name']}!")
            enemy['hp'] -= 15
            slow_print(f"\nУ врага осталось {enemy['hp']} HP")
            slow_print(f"\nВраг атакует тебя!")
            # подсчет кол-ва урона врага
            enemy_damage = enemy['damage'] + (random.randint(-5, 5))
            user_hp -= enemy_damage

            # крит - если урон врага превышает базовый урон на 3
            if enemy_damage > enemy['damage'] + 3:
                slow_print(f'Враг нанёс критический удар!')

            slow_print(f"\nУ тебя осталось {user_hp} HP\n")
        elif user_choice == '2':
            slow_print(f"\nТы убегаешь от {enemy['name']}!")
            break
        else:
            print('Нужно ввести 1 или 2!')

    if user_hp <= 0:
        slow_print('...YOU DIED...')
        exit()
    elif user_choice == '2':  # type: ignore
        slow_print(f"\nТы теряешь 10 HP во время побега!")
        user_hp -= 10
        slow_print(f"\nУ тебя осталось {user_hp} HP\n")
    else:
        item = random.choice(items)
        user_invent.append(item)
        slow_print(f'Ты получил с врага {item}!\n')
        slow_print(f"{enemy['name']} повержен!")

    return user_hp, user_invent


game(hp, invent)
