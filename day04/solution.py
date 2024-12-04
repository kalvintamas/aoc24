from util import *
import re

LOOKUP = 'XMAS'


def search(lookup, line):
    matches = 0
    pattern = '(?=(' + lookup + '))'
    result = re.findall(pattern, line)
    matches += len(result)
    # print(result, end=' ')
    pattern = '(?=(' + lookup[::-1] + '))'
    result = re.findall(pattern, line)
    # print(result)
    matches += len(result)
    return matches


def left_diameter(matrix):
    result = []
    for j in range(len(matrix[0]))[::-1]:
        i = 0
        line = []
        while j < len(matrix) and i < len(matrix[0]):
            line.append(matrix[i][j])
            i += 1
            j += 1
        if len(line):
            result.append(line)
    for i in range(1, len(matrix)):
        j = 0
        line = []
        while j < len(matrix) and i < len(matrix[0]):
            line.append(matrix[i][j])
            i += 1
            j += 1
        if len(line):
            result.append(line)
    return result


def right_diameter(matrix):
    result = []
    for i in range(len(matrix)):
        j = 0
        line = []
        while j < len(matrix[0]) and i >= 0:
            line.append(matrix[i][j])
            i -= 1
            j += 1
        if len(line):
            result.append(line)
    for j in range(1, len(matrix)):
        i = len(matrix) - 1
        line = []
        while j < len(matrix[0]) and i >= 0:
            line.append(matrix[i][j])
            i -= 1
            j += 1
        if len(line):
            result.append(line)
    return result


def part1(file, lookup=LOOKUP):
    matches = 0
    lines = get_lines(file)
    for line in lines:
        matches += search(lookup, line)
    lines = [''.join(line) for line in invert_matrix(lines)]
    for line in lines:
        matches += search(lookup, line)
    rd_lines = [''.join(line) for line in right_diameter(char_matrix(lines))]
    for line in rd_lines:
        matches += search(lookup, line)
    ld_lines = [''.join(line) for line in left_diameter(char_matrix(lines))]
    for line in ld_lines:
        matches += search(lookup, line)
    print(matches)


part1('example.txt')
part1('input.txt')


def part2(file):
    matrix = char_matrix(get_lines(file))
    matches = 0
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[0]) - 1):
            left = ((matrix[i - 1][j - 1], matrix[i + 1][j + 1]) in [('M', 'S'), ('S', 'M')])
            right = ((matrix[i - 1][j + 1], matrix[i + 1][j - 1]) in [('M', 'S'), ('S', 'M')])
            if matrix[i][j] == 'A' and left and right:
                matches += 1
    print(matches)


part2('example.txt')
part2('input.txt')














