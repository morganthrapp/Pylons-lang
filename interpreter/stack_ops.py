import math
import sys


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


def swap(_stack):
    if len(_stack) > 1:
        _stack[-2], _stack[-1] = _stack[-1], _stack[-2]
        return _stack


def print_stack(_stack):
    print([x for x in _stack if x is not None])
    return _stack


def get_input(_stack):
    for arg in sys.argv[1:]:
        _stack.append(int(arg))
    return _stack