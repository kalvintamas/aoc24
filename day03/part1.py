import re
from util import *


def part1(file):
    data = read_file(file)
    data = re.findall(r'(?<=mul\()(\d{1,3},\d{1,3})(?=\))', data)
    data = [item.split(',') for item in data]
    data = [int(item[0]) * int(item[1]) for item in data]
    data = sum(data)
    print(data)


part1('example1.txt')
part1('input.txt')
