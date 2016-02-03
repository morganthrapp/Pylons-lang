import math

BLOCK_SEP = '|'
LOOP_START = '{'
LOOP_END = '}'
POINTER_SET = ';'


def add(_stack):
    if len(_stack) > 1:
        new_val = _stack[-1] + _stack[-2]
        _stack[-2] = new_val
        return _stack[:-1]


def sub(_stack):
    if len(_stack) > 1:
        new_val = _stack[-1] - _stack[-2]
        _stack[-2] = new_val
        return _stack[:-1]


def mul(_stack):
    if len(_stack) > 1:
        new_val = _stack[-1] * _stack[-2]
        _stack[-2] = new_val
        return _stack[:-1]


def div(_stack):
    if len(_stack) > 1:
        new_val = _stack[-1] / _stack[-2]
        _stack[-2] = new_val
        return _stack[:-1]


def char_print(_stack, upper=False):
    if upper:
        print(''.join(chr(x) for x in _stack).upper())
    else:
        print(''.join(chr(x) for x in _stack))
    return _stack


def sqr(_stack):
    new_val = math.sqrt(_stack[-1])
    _stack[-1] = new_val
    return _stack


def exp(_stack):
    if len(_stack) > 1:
        new_val = _stack[-1] ** _stack[-2]
        _stack[-2] = new_val
        return _stack[:-1]


commands = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
    'p': print,
    'c': char_print,
    'C': lambda x: char_print(x, upper=True),
    's': sqr,
    'e': exp,
}


def parse_block(instruction_slice, _pointer=None):
    """This function takes a slice of the instructions and tried to parse it out into a numerical block.
       |\d+| is a block.
       If it can't find anything, it just returns the original slice.
       :param _pointer: str
       :param instruction_slice: int"""
    block_end = instruction_slice.find(BLOCK_SEP)
    if _pointer:
        return instruction_slice[:block_end] or instruction_slice, _pointer + block_end + 1
    else:
        return instruction_slice[:block_end] or instruction_slice


def parse(instructions, stack=None, pointer=0):
    if not stack:
        stack = []
    while pointer < len(instructions):
        command = instructions[pointer]
        pointer += 1
        if command == POINTER_SET:
            command = instructions[pointer]
            if command.startswith(BLOCK_SEP):
                new_pointer, pointer = parse_block(instructions[pointer+1:], pointer)
            else:
                new_pointer = command
                pointer += 1
            return parse(instructions[:instructions.find(POINTER_SET)] + instructions[pointer:], stack, int(new_pointer)-1)
        if command == LOOP_START:
            start = pointer
            while instructions[pointer] != LOOP_END:
                pointer += 1
            command = instructions[start:pointer]
            command, loop = command.split(',')
            if loop.startswith(BLOCK_SEP):
                loop = parse_block(loop[1:])
            for _ in range(int(loop)):
                stack = parse(command, stack)
        if command == BLOCK_SEP:
            command, pointer = parse_block(instructions[pointer:], pointer)
        if command.isnumeric():
            stack.append(int(command))
        elif command in commands:
            stack = commands[command](stack)

    return stack


assert parse('|25|2+7*') == [189]
assert parse('48*') == [4 * 8]
assert parse('1{1+,3}') == [4]
assert parse('1{1+,|11|}') == [12]
parse('|72||101|c')
assert parse('12+;1') == [3, 3]
assert parse('12+;14+') == [3, 7]
assert parse('   12+34+56;|10|') == [3, 7, 5, 6, 5, 6]
assert parse('    12+34+56;|10|') == [3, 7, 11, 5, 6]
assert parse('4s') == [2]
assert parse('22e') == [4]
