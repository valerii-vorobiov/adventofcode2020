def read_input():
    with open('input') as f:
        lines = f.read().splitlines()
    return lines


def main1():
    lines = read_input()
    return max(get_place_number(line) for line in lines)


def get_place_number(line):
    row = get_boundaries(0, 127, list(line)[::-1][-7:])
    column = get_boundaries(0, 7, list(line)[::-1][:-7])
    return (row * 8) + column


def get_boundaries(_min, _max, letters):
    while letters:
        letter = letters.pop()
        middle = _min + (_max - _min) // 2
        return get_boundaries(middle + 1, _max, letters) \
            if letter in ('B', 'R') \
            else get_boundaries(_min, middle, letters)
    return _min


def main2():
    pass


def main(task):
    return {1: main1, 2: main2}[task]()


if __name__ == '__main__':
    print(main(1))
