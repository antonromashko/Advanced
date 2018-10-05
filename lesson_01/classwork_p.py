def func(string):
    t = tuple(ord(i) for i in string)
    return tuple(t)


print(func('s faf'))