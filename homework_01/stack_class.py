class LimitExceedError(Exception):
    def __init__(self, message=''):
        self.message = message

    def __str__(self):
        return self.message


class EmptyStackError(LimitExceedError):
    pass


class Stack:
    """Class Stack matches the data structure stack FILO"""

    def __init__(self, data_type=object, limit=None):
        self.stack = []
        self.data_type = data_type
        self.limit = limit

    def __str__(self):
        """Return string like Stack<'type'>"""
        return "{} <{}>".format(self.__class__.__name__, self.data_type.__name__)

    def _push(self, item):
        """Check whether satisfies class arguments value
        TypeError if item not equal to the data_type(default object)
        Exception('LimitExceedError') if item doesn't satisfy limit value(default None)"""
        if not isinstance(item, self.data_type):
            raise TypeError
        if len(self.stack) >= self.limit:
            raise LimitExceedError('Stack limit is over!')

    def push(self, item):
        """Add element to stack, nothing return"""
        self._push(item)
        self.stack.append(item)

    def pull(self):
        """Delete last added item from stack and return it
        Exception('EmptyStackError') if stack is empty"""
        if len(self.stack) != 0:
            return self.stack.pop()
        else:
            raise EmptyStackError('Empty stack. Nothing to remove.')

    def count(self):
        """Return number of items in stack"""
        return len(self.stack)

    def clear(self):
        """Empty stack"""
        self.stack.clear()

    @property
    def type(self):
        """Return stack type"""
        return self.data_type
