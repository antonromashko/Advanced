from abc import ABCMeta


class NumberBaseContext(metaclass=ABCMeta):
    def _validation(self):
        pass


class Context(NumberBaseContext):
    my_dict = {}

    def __init__(self, **kwargs):
        self._validation()
        self.my_dict.update(kwargs)

    def __getattr__(self, name):
        if name in self.my_dict:
            return self.my_dict[name]
        else:
            raise AttributeError("No such attribute: " + name)

    def _validation(self):
        return True

    def __setattr__(self, key, value):
        if key.isidentifier():
            self.my_dict[key] = value
        else:
            raise TypeError

    def __str__(self):
        return "Class('%s')" % ', '.join("%s = %s" % item for item in self.my_dict.items())

    def __len__(self):
        return len(self.my_dict)

    def __iter__(self):
        for i in self.my_dict.items():
            yield i


class RealContext(Context):
    def __init__(self, **kwargs):
        if all(self._validation(key, value) for key, value in kwargs.items()):
            self.my_dict.update(kwargs)
        else:
            raise TypeError

    def _validation(self, key, value):
        if isinstance(value, (int, float)):
            super().__setattr__(key, value)
            return True
        else:
            return False


class ComplexContext(Context):
    def __init__(self, **kwargs):
        if all(self._validation(key, value) for key, value in kwargs.items()):
            self.my_dict.update(kwargs)
        else:
            raise TypeError

    def _validation(self, key, value):
        if isinstance(value, complex):
            super().__setattr__(key, value)
            return True
        else:
            return False


class ValidationError(Exception):
    pass


class NumberContext(RealContext, ComplexContext):
    def __init__(self, **kwargs):
        if all(RealContext._validation(self, key, value) for key, value in kwargs.items()):
            self.my_dict.update(kwargs)
        elif all(ComplexContext._validation(self, key, value) for key, value in kwargs.items()):
            self.my_dict.update(kwargs)
        else:
            raise ValidationError


