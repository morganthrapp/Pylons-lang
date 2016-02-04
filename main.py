from interpreter.constants import COMPLEX_TOKENS, COMMANDS


def run(instructions, stack=None, pointer=0, global_vars=None):
    if not stack:
        stack = []
    if not global_vars:
        global_vars = {}
    for token in tokenize(instructions):
        if token in global_vars:
            token = global_vars[token]
    print(stack)
    return stack


def tokenize(instructions):
    tokens = []
    pointer = 0
    while pointer < len(instructions):
        command = instructions[pointer]
        if command in COMPLEX_TOKENS:
            pointer, token = COMPLEX_TOKENS[command](instructions, pointer)
            tokens.append(token)
        elif command in COMMANDS:
            tokens.append(command)
            pointer += 1
        elif command.isnumeric():
            tokens.append(command)
            pointer += 1
        elif command.isupper():
            tokens.append(command)
            pointer += 1
        else:
            raise ValueError('Invalid token {}'.format(command))  # If we find something that shouldn't be there.

    return tokens
