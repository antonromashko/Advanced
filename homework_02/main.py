import os
import time
import ast

def timing(f):
    def wrapper(arg):
        start = time.time()
        r = f(arg)
        end = time.time()
        print(f.__name__, 'time: {}'.format(end-start))
        return r
    return wrapper


@timing
def process(content):
    list_of_numbers = [str(n).strip() for n in ast.literal_eval(content)]
    return str(sum(int(i) for i in list_of_numbers))


def monitor(initial, results, mistakes):
    files_txt = list(filter(lambda i: i.endswith('.txt'), os.listdir(initial)))
    for file in files_txt:
        with open(initial + '/' + file, 'r') as file_txt:
            t = file_txt.read()
            try:
                process(t)
                with open(results + '/' + file, 'w') as result_txt:
                    result_txt.write(process(t))
            except Exception:
                with open(mistakes + '/' + file, 'w') as mistake_txt:
                    mistake_txt.write(t)
        os.remove(initial + '/' + file)
