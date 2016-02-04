BLOCK_SEP = '|'
LOOP_START = '{'
LOOP_END = '}'
POINTER_SET = ';'
CONSTANT_SEP = ':'
VARIABLE_START = '['
VARIABLE_END = ']'
JUMP_IF_ZERO = 'z'

# We have to do it this way to avoid circular imports.
from .parse_ops import parse_variable, parse_set_pointer, parse_constant, parse_loop, parse_block, parse_jump_if_zero
COMPLEX_TOKENS = {
    VARIABLE_START: parse_variable,
    POINTER_SET: parse_set_pointer,
    CONSTANT_SEP: parse_constant,
    LOOP_START: parse_loop,
    BLOCK_SEP: parse_block,
    JUMP_IF_ZERO: parse_jump_if_zero,
}

# We have to do it this way to avoid circular imports.
from .stack_ops import add, sub, mul, div, print_stack, char_print, sqr, exp, swap, get_input
COMMANDS = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
    'p': print_stack,
    'c': char_print,
    's': sqr,
    'e': exp,
    '\\': swap,
    'i': get_input,
}
