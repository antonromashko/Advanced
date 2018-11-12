class ConstAttributeError(Exception):
    """Custom exception if try to change attribute value"""
    pass


class Const(type):
    """Metaclass prevents static properties from changing."""
    def __getattr__(cls, key):
        return cls[key]

    def __setattr__(cls, key, value):
        """Checks if a variable exists.
        Note:
            Do not include the `self` parameter in the ``Args`` section.
        Args:
            key: variable name.
            value: variable value"""
        if key not in cls.__dict__.keys():
            super().__setattr__(key, value)
        else:
            raise ConstAttributeError


class A(metaclass=Const):
    x = 1
