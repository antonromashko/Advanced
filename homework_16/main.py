from multiprocessing import Process
from random import sample
from subprocess import call


my_attr = list(map(str, sample(range(1, 100), 3)))
sub_file = ['python', 'slave.py']
sub_file.extend(my_attr)


def multi_slave():
    call(sub_file)


def pro(x):
    processes = [Process(target=multi_slave) for i in range(x)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
        print('pid =', str(p.pid))


if __name__ == '__main__':
    pro(3)
