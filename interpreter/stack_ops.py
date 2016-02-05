import math
import sys
import itertools
from .cust_types import List


def add(_stack):
    if len(_stack) > 1:
        new_val = _stack[-1] + _stack[-2]
        _stack[-2] = new_val
        return _stack[:-1]
    else:
        return _stack


def sub(_stack):
    if len(_stack) > 1:
        new_val = _stack[-1] - _stack[-2]
        _stack[-2] = new_val
        return _stack[:-1]
    else:
        return _stack


def mul(_stack):
    if len(_stack) > 1:
        new_val = _stack[-1] * _stack[-2]
        _stack[-2] = new_val
        return _stack[:-1]
    else:
        return _stack


def div(_stack):
    if len(_stack) > 1:
        new_val = _stack[-1] / _stack[-2]
        _stack[-2] = new_val
        return _stack[:-1]
    else:
        return _stack


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
    else:
        return _stack


def swap(_stack):
    if len(_stack) > 1:
        _stack[-2], _stack[-1] = _stack[-1], _stack[-2]
        return _stack


def is_prime(_stack):
    n = _stack[-1]
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


def get_input(_stack):
    for arg in sys.argv[1:]:
        if arg.isnumeric():
            _stack.append(int(arg))
        else:
            for char in arg:
                _stack.append(ord(char))
    return _stack


def mod(_stack):
    if len(_stack) > 1:
        new_val = _stack[-1] % _stack[-2]
        _stack[-2] = new_val
        return _stack[:-1]
    else:
        return _stack


def bitwise_and(_stack):
    if len(_stack) > 1:
        new_val = _stack[-1] & _stack[-2]
        _stack[-2] = new_val
        return _stack[:-1]
    else:
        return _stack


def bitwise_xor(_stack):
    if len(_stack) > 1:
        new_val = _stack[-1] ^ _stack[-2]
        _stack[-2] = new_val
        return _stack[:-1]
    else:
        return _stack


def bitwise_or(_stack):
    if len(_stack) > 1:
        new_val = _stack[-1] | _stack[-2]
        _stack[-2] = new_val
        return _stack[:-1]
    else:
        return _stack


def bitwise_twos(_stack):
    new_val = ~_stack[-1]
    _stack[-1] = new_val
    return _stack


def bitwise_lshift(_stack):
    if len(_stack) > 1:
        new_val = _stack[-1] << _stack[-2]
        _stack[-2] = new_val
        return _stack[:-1]
    else:
        return _stack


def bitwise_rshift(_stack):
    if len(_stack) > 1:
        new_val = _stack[-1] >> _stack[-2]
        _stack[-2] = new_val
        return _stack[:-1]
    else:
        return _stack


def stack_sum(_stack):
    total = 0
    for x in _stack:
        if isinstance(x, List):
            total += sum(x.val)
        else:
            total += x
    return [total]


def stack_len(_stack):
    return [len(_stack)]


def clear_stack(_stack):
    return []


def pop_stack(_stack):
    return _stack[:-1]


def get_top(_stack):
    return [_stack[-1]]


def get_bottom(_stack):
    return [_stack[0]]


def duplicate(_stack):
    _stack.append(_stack[-1])
    return _stack


def greater_than(_stack):
    return _stack[-1] > _stack[-2]


def sort(_stack):
    return list(sorted(_stack))


def reverse(_stack):
    return list(reversed(_stack))


def permutations(_stack):
    perms = list(itertools.permutations(_stack))
    return perms


def print_stack(_stack):
    print([x for x in _stack if x is not None])
    return _stack


def count(_stack):
    stack = sort(_stack)
    _stack = []
    for x in set(stack):
        _stack.append(x)
        _stack.append(stack.count(x))
    return _stack


def join_print(_stack):
    print(''.join(map(str, _stack)))
    return _stack


def factorial(_stack):
    new_val = math.factorial(_stack[-1])
    _stack[-1] = new_val
    return _stack
