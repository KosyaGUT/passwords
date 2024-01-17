from random import choice
import string


class Password:

    long_ps: int  # длинна пароля
    level_ps: str  # сложность пароля
    special_characters: int  # нужны ли спецсимволы
    symbols: str  # символы

    def __init__(self, long: int, level: str, spec_char: int, symbols: str):
        self.long_ps = long
        self.level_ps = level
        self.special_characters = spec_char
        self.symbols = symbols

    def generator_passw(self):
        password = ''
        for _ in range(self.long_ps):
            password += choice(self.symbols)
        print("Вот ваш пароль: ", password)


def check_param():
    global symbols
    while True:
        long = input('Введите длину пароля (max: 24): ')

        if long.isalpha():
            print("Не нужно вводить текст (^._.^)/")
            continue
        if 8 < int(long) <= 24:
            break
        else:
            print("Введите число из диапазона от 8 до 24")
            continue

    while True:
        level = input('Выберите сложность пароля простая/средняя/сложная: ').capitalize()
        if level not in ['Простая', 'Средняя', 'Сложная']:
            print("Постарайтесь вводить без цифр и без ошибок")
            continue
        elif level == 'Простая':
            symbols = string.ascii_letters
            break
        elif level == 'Средняя':
            symbols = string.ascii_letters + string.digits
            break
        else:
            symbols = string.ascii_letters + string.digits + string.punctuation
            break

    while True:
        spec_char = int(input('Напишите 1 если хотите использовать спец. символы, 0 если нет: '))
        if spec_char == 1:
            if level != 'Сложная':
                symbols = string.ascii_letters + string.digits + string.punctuation
            break
        elif spec_char == 0:
            pass
            break
        else:
            print('Введите либо 0, либо 1')
            continue
    return int(long), level, spec_char, symbols


def main():
    param = check_param()
    ps = Password(*param)
    ps.generator_passw()


if __name__ == '__main__':
    main()