class Block:
    def __init__(self, val):
        self.val = int(val)


class ForLoop:
    def __init__(self, command, iterations):
        self.command = command
        self.iterations = iterations


class Variable:
    def __init__(self, name, val):
        self.name = name
        self.val = val


class PointerSetter:
    def __init__(self, loc):
        self.location = int(loc)


class JumpZero:
    pass


class Function:
    def __init__(self, name, command):
        self.name = name
        self.command = command


class WhileLoop:
    def __init__(self, command, condition):
        self.command = command
        self.condition = condition


class List:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        return List([x + other for x in self.val])

    def __sub__(self, other):
        return List([x - other for x in self.val])

    def __mul__(self, other):
        return List([x * other for x in self.val])

    def __truediv__(self, other):
        return List([x / other for x in self.val])

    def __floordiv__(self, other):
        return List([x // other for x in self.val])

    def __pow__(self, power, modulo=None):
        return List([x ** power for x in self.val])

    def __lt__(self, other):
        return min(self.val) < other

    def __gt__(self, other):
        return max(self.val) > other

    def __ge__(self, other):
        return max(self.val) >= other

    def __and__(self, other):
        return List([x & other for x in self.val])

    def __invert__(self):
        return List([~x for x in self.val])

    def __lshift__(self, other):
        return List([x << other for x in self.val])

    def __rshift__(self, other):
        return List([x >> other for x in self.val])

    def __int__(self):
        return int(sum(self.val))

    def __len__(self):
        return len(self.val)

    def __xor__(self, other):
        return List([x ^ other for x in self.val])

    def __or__(self, other):
        return List([x | other for x in self.val])

    def __repr__(self):
        return str(self.val)

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        return self.__sub__(other)