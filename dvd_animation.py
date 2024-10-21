"""Импортируем мз Dvd_Logo все компоненты для анимации"""
import sys
import time
import bext
from dvd_logo import dvd_logo


class DVDAnimation:
    """Класс для управления анимацией."""
    def __init__(self, num_logos):
        self.logos = [dvd_logo.Logo() for _ in range(num_logos)]
        # Считаем, сколько раз логотип столкнулся с углом.
        self.corner_bounces = 0

    def run(self):
        """Запускаем анимацию."""
        bext.clear()

        # Основной цикл программы.
        while True:
            # Обрабатываем все логотипы в списке логотипов.
            for logo in self.logos:
                # Очищаем место, где ранее находился логотип:
                bext.goto(logo.x, logo.y)
                print('   ', end='')
                # Запоминаем текущее направление перед движением:

                original_direction = logo.direction

                # Обрабатываем столкновения с границами:
                logo.bounce()

                # Если направление изменилось, меняем цвет логотипа:
                if logo.direction != original_direction:
                    logo.change_color()
                    if logo.x in {0, dvd_logo.WIDTH - 3} and \
                            logo.y in {0, dvd_logo.HEIGHT - 1}:
                        self.corner_bounces += 1

                # Перемещаем логотип
                logo.move()

        # Отображаем количество отскакиваний от углов:
            bext.goto(5, 0)
            bext.fg('white')
            print('Corner bounces:', self.corner_bounces, end='')

            for logo in self.logos:
                # Отрисовываем логотипы на новом месте:
                bext.goto(logo.x, logo.y)
                bext.fg(logo.color)
                print('DVD', end='')

            bext.goto(0, 0)
            sys.stdout.flush()  # Нужно для программ, использующих модуль bext.
            time.sleep(dvd_logo.PAUSE_AMOUNT)

    @staticmethod
    def stop():
        """Останавливаем анимацию."""
        print('Animation stopped.')
