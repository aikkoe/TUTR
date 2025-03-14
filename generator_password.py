import random


DIGITS = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
SYMBOLS = '!#$%&*+-=?@^_'

chars = ''

count = int(input(
    'Введите кол-во требуемых паролей: \n'))
leng_pass = int(input(
    'Введите длину пароля: \n'))
digits = input(
    'Включать ли цифры "0123456789"? Ответьте "да" или "нет"\n')
upcase = input(
    'Включать ли прописные буквы "ABCDEFGHIJKLMNOPQRSTUVWXYZ"? Ответьте "да" или "нет"\n')
lowercase = input(
    'Включать ли строчные буквы "abcdefghijklmnopqrstuvwxyz"? Ответьте "да" или "нет"\n')
symbols = input(
    'Включать ли символы "!#$%&*+-=?@^_"? Ответьте "да" или "нет"\n')
excep = input(
    'Исключать ли неоднозначные символы "il1Lo0O"? Ответьте "да" или "нет"\n')


if digits.lower() == 'да':
    chars += DIGITS

if upcase.lower() == 'да':
    chars += UPPERCASE_LETTERS

if lowercase.lower() == 'да':
    chars += LOWERCASE_LETTERS

if symbols.lower() == 'да':
    chars += SYMBOLS

if excep.lower() == 'да':
    for _ in 'il1Lo0O':
        chars.replace(_, '')


def generate_password(leng, char):
    result = ''
    for _ in range(count):
        for _ in range(leng):
            result += random.choice(char)
        result += '\n'
    return result


print(generate_password(leng_pass, chars))

