from homework_04.task_12 import Context


class ContextNew(Context):
    def __enter__(self, **kwargs):
        self.my_dict.update(kwargs)
        for k, v in self.my_dict.items():
            globals()[k] = v

    def __exit__(self, typ, value, traceback):
        for k, v in self.my_dict.items():
            del globals()[k]


with ContextNew(x=1, y=2) as c:
    print(x, y)
print(x, y)
