from .constants import BLOCK_SEP, LOOP_END, VARIABLE_END
from .types import Block, Loop, Variable, PointerSetter, JumpZero


def parse_block(instructions, pointer=0):
    pointer += 1
    instructions = instructions[pointer:]
    block_end = instructions.find(BLOCK_SEP)
    value = instructions[:block_end]
    pointer += block_end + 1  # The 2 accounts for the block start.
    return pointer, Block(value)


def parse_loop(instructions, pointer):
    start = pointer
    while instructions[pointer] != LOOP_END:
        pointer += 1
    command = instructions[start+1:pointer]
    command, loop_count = command.split(',')
    if loop_count.startswith(BLOCK_SEP):
        block_pointer, block = parse_block(loop_count)
        loop_count = block.val
        pointer += block_pointer
    pointer += 1  # To ignore the end of the loop block.
    return pointer, Loop(command, loop_count)


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
    commands = instructions[pointer:variable_end_location]
    value = run(commands)
    pointer += len(commands) + 1  # Set the pointer to after the initialization block.
    return pointer, Variable(name, sum(value))


def parse_jump_if_zero(instructions, pointer):
    return pointer + 1, JumpZero()