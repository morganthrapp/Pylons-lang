from interpreter.constants import COMPLEX_TOKENS, COMMANDS, FUNCTION_ARG, STRING_MODE, RUN_ACTIONS
from interpreter.cust_types import Pointer, Stack
from interpreter.stack_ops import is_int


def run(instructions, stack=None, pointer=None, global_vars=None, functions=None):
    if stack is None:
        stack = Stack()
    else:
        stack = stack
    if pointer is None:
        pointer = Pointer()
    else:
        pointer = pointer
    if not global_vars:
        global_vars = {'A': -1, 'B': 10, 'C': 100, 'D': 1000, 'E': 0}
    if not functions:
        functions = {}
    tokens = tokenize(instructions)
    num_tokens = len(tokens)  # We do this so that once we remove a token, the other addresses stay static.
    while pointer < num_tokens:
        token = tokens[pointer]
        if token is None:
            pointer += 1
            continue  # For now, the interpreter is super permissive.
        elif type(token) in RUN_ACTIONS:
            RUN_ACTIONS[type(token)](token, pointer, stack, functions, global_vars)
        elif token.isnumeric():
            stack.append(int(token))
        elif token in COMMANDS:
            stack = COMMANDS[token](stack)
        elif token in global_vars:
            stack.append(global_vars[token])
        elif token in functions:
            command = functions[token]
            index = -1
            while FUNCTION_ARG in command:
                command = command.replace(FUNCTION_ARG, '#{}#'.format(str(stack[index])), 1)
                index -= 1
            stack = run(command, stack=stack[:], global_vars=global_vars, functions=functions)
        pointer += 1
    return stack


def tokenize(instructions):
    tokens = []
    pointer = Pointer()
    string_mode = False
    instructions = str(instructions)
    while pointer < len(instructions):
        token = instructions[pointer]
        if token == STRING_MODE:
            string_mode = not string_mode
            pointer += 1
        elif string_mode:
            tokens.append(str(ord(token)))
            pointer += 1
        elif token in COMPLEX_TOKENS:
            pointer, token = COMPLEX_TOKENS[token](instructions, pointer)
            tokens.append(token)
        elif token in COMMANDS:
            tokens.append(token)
            pointer += 1
        elif is_int(token):
            tokens.append(token)
            pointer += 1
        elif token.isupper():
            tokens.append(token)
            pointer += 1
        else:
            pointer += 1  # If we find a command we don't recognize, just skip it.

    return tokens


if __name__ == '__main__':
    import sys
    program_file = sys.argv[1]
    sys.argv = sys.argv[2:]
    with open(program_file, 'rt') as instruction_file:
        program = instruction_file.read()
    print(run(program))