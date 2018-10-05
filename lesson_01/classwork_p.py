def func(string):
    l = []
    for s in string:
        l.append(ord(s))
    return tuple(l)
print(func('sdfaf'))