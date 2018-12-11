import sys

param = list(map(int, sys.argv[1:]))


def slaver(start, end, step):
    return sum(list(range(start, end, step)))


slaver(param[0], param[1], param[2])