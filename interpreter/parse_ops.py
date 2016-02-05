from .constants import BLOCK_SEP, LOOP_END, VARIABLE_END, FUNCTION_END
from .cust_types import Block, ForLoop, Variable, PointerSetter, JumpZero, Function, WhileLoop, List


def parse_block(instructions, pointer=0):
    pointer += 1
    instructions = instructions[pointer:]
    block_end = instructions.find(BLOCK_SEP)
    value = instructions[:block_end]
    pointer += block_end + 1
    return pointer, Block(value)


def parse_loop(instructions, pointer):
    start = pointer
    while instructions[pointer] != LOOP_END:
        pointer += 1
    command = instructions[start + 1:pointer]
    command, loop_count = command.split(',')
    if BLOCK_SEP in loop_count:
        block_pointer, block = parse_block(loop_count)
        loop_count = block.val
        pointer += block_pointer
    pointer += 1  # To ignore the end of the loop block.
    return pointer, ForLoop(command, loop_count)


def parse_constant(instructions, pointer):
    pointer += 1
    variable_name = instructions[pointer]
    pointer += 1
    value = instructions[pointer]
    if value == BLOCK_SEP:
        block_pointer, block = parse_block(instructions[pointer:])
        value = block.val
        pointer += block_pointer
    else:
        pointer += 1
    return pointer, Variable(variable_name, value)


def parse_set_pointer(instructions, pointer):
    pointer += 1
    if instructions[pointer] == BLOCK_SEP:
        block_length, block = parse_block(instructions[pointer:])
        new_loc = block.val
        pointer += block_length
    else:
        new_loc = instructions[pointer]
        pointer += 1  # So that the pointer we return is past the value of the setter
    return pointer, PointerSetter(new_loc)


def parse_variable(instructions, pointer):
    from main import run  # We have to do it this way to avoid circular imports.
    pointer += 1  # Skip the initializer.
    name = instructions[pointer]
    pointer += 1  # Skip over the name.
    variable_end_location = instructions.find(VARIABLE_END)
    command = instructions[pointer:variable_end_location]
    if command.isnumeric():
        value = sum(run(command))
    else:
        value = command
    pointer += variable_end_location + 1 # Set the pointer to after the initialization block.
    return pointer, Variable(name, value)


def parse_jump_if_zero(instructions, pointer):
    return pointer + 1, JumpZero()


def parse_function(instructions, pointer):
    pointer += 1
    function_name = instructions[pointer]
    pointer += 1
    function_end_location = instructions.find(FUNCTION_END)
    command = instructions[pointer:function_end_location]
    pointer += len(command) + 1  # Set the pointer to after the function block.
    return pointer, Function(function_name, command)


def parse_while_loop(instructions, pointer):
    start = pointer
    while instructions[pointer] != LOOP_END:
        pointer += 1
    command = instructions[start + 1:pointer]
    command, loop_condition = command.split(',')
    if BLOCK_SEP in loop_condition:
        block_start = loop_condition.find(BLOCK_SEP)
        block_pointer, block = parse_block(loop_condition, block_start)
        loop_condition = loop_condition[:block_start] + block.val + loop_condition[block_pointer:]
    pointer += 1  # To skip the end of the loop block.
    return pointer, WhileLoop(command, loop_condition)


def parse_list(instructions, pointer):
    from main import run  # We have to do it this way to avoid circular imports.
    pointer += 1
    list_end = instructions.find(')')
    list_body = instructions[pointer:list_end]
    pointer += len(list_body) + 1
    list_val = run(list_body)
    return pointer, List(list_val)
