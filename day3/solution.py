from functools import reduce


def read_input():
    with open('input') as f:
        lines = f.read().splitlines()
    return lines


def main1(right=3, down=1):
    lines = read_input()
    tree = '#'
    pos = right
    found = 0
    for line in lines[down::down]:
        if line[pos] == tree:
            found += 1
        pos = (pos + right) % len(line)
    return found


def main2():
    params = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    res = [main1(*p) for p in params]
    return reduce((lambda x, y: x * y), res)


def main(task):
    return {1: main1, 2: main2}[task]()


if __name__ == '__main__':
    print(main(2))
