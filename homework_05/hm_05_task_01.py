import re

words_dict = {}
class_name = input('Input class name: ')


def remove_spec(my_string):
    clear_specs = re.sub('[^A-Za-z0-9\'\"\=]+', '', my_string)
    new_list = clear_specs.split("=")
    new_list[0] = re.sub('[^A-Za-z0-9]+', '', new_list[0])
    return new_list


def type_checking(my_string):
    try:
        if my_string in ('True', 'False'):
            my_string = bool(my_string)
        else:
            my_string = int(my_string)
    except ValueError:
        if my_string.startswith(("'", "\"")) and my_string[0] == my_string[len(my_string) - 1]:
            my_string = re.sub('[^A-Za-z0-9]+', '', my_string)
        else:
            raise TypeError
    return my_string


def get_params():
    while True:
        enter = input('Enter: ')
        parts = remove_spec(enter)
        if enter == '':
            break
        else:
            try:
                if parts[0].isidentifier() is False:
                    raise SyntaxError
                else:
                    words_dict[parts[0]] = type_checking(parts[1])
            except (SyntaxError, TypeError):
                print('Invalid character')


get_params()


def get_elements(self):
    elements = ''.join(key + '=' + str(value) + '\n' for key, value in words_dict.items())
    return "Class <%s>:" % str(self.__class__.__name__) + '\n' + elements


classes = type(class_name, (object,), words_dict)
classes.__str__ = get_elements
s = classes()
print(s)
