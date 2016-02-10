BLOCK_SEP = '#'
WHILE_LOOP_START = 'w'
LOOP_START = '{'
LOOP_END = '}'
ELEMENT_MOVE = ';'
CONSTANT_SEP = ':'
VARIABLE_START = '['
VARIABLE_END = ']'
JUMP_IF_ZERO = 'z'
FUNCTION_START = 'f'
FUNCTION_END = '@'
FUNCTION_ARG = '.'
STRING_MODE = '"'
LIST_START = '('
LIST_END = ')'
JUMP_START = '?'
LOOP_SEP = ','
ELEMENT_ACCESS = '@'
TRUNCATE_STACK = '='

# This is so that we don't get circular imports.
from .parse_ops import parse_variable, parse_move_element, parse_constant, parse_for_loop, parse_block, \
    parse_jump_if_zero, \
    parse_function, parse_while_loop, parse_list, parse_if, parse_get_element, parse_truncate
from .stack_ops import add, sub, mul, div, is_prime, char_print, sqr, exp, swap, get_input, mod, bitwise_and, \
    bitwise_or, bitwise_xor, bitwise_twos, bitwise_lshift, bitwise_rshift, stack_len, stack_sum, clear_stack, \
    pop_stack, get_top, get_bottom, duplicate, greater_than, sort, reverse, permutations, print_stack, count, \
    join_print, factorial, run_length_encoding, push, this_isnt_golf_script, pi, random, is_in, stack_zip, push_range
from .run_ops import run_block, run_variable, run_move, run_getter, run_define_function, run_jump, run_for_loop, \
    run_while_loop, run_list, run_truncate
from .cust_types import Block, Variable, ElementMover, ElementGetter, Function, Jump, ForLoop, WhileLoop, List, Truncate

COMPLEX_TOKENS = {
    VARIABLE_START: parse_variable,
    ELEMENT_MOVE: parse_move_element,
    CONSTANT_SEP: parse_constant,
    LOOP_START: parse_for_loop,
    BLOCK_SEP: parse_block,
    JUMP_IF_ZERO: parse_jump_if_zero,
    FUNCTION_START: parse_function,
    WHILE_LOOP_START: parse_while_loop,
    LIST_START: parse_list,
    JUMP_START: parse_if,
    ELEMENT_ACCESS: parse_get_element,
    TRUNCATE_STACK: parse_truncate,
}

COMMANDS = {
    '⛳': this_isnt_golf_script,
    '!': factorial,
    '%': mod,
    '*': mul,
    '+': add,
    '-': sub,
    '/': div,
    '<': bitwise_lshift,
    '>': bitwise_rshift,
    '^': bitwise_xor,
    '|': bitwise_or,
    '~': bitwise_twos,
    '&': bitwise_and,
    '_': is_in,
    '`': sort,
    '\\': swap,
    ',': pop_stack,
    'a': pi,
    'b': get_bottom,
    'c': char_print,
    'd': duplicate,
    'e': exp,
    'g': greater_than,
    'h': push,
    'i': get_input,
    'j': join_print,
    'k': push_range,
    'l': stack_len,
    'm': is_prime,
    'n': run_length_encoding,
    'o': count,
    'p': print_stack,
    'q': sqr,
    'r': random,
    's': stack_sum,
    't': get_top,
    'u': permutations,
    'v': reverse,
    'x': clear_stack,
    'y': stack_zip,
}

RUN_ACTIONS = {
    Block: run_block,
    Variable: run_variable,
    ElementMover: run_move,
    ElementGetter: run_getter,
    Function: run_define_function,
    Jump: run_jump,
    ForLoop: run_for_loop,
    WhileLoop: run_while_loop,
    List: run_list,
    Truncate: run_truncate

}

# Unused symbols [$, =, ']
