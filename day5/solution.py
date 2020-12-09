def main1():
    pass


def main2():
    pass


def main(task):
    return {1: main1, 2: main2}[task]()


if __name__ == '__main__':
    print(main(2))
