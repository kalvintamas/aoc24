from util import *


def safe(row):
    for j in range(len(row) - 1):
        val = row[j] - row[j + 1]
        if row[0] < row[1]:
            val *= -1
        if val not in (1, 2, 3):
            return False
    return True


def part2(file):
    data = get_matrix(file)
    # reverse loop to enable removal
    for i in range(len(data))[::-1]:
        row = data[i]
        idx = safe(row)
        if not safe(row):
            can_be = False
            for j in range(len(row)):
                if safe(row[:j] + row[j + 1:]):
                    can_be = True
                    break
            if not can_be:
                data.pop(i)
    print(len(data))


part2('example.txt')
part2('input.txt')

