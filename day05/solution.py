from util import *
from functools import cmp_to_key


def load(file):
    data = read_file(file)
    data = data.split('\n\n')
    rules = [[int(page) for page in rule.split('|')] for rule in data[0].split('\n')]
    updates = [[int(page) for page in update.split(',')] for update in data[1].split('\n')]
    return rules, updates


def sort_updates(rules, updates):
    correct_updates = []
    incorrect_updates = []
    for update in updates:
        flag = False
        for i in range(len(update)):
            for j in range(i + 1, len(update)):
                if [update[j], update[i]] in rules:
                    flag = True
                    break
            if flag:
                break
        if flag:
            incorrect_updates.append(update)
        else:
            correct_updates.append(update)
    return correct_updates, incorrect_updates


def part1(file):
    rules, updates = load(file)
    correct_updates = sort_updates(rules, updates)[0]
    correct_updates = [update[len(update) // 2] for update in correct_updates]
    print(sum(correct_updates))


part1('example.txt')
part1('input.txt')


def part2(file):
    rules, updates = load(file)
    incorrect_updates = sort_updates(rules, updates)[1]

    def compare(a, b):
        if [a, b] in rules:
            return -1
        elif [b, a] in rules:
            return 1
        else:
            return 0

    fixed_updates = [sorted(update, key=cmp_to_key(compare)) for update in incorrect_updates]
    fixed_updates = [update[len(update) // 2] for update in fixed_updates]
    print(sum(fixed_updates))


part2('example.txt')
part2('input.txt')
