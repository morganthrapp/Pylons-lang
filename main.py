from interpreter.constants import COMPLEX_TOKENS, COMMANDS
from interpreter.types import Block, Loop, Variable, PointerSetter, JumpZero


def run(instructions, stack=None, pointer=0, global_vars=None):
    if not stack:
        stack = []
    if not global_vars:
        global_vars = {}
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
        elif isinstance(token, JumpZero):
            if stack[-1] == 0:
                continue
        elif isinstance(token, Loop):
            for _ in range(token.iterations):
                stack = run(token.command, stack=stack, global_vars=global_vars)
        elif token.isnumeric():
            stack.append(int(token))
        elif token in COMMANDS:
            stack = COMMANDS[token](stack)
        elif token.isupper():
            stack.append(global_vars[token])
        pointer += 1
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
            pointer += 1  # If we find a command we don't recognize, just skip it.

    return tokens


if __name__ == '__main__':
    print(run(input()))
