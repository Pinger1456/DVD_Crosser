"""Отскакивающий от краев логотип DVD, (c) Эл Свейгарт al@inventwithpython.com
Анимация отскакивающего логотипа DVD. Оценить ее по достоинству могут
только люди "определенного возраста". Для останова нажмите Ctrl+C.

Примечание: не меняйте размера окна терминала во время работы программы.
Код размещен на https://nostarch.com/big-book-small-python-projects
Теги: короткая, графика, bext"""

import sys

from dvd_animation import DVDAnimation

if __name__ == '__main__':
    animation = DVDAnimation(num_logos=5)
    try:
        animation.run()
    except KeyboardInterrupt:
        print()
        print('Bouncing DVD Logo, by Al Sweigart')
        sys.exit()  # При нажатии Ctrl+C завершаем выполнение программы.
