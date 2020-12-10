import re


def read_input():
    with open('input') as f:
        lines = re.split(r'\n\n', f.read(), flags=re.MULTILINE)
    return lines


def main1():
    return sum(len(set(line.replace('\n', ''))) for line in read_input())


def main2():
    pass


def main(task):
    return {1: main1, 2: main2}[task]()


if __name__ == '__main__':
    print(main(1))
