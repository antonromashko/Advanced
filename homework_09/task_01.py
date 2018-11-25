import arrow
from abc import ABCMeta


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class BaseComputer(metaclass=ABCMeta):
    component = {}

    def __init__(self):
        self.release_date = arrow.now()
        self.vendor = __class__.__name__

    def get_elem(self):
        return self.component


class Monitor(BaseComputer):
    def __init__(self, model, diagonal):
        super().__init__()
        self.model = model
        self.diagonal = diagonal
        self.component = {'component': __class__.__name__,
                          'model': self.model,
                          'diagonal': self.diagonal,
                          'release time': self.release_date,
                          'vendor': self.vendor}


class KeyBoard(BaseComputer):
    def __init__(self, key_type):
        super().__init__()
        self.key_type = key_type
        self.component = {'component': __class__.__name__,
                          'type': self.key_type,
                          'release time': self.release_date,
                          'vendor': self.vendor}


class CompCase(BaseComputer):
    def __init__(self, case_type):
        super().__init__()
        self.case_type = case_type
        self.component = {'component': __class__.__name__,
                          'type': self.case_type,
                          'release time': self.release_date,
                          'vendor': self.vendor}


class CompFactory(metaclass=Singleton):
    @staticmethod
    def component_creator(component, model, diagonal, key_type, case_type):
        if component == 'Monitor':
            return Monitor(model, diagonal)
        if component == 'Keyboard':
            return KeyBoard(key_type)
        if component == 'CompCase':
            return CompCase(case_type)


m = CompFactory()
components = ['Monitor', 'Keyboard', 'CompCase']


if __name__ == '__main__':
    for comp in components:
        print(m.component_creator(comp, 1, 2, 'PC', 'Tower').get_elem())