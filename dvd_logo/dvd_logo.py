"""Отскакивающий от краев логотип DVD, (c) Эл Свейгарт al@inventwithpython.com
Анимация отскакивающего логотипа DVD. Оценить ее по достоинству могут
только люди "определенного возраста". Для останова нажмите Ctrl+C.

Примечание: не меняйте размера окна терминала во время работы программы.
Код размещен на https://nostarch.com/big-book-small-python-projects
Теги: короткая, графика, bext"""

import sys
import random

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Задаем константы:
WIDTH, HEIGHT = bext.size()
# В Windows нельзя вывести символ в последний столбец без добавления
# автоматически символа новой строки, так что уменьшаем ширину на 1:
WIDTH -= 1

NUMBER_OF_LOGOS = 5  # (!) Попробуйте заменить на 1 или 100.
PAUSE_AMOUNT = 0.2  # (!) Попробуйте заменить на 1.0 или 0.0.
# (!) Попробуйте уменьшить количество цветов в этом списке:
COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

UP_RIGHT = 'ur'
UP_LEFT = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT = 'dl'
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)

"""Генерация логотипов"""


class Logo:
    """Генерация самого лого"""
    def __init__(self):
        self.color = random.choice(COLORS)
        self.x = random.randint(1, WIDTH - 4)
        self.y = random.randint(1, HEIGHT - 4)
        self.direction = random.choice(DIRECTIONS)

        if self.x % 2 == 1:
            # Гарантируем, что x четное число, для столкновения с углом.
            self.x -= 1

        if self.y >= HEIGHT:
            self.y = HEIGHT - 2

    def move(self):
        """Перемещаем логотип. (Координата x меняется на 2, поскольку
        в терминале высота символов вдвое превышает ширину.)"""
        if self.direction == UP_RIGHT:
            self.x += 2
            self.y -= 1
        elif self.direction == UP_LEFT:
            self.x -= 2
            self.y -= 1
        elif self.direction == DOWN_RIGHT:
            self.x += 2
            self.y += 1
        elif self.direction == DOWN_LEFT:
            self.x -= 2
            self.y += 1
            # Проверяем, чтобы Y не был отрицательным
        if self.y < 0:
            self.y = 0
        elif self.y >= HEIGHT:
            self.y = HEIGHT - 1

    def bounce(self):
        """Проверяем, не отскакивает ли логотип от угла"""
        if self.x == 0 and self.y == 0:
            self.direction = DOWN_RIGHT

        elif self.x == 0 and self.y == HEIGHT - 1:
            self.direction = UP_RIGHT

        elif self.x == WIDTH - 3 and self.y == 0:
            self.direction = DOWN_LEFT

        elif self.x == WIDTH - 3 and self.y == HEIGHT - 1:
            self.direction = UP_LEFT

        # Проверяем, не отскакивает ли логотип от левого края:
        elif self.x == 0 and self.direction == UP_LEFT:
            self.direction = UP_RIGHT
        elif self.x == 0 and self.direction == DOWN_LEFT:
            self.direction = DOWN_RIGHT

        # Проверяем, не отскакивает ли логотип от правого края:
        # (WIDTH - 3, поскольку 'DVD' состоит из трех букв.)
        elif self.x >= WIDTH - 3 and self.direction == UP_RIGHT:
            self.direction = UP_LEFT
        elif self.x >= WIDTH - 3 and self.direction == DOWN_RIGHT:
            self.direction = DOWN_LEFT

        # Проверяем, не отскакивает ли логотип от верхнего края:
        elif self.y == 0 and self.direction == UP_LEFT:
            self.direction = DOWN_LEFT
        elif self.y == 0 and self.direction == UP_RIGHT:
            self.direction = DOWN_RIGHT

        # Проверяем, не отскакивает ли логотип от нижнего края:
        elif self.y == HEIGHT - 1 and self.direction == DOWN_LEFT:
            self.direction = UP_LEFT
        elif self.y == HEIGHT - 1 and self.direction == DOWN_RIGHT:
            self.direction = UP_RIGHT

    def change_color(self):
        """Меняем цвет при отскакивании логотипа"""
        self.color = random.choice(COLORS)
