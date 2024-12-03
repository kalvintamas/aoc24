import re
from util import *


def part1(file):
    data = read_file(file)
    data = re.findall(r'((?:(?<=mul\()(?:\d{1,3},\d{1,3})(?=\)))|(?:do\(\))|(?:don\'t\(\)))', data)
    enabled = True
    sum = 0
    for match in data:
        if match == "do()":
            enabled = True
        elif match == "don't()":
            enabled = False
        elif enabled:
            factors = [int(item) for item in match.split(",")]
            sum += factors[0] * factors[1]
    print(sum)


part1('example2.txt')
part1('input.txt')
