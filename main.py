import numpy as np
from PIL import Image

FIELD_LENGTH = 1024
FIELD_WIDTH = 1024
START_POSITION = (512, 512)


def main(length, width, start, filename):
    ant_position = np.array(start)
    current_direction = 0  # 0: вверх, 1: направо, 2: вниз, 4: налево
    directions = np.array([[-1, 0], [0, 1], [1, 0], [0, -1]])  # шаг в определённом направлении
    field = np.ones((length, width), dtype=bool)
    black_count = 0

    while 0 <= ant_position[0] < length and 0 <= ant_position[1] < width:
        is_white_cell = field[tuple(ant_position)]
        if is_white_cell:
            current_direction = (current_direction + 1) % 4
            field[tuple(ant_position)] = False
            black_count += 1
        else:
            current_direction = (current_direction - 1) % 4
            field[tuple(ant_position)] = True
            black_count -= 1
        ant_position = (ant_position + directions[current_direction])

    img = Image.fromarray(field)
    img.save(filename)
    print(f'Количество черных клеток: {black_count}')


if __name__ == '__main__':
    main(FIELD_LENGTH, FIELD_WIDTH, START_POSITION, 'solution.png')
