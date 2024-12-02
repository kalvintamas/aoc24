from util import *


def safe(asc, a, b):
    if asc != a < b:
        return False
    val = a - b
    if asc:
        val *= -1
    return val in (1, 2, 3)


def part1(file):
    data = get_matrix(file)
    # reverse loop to enable removal
    for i in range(len(data))[::-1]:
        check(data, i)
    print(len(data))


def check(data, i):
    row = data[i]
    asc = row[0] < row[1]
    for j in range(len(row) - 1):
        val = row[j] - row[j + 1]
        if asc:
            val *= -1
        if val not in (1, 2, 3):
            data.pop(i)


part1('example.txt')
part1('input.txt')
