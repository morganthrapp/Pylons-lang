import itertools
import math
import sys
from random import randint
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
        new_val = _stack[-1] // _stack[-2]
        _stack[-2] = new_val
        return _stack[:-1]
    else:
        return _stack


def char_print(_stack, upper=False):
    if upper:
        print(''.join(chr(x) for x in _stack).upper())
    else:
        print(''.join(chr(x) for x in _stack))
    exit()


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
    for arg in sys.argv:
        if arg.isnumeric():
            _stack.append(int(arg))
        else:
            _stack += map(ord, arg)
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
    total = sum(int(x) for x in _stack if x is not None)
    return [total]


def stack_len(_stack):
    return [len(_stack)]


def clear_stack(_stack):
    return []


def pop_stack(_stack):
    return _stack[:-1]


def get_top(_stack):
    val = _stack[-1]
    if isinstance(val, List):
        return [val.val[-1]]
    else:
        return [val]


def get_bottom(_stack):
    val = _stack[0]
    if isinstance(val, List):
        return [val.val[0]]
    else:
        return [val]


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
        _stack.append(stack.count(x))
        _stack.append(x)
    return _stack


def join_print(_stack):
    print(''.join(map(str, _stack)))
    exit()


def factorial(_stack):
    new_val = math.factorial(_stack[-1])
    _stack[-1] = new_val
    return _stack


def run_length_encoding(_stack):
    input_string = ''.join(map(str,_stack))
    count = 1
    prev = ''
    lst = []
    for character in input_string:
        if character != prev:
            if prev:
                lst += [count, int(prev)]
                # print lst
            count = 1
            prev = character
        else:
            count += 1
    else:
        lst += [count, int(character)]
    return lst


def no_print(_stack):
    exit()


def push(_stack):
    val = _stack[-1]
    lst = _stack[-2]
    if isinstance(lst, List):
        lst.val.append(val)
    return _stack[:-1]


def this_isnt_golf_script(_stack):
    print("This isn't golf script! Good try though.")
    return _stack


def pi(_stack):
    if len(_stack) > 1:
        digits = _stack[-1]
    else:
        digits = 100
    pi_val = str(math.pi)[:digits + 1].replace('.', '')
    _stack += list(map(int, pi_val))
    return


def random(_stack):
    start = 0
    end = sys.maxsize
    if len(_stack) > 2:
        start = _stack[-1]
        end = _stack[-2]
        rand_val = randint(start, end)
    elif len(_stack) > 1:
        end = _stack[-1]
        rand_val = randint(start, end)
    else:
        rand_val = randint(start, end)
    _stack.append(rand_val)
    return _stack
