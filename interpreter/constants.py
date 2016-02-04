BLOCK_SEP = '#'
WHILE_LOOP_START = 'w'
LOOP_START = '{'
LOOP_END = '}'
POINTER_SET = ';'
CONSTANT_SEP = ':'
VARIABLE_START = '['
VARIABLE_END = ']'
JUMP_IF_ZERO = 'z'
FUNCTION_START = 'f'
FUNCTION_END = '@'
FUNCTION_ARG = '.'
STRING_MODE = '"'

# This is so that we don't get circular imports.
from .parse_ops import parse_variable, parse_set_pointer, parse_constant, parse_loop, parse_block, parse_jump_if_zero, \
    parse_function, parse_while_loop
from .stack_ops import add, sub, mul, div, print_stack, char_print, sqr, exp, swap, get_input, mod, bitwise_and, \
    bitwise_or, bitwise_xor, bitwise_twos, bitwise_lshift, bitwise_rshift, stack_len, stack_sum, clear_stack, \
    pop_stack, get_top, get_bottom, duplicate, greater_than

COMPLEX_TOKENS = {
    VARIABLE_START: parse_variable,
    POINTER_SET: parse_set_pointer,
    CONSTANT_SEP: parse_constant,
    LOOP_START: parse_loop,
    BLOCK_SEP: parse_block,
    JUMP_IF_ZERO: parse_jump_if_zero,
    FUNCTION_START: parse_function,
    WHILE_LOOP_START: parse_while_loop,
}

COMMANDS = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
    '%': mod,
    '&': bitwise_and,
    '^': bitwise_xor,
    '|': bitwise_or,
    '~': bitwise_twos,
    '<': bitwise_lshift,
    '>': bitwise_rshift,
    'p': print_stack,
    'c': char_print,
    'q': sqr,
    'e': exp,
    '\\': swap,
    'i': get_input,
    's': stack_sum,
    'l': stack_len,
    'x': clear_stack,
    ',': pop_stack,
    't': get_top,
    'b': get_bottom,
    'd': duplicate,
    'g': greater_than,
}
