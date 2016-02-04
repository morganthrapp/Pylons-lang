from interpreter.constants import COMPLEX_TOKENS, COMMANDS, FUNCTION_ARG, STRING_MODE
from interpreter.types import Block, Loop, Variable, PointerSetter, JumpZero, Function


def run(instructions, stack=None, pointer=0, global_vars=None, functions=None):
    if not stack:
        stack = []
    if not global_vars:
        global_vars = {}
    if not functions:
        functions = {}
    tokens = tokenize(instructions)
    num_tokens = len(tokens)  # We do this so that once we remove a token, the other addresses stay static.
    while pointer < num_tokens:
        token = tokens[pointer]
        if token is None:
            pointer += 1
            continue  # For now, the interpreter is super permissive.
        elif isinstance(token, Block):
            stack.append(token.val)
        elif isinstance(token, Variable):
            global_vars[token.name] = token.val
        elif isinstance(token, PointerSetter):
            tokens[pointer] = None
            pointer = token.location
            continue
        elif isinstance(token, Function):
            functions[token.name] = token.command
        elif isinstance(token, JumpZero):
            if stack[-1] == 0:
                continue
        elif isinstance(token, Loop):
            if str(token.iterations).isnumeric():
                iterations = int(token.iterations)
            else:
                iterations = sum(run(token.iterations, global_vars=global_vars, functions=functions))
            for _ in range(iterations):
                stack = run(token.command, stack=stack, global_vars=global_vars, functions=functions)
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
            stack = run(command, stack=stack, global_vars=global_vars, functions=functions)
        pointer += 1
    return stack


def tokenize(instructions):
    tokens = []
    pointer = 0
    string_mode = False
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
        elif token.isnumeric():
            tokens.append(token)
            pointer += 1
        elif token.isupper():
            tokens.append(token)
            pointer += 1
        else:
            pointer += 1  # If we find a command we don't recognize, just skip it.

    return tokens


if __name__ == '__main__':
    print(run(input()))
