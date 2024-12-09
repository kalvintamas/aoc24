import enum
import re
from unittest import case

from util import *


class Dir(enum.Enum):
    UP = 'UP',
    RIGHT = 'RIGHT',
    DOWN = 'DOWN',
    LEFT = 'LEFT',


DIR = {
    '^': Dir.UP,
    '>': Dir.RIGHT,
    'ˇ': Dir.DOWN,
    '<': Dir.LEFT,
}


def turn_right(d: Dir):
    match d:
        case Dir.UP:
            return Dir.RIGHT
        case Dir.RIGHT:
            return Dir.DOWN
        case Dir.DOWN:
            return Dir.LEFT
        case Dir.LEFT:
            return Dir.UP


def bound(matrix, x, y):
    return x in range(len(matrix)) and y in range(len(matrix[0]))


def check(matrix, x, y):
    return matrix[x][y] != '#'


def part1(file):
    matrix = char_matrix(get_lines(file))
    print(matrix)
    x, y = -1, -1
    d: Dir
    for i, row in enumerate(matrix):
        for j, item in enumerate(row):
            if item in DIR:
                x, y = i, j
                d = DIR[item]
                break
    if not d:
        print('error')
        return
    while bound(matrix, x, y):
        match d:
            case Dir.UP:
                if check(matrix, x, y):
                    matrix[x][y] = 'X'
                else:
                    d = turn_right(d)




part1('example.txt')
part1('input.txt')
