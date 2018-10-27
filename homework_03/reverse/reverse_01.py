import os


def get_element(file, n_pos, qty=1, pos='left'):
    if pos == 'left':
        file.seek(0 + n_pos)
        return file.read(qty)
    elif pos == 'right':
        file.seek(-1 - n_pos, os.SEEK_END)
        return file.read(qty)
    else:
        raise ValueError


def check_sep(file, element):
    if element == b'\r':
        file.write(b'\n')
    elif element == b'\n':
        file.write(b'\r')
    else:
        file.write(element)


def write_elements(file, n_pos, left, right):
    file.seek(0 + n_pos)
    check_sep(file, right)
    file.seek(-1 - n_pos, os.SEEK_END)
    check_sep(file, left)


def my_reverse(filename):
    with open(filename, 'rb+') as file:
        file.seek(0, os.SEEK_END)
        rng = file.tell()
        for i in range(rng // 2):
            left = get_element(file, i, pos='left')
            right = get_element(file, i, pos='right')
            write_elements(file, i, left, right)


my_reverse('1.txt')