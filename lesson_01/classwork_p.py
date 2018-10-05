import random


def func(string):
    t = tuple(ord(i) for i in string)
    return tuple(t)


def random_digit(x):
    list_random = []
    dict_dig = {}
    for i in range(50):
        list_random.append(random.random())
    dict_dig['after'] = [dig for dig in list_random if dig > x]
    dict_dig['before'] = [dig for dig in list_random if dig <= x]
    return dict_dig


print(random_digit(0.2))

