import numpy as np
from PIL import Image

FIELD_LENGTH = 1024
FIELD_WIDTH = 1024
START_POSITION = (512, 512)


def main(length, width, start):
    ant_position = np.array(start)  # задали стартовую позицию
    current_direction = 0  # 0: вверх, 1: направо, 2: вниз, 4: налево
    directions = np.array([[-1, 0], [0, 1], [1, 0], [0, -1]])  # шаг в определённом направлении
    field = np.ones((length, width), dtype=bool)  # создали поле
    black_count = 0  # счётчик чёрных клеток

    while 0 <= ant_position[0] < length and 0 <= ant_position[1] < width:
        is_white_cell = field[tuple(ant_position)]  # определили цвет клетки
        if is_white_cell:
            current_direction = (current_direction + 1) % 4  # повернули по часовой стрелке
            field[tuple(ant_position)] = False  # инвертировали цвет
            black_count += 1  # посчитали клетку
        else:
            current_direction = (current_direction - 1) % 4  # повернули против часовой стрелки
            field[tuple(ant_position)] = True  # инвертировали цвет
            black_count -= 1  # посчитали клетку
        ant_position = (ant_position + directions[current_direction])  # сделали шаг

    img = Image.fromarray(field)  # преобразовали в изображение
    img.save('solution.png')  # сохранили изображение
    print(f'Количество черных клеток: {black_count}')


if __name__ == '__main__':
    main(FIELD_LENGTH, FIELD_WIDTH, START_POSITION)
