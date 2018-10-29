import os


def get_element(my_txt, n_pos, qty=1, pos='left'):
    if pos == 'left':
        my_txt.seek(0 + n_pos)
        return my_txt.read(qty)
    elif pos == 'right':
        my_txt.seek(0, 2)
        my_txt.seek(my_txt.tell() - (n_pos + 1), 0)
        return my_txt.read(qty)
    else:
        raise ValueError


def check_sep(my_txt, element):
    if element == '\r':
        my_txt.write('\n')
    elif element == '\n':
        my_txt.write('\r')
    else:
        my_txt.write(element)


def write_elements(my_txt, n_pos, left, right):
    my_txt.seek(0 + n_pos)
    check_sep(my_txt, right)
    my_txt.seek(0, 2)
    my_txt.seek(my_txt.tell() - (n_pos + 1), 0)
    check_sep(my_txt, left)


def my_reverse(my_file):
    with open(my_file, 'r+', newline='\n') as my_txt:
        my_txt.seek(0, 2)
        rng = my_txt.tell()
        for i in range(rng // 2):
            left = get_element(my_txt, i, pos='left')
            right = get_element(my_txt, i, pos='right')
            write_elements(my_txt, i, left, right)


