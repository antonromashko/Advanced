import random
from homework_01 import *


def test_stack(limit, data_type):
    """Test only for types: int, str, float, bool, list and tuple."""
    stack = Stack(data_type, limit)
    push_and_limit(limit, stack, data_type)
    count_check(limit, stack)
    pull_check(limit, stack)
    empty_stack_error_test(stack)
    type_check(data_type, stack)
    clear_check(limit, stack, data_type)
    data_type_check(data_type, stack)


def data_type_check(data_type, stack):
    """Testing argument data_type"""
    if data_type == int:
        try:
            stack.push(str(random.randint(10, 20)))
            print('- Class take any arguments')
        except TypeError:
            print('+ Class take only correct data type')
    else:
        try:
            stack.push(random.randint(10, 20))
            print('- Class take any arguments')
        except TypeError:
            print('+ Class take only correct data type')


def clear_check(limit, stack, data_type):
    """Testing clear method"""
    for i in range(limit):
        stack.push(data_type(str(random.randint(10, 20))))
    stack.clear()
    if len(stack.stack) == 0:
        print('+ Clear method works')
    else:
        print('- Clear method finished with mistakes')


def type_check(data_type, stack):
    """Testing type method"""
    if stack.type == data_type:
        print('+ Type method works')
    else:
        print('- Type method finished with mistakes')


def empty_stack_error_test(stack):
    """Testing EmptyStackError. Try to remove from empty stack."""
    try:
        stack.pull()
        print("- EmptyStackError doesn't work")
    except EmptyStackError:
        print('+ EmptyStackError generated right')


def pull_check(limit, stack):
    """Testing pull method"""
    for i in range(limit):
        stack.pull()
    if len(stack.stack) == 0:
        print('+ Pull method works')
    else:
        print('- Pull method finished with mistakes')


def count_check(limit, stack):
    """Testing count method"""
    if stack.count() == limit:
        print('+ Count method works')
    else:
        print('- Count method finished with mistakes')


def push_and_limit(limit, stack, data_type):
    """Testing of push method, LimitExceedError and limit argument"""
    for i in range(limit):
        stack.push(data_type(str(random.randint(10, 20))))
    print(stack.stack)
    try:
        stack.push(data_type(str(random.randint(10, 20))))
        print("- LimitExceedError doesn't work")
    except LimitExceedError:
        print('+ LimitExceedError generated right!')
    if len(stack.stack) == limit:
        print('+ Push method works')
        print('+ Limit of stack items is ' + str(len(stack.stack) == limit))
    else:
        print('- Push method finished with mistakes')
        print('- Limit of stack items is ' + str(len(stack.stack) == limit))


test_stack(5, int)
