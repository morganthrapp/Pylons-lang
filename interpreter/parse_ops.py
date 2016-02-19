from .constants import BLOCK_SEP, LOOP_END, VARIABLE_END, FUNCTION_END, LOOP_SEP, LIST_END
from .cust_types import Pointer, Block, ForLoop, Variable, ElementMover, Jump, Function, WhileLoop, List, \
    ElementGetter, Truncate
from .stack_ops import is_int


def parse_number(instructions, pointer=0):
    number = instructions[pointer]
    if number == BLOCK_SEP:
        block_pointer, block = parse_block(instructions, pointer)
        number = block.val
        pointer += block_pointer
    elif number.startswith('-'):
        number = int(instructions[pointer] + instructions[pointer + 1])
        pointer += 1
    elif is_int(number):
        number = int(instructions[pointer])
        pointer += 1
    else:
        pointer += 1
    return pointer, number


def parse_block(instructions, pointer=0):
    pointer += 1
    instructions = instructions[pointer:]
    block_end = instructions.find(BLOCK_SEP)
    value = instructions[:block_end]
    pointer += block_end + 1
    return pointer, Block(value)


def parse_for_loop(instructions, pointer):
    start = pointer[:]
    pointer = instructions[start:].find(LOOP_END) + start[:]
    command = instructions[start + 1:pointer]
    command, _, loop_count = command.rpartition(LOOP_SEP)
    loop_pointer, number = parse_number(loop_count)
    pointer += loop_pointer
    return pointer, ForLoop(command, loop_count)


def parse_constant(instructions, pointer):
    pointer += 1
    variable_name = instructions[pointer]
    pointer += 1
    pointer, value = parse_number(instructions, pointer)
    return pointer, Variable(variable_name, value)


def parse_move_element(instructions, pointer):
    pointer += 1
    pointer, new_loc = parse_number(instructions, pointer)
    return pointer, ElementMover(new_loc)


def parse_get_element(instructions, pointer):
    pointer += 1
    pointer, new_loc = parse_number(instructions, pointer)
    return pointer, ElementGetter(new_loc)


def parse_variable(instructions, pointer):
    from main import run  # We have to do it this way to avoid circular imports.
    pointer += 1  # Skip the initializer.
    name = instructions[pointer]
    pointer += 1  # Skip over the name.
    variable_end_location = instructions[pointer[:]:].find(VARIABLE_END) + pointer[:]
    command = instructions[pointer:variable_end_location]
    if command.isnumeric():
        value = sum(run(command))
    elif command.strip():
        value = command
    else:
        value = 't'
    pointer = variable_end_location[:] + 1  # Set the pointer to after the initialization block.
    return pointer, Variable(name, value)


def parse_jump_if_zero(instructions, pointer):
    return pointer + 1, Jump(clear_stack=True)


def parse_function(instructions, pointer):
    pointer += 1
    function_name = instructions[pointer]
    pointer += 1
    function_end_location = instructions.find(FUNCTION_END)
    command = instructions[pointer:function_end_location]
    pointer += len(command) + 1  # Set the pointer to after the function block.
    return pointer, Function(function_name, command)


def parse_while_loop(instructions, pointer):
    start = pointer[:]
    pointer = instructions[start:].find(LOOP_END) + start[:]
    command = instructions[start + 1:pointer]
    command, _, loop_condition = command.rpartition(LOOP_SEP)
    if BLOCK_SEP in loop_condition:
        block_start = loop_condition.find(BLOCK_SEP)
        block_pointer, block = parse_block(loop_condition, block_start)
        loop_condition = loop_condition[:block_start] + block.val + loop_condition[block_pointer:]
    return pointer, WhileLoop(command, loop_condition)


def parse_list(instructions, pointer):
    from main import run  # We have to do it this way to avoid circular imports.
    pointer += 1
    list_end = instructions[pointer:].find(LIST_END) + pointer[:]
    list_body = instructions[pointer:list_end]
    pointer += len(list_body) + 1
    list_val = run(list_body)
    return pointer, List(list_val)


def parse_if(instructions, pointer):
    pointer += 1
    pointer, condition = parse_number(instructions, pointer)
    clear_stack = is_int(condition)
    return pointer, Jump(condition, clear_stack)


def parse_truncate(instructions, pointer):
    pointer += 1
    pointer, length = parse_number(instructions, pointer)
    return pointer, Truncate(length)
