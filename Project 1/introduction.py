import random
import copy
import time
import sys


# функция медленного ввода текста
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
            slow_print(f'Ты нашёл {item}!\n')

        if event == events[0]:
            random_enemy = random.choice(enemies)
            enemy_copy = copy.deepcopy(random_enemy)
            user_hp = fight(enemy_copy, user_hp)

        if event == events[2]:
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

# Список противников
enemies = [enemy_zombie, enemy_solder]


def fight(enemy, user_hp):  # БОЕВАЯ СИСТЕМА
    while enemy['hp'] > 0 and user_hp > 0:
        # удар игрока
        enemy['hp'] -= 15
        slow_print(
            f"Ты ударил {enemy['name']}! У него осталось {enemy['hp']} HP")

        # удар противника
        if enemy['hp'] > 0:
            user_hp -= enemy['damage']
            slow_print(
                f"{enemy['name']} ударил тебя! У тебя осталось {user_hp} HP")

        print()

    if user_hp <= 0:
        slow_print('...YOU DIED...')
    else:
        slow_print(f"{enemy['name']} повержен!")

    return user_hp


game(hp, invent)
