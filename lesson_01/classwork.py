# GIT
# разрешение конфликтов
# контроль версий
# branch
# 'myproj'/git init сщздает папку служебную .git/
# git status
# git commit -m 'Initial commit'  типа точка сохраненя
# git add -A маркерование изменение
# git config --add --global user.name 'username'
# git diff HEAD^ or HEAD^^
# git reset --hard
# git reset --hard HEAD^ откат на commit
# git push -u origin master
# https://www.python.org/dev/peps/pep-0008/
# RuntimeError
# print('Age: {}'.format(age))
# logging.info('Age: {}'.format(age))
# test scripts
# test functions
# test cases
# test suites
# test frameworks
# хитрость с tuple
# b = []
# a = (1, 2, b)
# a[2].append(2)
# print(a)
#
#
# def foo(a=[]):
#    """с каждым вызвом функции используется ссылка на а"""
#    a.append(1)
#    print(a)
#
#
# mydir = {'a': 1, 'cb': 2, 'c': 3, 'ed': 5}
# print(list(filter(lambda x: x.startswith('c'), map(lambda k: (str(k) + str(mydir[k])), mydir.keys()))))

# a = list(range(100))
# a2 = list(map(lambda x: x**2, a))
# print(a2)


# def unpacker(*args):
#     list_final = []
#     for i in args:
#         if not isinstance(i, (list, tuple, set, frozenset)):
#             list_final.append(i)
#         else:
#             list_final.extend(unpacker(*i))
#     return list_final
#
#
# print(unpacker(1, (2, 0, True), 3, [1, [7, ('fsfsf', 2.1113, [5]),[9, 2, [12, 'tre']]]]))
# класс имеет поле(переменную) или метод(функция)
# вызвать переменную __file из вне из класса А() можно --- a._A__file
# test_mro.py проверить наследовательность
# import keyword
#
#
# class Language:
#    words = ['language']
#
#    def lexicon(self):
#        return ', '.join(str(k) for k in self.words)
#
#
# class ProgLanguage(Language):
#    keywords = [1, 2]
#
#    def lexicon(self):
#        return ', '.join(str(k) for k in self.keywords)
#
#
# class Python(ProgLanguage):
#     keywords = keyword.kwlist
# p = Python()
# print(p.lexicon())
#  @property

# import datetime
# import pandas as pd
#
#
# class Human:
#    def __init__(self, name, birth_date):
#        self.name, self.birth = name, birth_date
#
#    @property
#    def age(self):
#        return round((datetime.datetime.now()-self.birth).days / 365)
#
#    @age.setter
#    def age(self, value):
#        self.age = value
#
#
# h = Human('dsa', pd.to_datetime('2013-03-28 21:28:08.000'))
# h.age = pd.to_datetime('2010-03-28 21:28:08.000')
# print(h.age)


# def singleton(class_):
#    instance = {}
#
#    def get_instance(*args, **kwargs):
#        if class_ not in instance:
#            instance[class_] = class_(*args, **kwargs)
#        return instance[class_]
#    return get_instance
#
#
# @singleton
# class MyClass:
#    pass
#
#
# a = MyClass()
# b = MyClass()
# print(a is b)

# models = {}
#
#
# class ModelMetaclass(type):
#    def __new__(mcs, name, *args):
#        models[name] = type.__new__(mcs, name, *args)
#        return models[name]
#
#
# print(models)
#
#
# class Model(metaclass=ModelMetaclass):
#    pass
#
#
# print(models)
#
#
# class MyModel(Model):
#    pass
# print(models)


# class_name = input('Input class name: ')
# words_dict = {}
# while True:
#    enter = input('Enter: ')
#    parts = enter.split("=")
#    if enter == '':
#        break
#    elif parts[0].isidentifier() is False:
#        continue
#    else:
#        words_dict[parts[0]] = parts[1]
#
#
# classes = type(class_name, (object,), words_dict)
# s = classes()
# print(s)
# print(s.a)
# import ast
# x = "[1, 2, 3]"
# x = [str(n).strip() for n in ast.literal_eval(x)]
# y = sum(int(i) for i in x)
# print(y)
# n = str(sum(int(i) for i in s))
# print(x)
#from contextlib import contextmanager
#import itertools
#
#
#def coroutines(f):
#    def wrap(*args, **kwargs):
#        gen = f(*args, **kwargs)
#        gen.send(None)
#        return gen
#    return wrap
#
#
#@coroutines
#def calc():
#    i = 0
#    while True:
#        x = yield i
#        if x is not None:
#            break
#        i += 1
##gen = (x for x in xrange(0, 100*10000))
#c = calc()
#print(next(c))
#print(next(c))
#print(next(c))
#print(c.send(5))
#print(next(c))


#bool(re.search('[a-zA-Z]', 'Ivan Petrov'))