def read_file(file='input.txt'):
    return open(file, 'r').read()


def get_lines(file='input.txt'):
    return [line.strip() for line in open(file, 'r').readlines()]


def n_str(n: int, length: int) -> str:
    r = str(n)
    for i in range(length - 1):
        r += str(n)
    return r


def get_matrix(file='input.txt'):
    matrix = [line.split() for line in get_lines(file)]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            try:
                matrix[i][j] = int(matrix[i][j])
            except:
                pass
    return matrix


def invert_matrix(matrix):
    new_matrix = [[] for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        row = matrix[i]
        for j in range(len(row)):
            new_matrix[j].append(row[j])
    return new_matrix


def char_matrix(lines):
    return [[char for char in line] for line in lines]

