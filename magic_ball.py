import random


print('Привет! Я предсказатель!\n')
user_name = input('Как тебя зовут?\n')
print(f'Привет! {user_name}')


list_answer = ['Бесспорно', 'Предрешено', 'Никаких сомнений',
               'Определённо да', 'Можешь быть уверен в этом', 'Мне кажется - да', 'Вероятнее всего',
               'Хорошие перспективы', 'Знаки говорят - да', 'Да', 'Пока неясно, попробуй снова',
               'Спроси позже', 'Сейчас нельзя предсказать', 'Даже не думай', 'Мой ответ - нет',
               'По моим данным - нет', 'Перспективы не очень хорошие']


def is_valid_input(user_input):
    return any(char.isalpha() for char in user_input) and any(char.isspace() for char in user_input)


def get_user_input():
    user_input = input('Введите ваш вопрос, а я попробую предсказать:\n')

    while not is_valid_input(user_input):
        user_input = input('Пожалуйста, задайте осмысленный вопрос:\n')

    return user_input


def game_start():
    get_user_input()
    count = 1
    flag = False
    while True:
        answer = random.choice(list_answer)
        print(f'Вот ответ: {answer}')
        second_quest = input('Хотите ещё задать вопрос? Введите Да или Нет\n')
        if second_quest.lower() == 'да':
            game_start()

        elif second_quest.lower() == 'нет':
            print('До свидания')
            break
        else:
            print('Введите корректно...')


game_start()
