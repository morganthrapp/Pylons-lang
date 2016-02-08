from interpreter.constants import COMPLEX_TOKENS, COMMANDS, FUNCTION_ARG, STRING_MODE
from interpreter.cust_types import Block, ForLoop, Variable, ElementMover, Jump, Function, WhileLoop, List, ElementGetter
import copy


def run(instructions, stack=None, pointer=0, global_vars=None, functions=None):
    if not stack:
        stack = []
    else:
        try:
            stack = copy.copy(stack)
        except AttributeError:
            print(stack)
    if not global_vars:
        global_vars = {'A': -1, 'B': 10, 'C': 100, 'D': 1000}
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
            if isinstance(token.val, str):
                if any(x in global_vars for x in token.val):
                    global_vars[token.name] = sum(run(token.val, functions=functions, global_vars=global_vars))
                else:
                    global_vars[token.name] = sum(run(token.val, stack=stack, functions=functions, global_vars=global_vars))
            else:
                global_vars[token.name] = int(token.val)
        elif isinstance(token, ElementMover):
            new_top = stack.pop(token.location)
            stack.append(new_top)
        elif isinstance(token, ElementGetter):
            stack.append(stack[token.location])
        elif isinstance(token, Function):
            if token.name in global_vars:
                global_vars.pop(token.name)
            functions[token.name] = token.command
        elif isinstance(token, Jump):
            # Certain jump types require an empty stack, others need the current value of the stack
            if token.clear_stack:
                _stack = []
            else:
                _stack = stack
            if stack[-1] == sum(run(token.condition, stack=_stack, functions=functions, global_vars=global_vars)):
                pointer += 2  # We skip the jump command and the next one.
                continue
        elif isinstance(token, ForLoop):
            if str(token.iterations).isnumeric():
                iterations = int(token.iterations)
            else:
                iterations = sum(run(token.iterations, global_vars=global_vars, functions=functions))
            for _ in range(iterations):
                stack = run(token.command, stack=stack, global_vars=global_vars, functions=functions)
        elif isinstance(token, WhileLoop):
            while run(token.condition, stack, global_vars=global_vars, functions=functions):
                stack = run(token.command, stack, global_vars=global_vars, functions=functions)
        elif isinstance(token, List):
            stack.append(token)
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
    import sys
    program_file = sys.argv[1]
    sys.argv = sys.argv[2:]
    with open(program_file, 'rt') as instruction_file:
        program = instruction_file.read()
    print(run(program))