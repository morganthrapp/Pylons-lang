from .constants import BLOCK_SEP, LOOP_END, VARIABLE_END


def parse_block(instructions, pointer):
    pointer += 1
    instructions = instructions[pointer:]
    block_end = instructions.find(BLOCK_SEP)
    value = instructions[:block_end]
    pointer += block_end + 1  # The 2 accounts for the block start.
    return pointer, '|{value}|'.format(value=value)


def parse_loop(instructions, pointer):
    start = pointer
    while instructions[pointer] != LOOP_END:
        pointer += 1
    command = instructions[start:pointer]
    command, loop = command.split(',')
    if loop.startswith(BLOCK_SEP):
        loop = parse_block(loop[1:], pointer)
    return pointer, '{%s,|%s|}'%(command, loop)


def parse_constant(instructions, pointer):
    variable_name = instructions[pointer]
    pointer += 1
    command = instructions[pointer]
    if command == BLOCK_SEP:
        value, pointer = parse_block(instructions[pointer:], pointer)
    else:
        value = command
        pointer += 1
    return pointer, ':{name}|{value}|'.format(name=variable_name, value=value)


def parse_set_pointer(instructions, pointer):
    command = instructions[pointer]
    if command == BLOCK_SEP:
        new_pointer, pointer = parse_block(instructions[pointer + 1:], pointer)
    else:
        new_pointer = command
        pointer += 1
    return pointer, ';{}'.format(new_pointer)


def parse_variable(instructions, pointer):
    from main import run  # We have to do it this way to avoid circular imports.
    name = instructions[pointer]
    pointer += 1
    variable_end_location = instructions.find(VARIABLE_END)
    value = run(instructions[pointer:variable_end_location])
    return pointer, ':{name}|{value}|'.format(name=name, value=sum(value))


def parse_jump_if_zero(instructions, pointer):
    return pointer + 1, instructions[pointer]