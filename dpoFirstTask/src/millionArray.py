import random


def initListWithRandomNumbers():
    rand_list = []

    n = 1000000

    for i in range(n):
        rand_list.append(random.randint(0, 999))

    return rand_list
