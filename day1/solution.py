def read_expenses():
    with open('input') as f:
        lines = f.readlines()
    expenses = [int(i) for i in lines]
    return expenses


def main1():
    expenses = read_expenses()
    search_value = 2020
    expenses.sort()
    min_value = expenses[0]
    # filter out too big values
    expenses = [i for i in expenses if search_value >= i + min_value]
    for i in expenses:
        if search_value - i in expenses:
            return i * (search_value - i)


def main2():
    expenses = read_expenses()
    search_value = 2020
    expenses.sort()
    min_value = expenses[0] + expenses[1]
    # filter out too big values
    expenses = [i for i in expenses if search_value >= i + min_value]
    for pos, val in enumerate(expenses):
        for i in expenses[pos:]:
            s = i + val
            if search_value - s in expenses:
                return i * val * (search_value - s)


def main(task):
    return {1: main1, 2: main2}[task]()


if __name__ == '__main__':
    print(main(2))
