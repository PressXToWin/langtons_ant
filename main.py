import numpy as np
from PIL import Image

FIELD_LENGTH = 10
FIELD_WIDTH = 10
START_POSITION = (5, 5)


def main(length, width, start):
    ant_position = np.array(start)
    current_direction = 0
    directions = np.array([[-1, 0], [0, 1], [1, 0], [0, -1]])
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
    img.save('solution.png')
    print(black_count)


if __name__ == '__main__':
    main(FIELD_LENGTH, FIELD_WIDTH, START_POSITION)
