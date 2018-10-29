from reverse_01 import my_reverse
import sys


def test_reverse(filename):
    with open(filename, 'r') as file:
        source = file.read()
    my_reverse(filename)
    my_reverse(filename)
    with open(filename, 'r') as file:
        test_cont = file.read()
    assert test_cont == source


def test_reverse_01(file):
    with open(file, 'r') as f:
        test1 = f.read()[::-1]
    my_reverse(file)
    with open(file, 'r') as f:
        test2 = f.read()
    assert test1 == test2


get_file = sys.argv[-1]
test_reverse(get_file)
test_reverse_01(get_file)
