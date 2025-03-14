import random


print('Welcome')


def is_valid(num):  # провека ввода пользователя
    if not num.isdigit():
        return False
    if int(num) not in range(1, int(right) + 1):
        return False
    return True


def is_valid_right(num):  # проверка пользовательской правой границы
    if not num.isdigit():
        return False
    if int(num) < 2:
        return False
    return True


def game_start():
    global right
    right = input(
        'Введите правую границу, до которой я могу загадать число: \n')

    while not is_valid_right(right):
        right = input(
            'Нужно ввести натуральное число от двух до бесконечности! Попробуйте ещё. \n')

    right = int(right)
    random_number = random.randint(1, right)
    count = 1

    while True:
        num = input(f'\nПопытка №{count}. Введите число от 1 до {right}. \n')

        while not is_valid(num):
            num = input(
                f'Вы не правильн вводите число. Нужно ввести число от 1 до {right}.\n')

        num = int(num)
        count += 1

        if num < random_number:
            print('\nЧисло меньше загаданного, попробуйте ещё.')
        elif num > random_number:
            print('\nЧисло больше загаданного, попробуйте ещё.')
        else:
            print('Ты угадал! Хочешь ещё? Напиши либо "Да" либо "Нет".')
            again = input()

            while again.lower() not in ['да', 'нет']:
                again = input(
                    'Ты не праивльно ввел, введи либо Да либо Нет: \n')

            if again.lower() == 'да':
                game_start()
            else:
                print('\nПокеда')
            break


game_start()
