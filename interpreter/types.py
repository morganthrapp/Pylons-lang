class Block:
    def __init__(self, val):
        self.val = int(val)


class Loop:
    def __init__(self, command, iterations):
        self.command = command
        self.iterations = int(iterations)


class Variable:
    def __init__(self, name, val):
        self.name = name
        self.val = int(val)


class PointerSetter:
    def __init__(self, loc):
        self.location = int(loc)


class JumpZero:
    pass
