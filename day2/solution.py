def read_input():
    with open('input') as f:
        lines = f.readlines()
    lines = [parse_line(i) for i in lines]
    return lines


def parse_line(line):
    lines, letter, password = line.split(' ')
    lines = [int(i) for i in lines.split('-')]
    letter = letter[:-1]
    return lines, letter, password


def validate1(lines, letter, password):
    return lines[0] <= password.count(letter) <= lines[1]


def main1():
    passwords = read_input()
    return len([1
                for lines, letter, password in passwords
                if validate1(lines, letter, password)])


def validate2(lines, letter, password):
    return (password[lines[0]-1] == letter) != (password[lines[1]-1] == letter)


def main2():
    passwords = read_input()
    return len([1
                for lines, letter, password in passwords
                if validate2(lines, letter, password)])


def main(task):
    return {1: main1, 2: main2}[task]()


if __name__ == '__main__':
    print(main(2))
