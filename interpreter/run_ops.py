def run_block(action, pointer, stack, functions, global_vars):
    stack.append(action.val)


def run_variable(action, pointer, stack, functions, global_vars):
    from main import run
    if isinstance(action.val, str):
        if any(x in global_vars for x in action.val) or len(action.val) != 1:
            global_vars[action.name] = sum(run(action.val, functions=functions, global_vars=global_vars))
        else:
            global_vars[action.name] = sum(
                run(action.val, stack=stack[:], functions=functions, global_vars=global_vars))
    else:
        global_vars[action.name] = int(action.val)


def run_move(action, pointer, stack, functions, global_vars):
    new_top = stack.pop(action.location)
    stack.append(new_top)


def run_getter(action, pointer, stack, functions, global_vars):
    from main import run
    from .stack_ops import is_int
    if is_int(action.location):
        stack.append(stack[action.location])
    else:
        loc = sum(run(action.location, functions=functions, global_vars=global_vars))
        stack.append(stack[loc])


def run_define_function(action, pointer, stack, functions, global_vars):
    if action.name in global_vars:
        global_vars.pop(action.name)
    functions[action.name] = action.command


def run_jump(action, pointer, stack, functions, global_vars):
    from main import run
    # Certain jump types require an empty stack, others need the current value of the stack
    if action.clear_stack:
        _stack = []
    else:
        _stack = stack
    if stack[-1] == sum(run(action.condition, stack=_stack[:], functions=functions, global_vars=global_vars)):
        pointer += 2  # We skip the jump command and the next one.


def run_for_loop(action, pointer, stack, functions, global_vars):
    from main import run
    if str(action.iterations).isnumeric():
        iterations = int(action.iterations)
    else:
        iterations = sum(run(action.iterations, global_vars=global_vars, functions=functions))
    for _ in range(iterations):
        stack[:] = run(action.command, stack=stack[:], global_vars=global_vars, functions=functions)


def run_while_loop(action, pointer, stack, functions, global_vars):
    from main import run
    while run(action.condition, stack[:], global_vars=global_vars, functions=functions):
        stack[:] = run(action.command, stack=stack[:], global_vars=global_vars, functions=functions)


def run_list(action, pointer, stack, functions, global_vars):
    stack.append(action)


def run_truncate(action, pointer, stack, functions, global_vars):
    stack[:] = stack[:-action.length]


def run_map(action, pointer, stack, functions, global_vars):
    from main import run
    for x in range(len(stack)):
        stack[x] = sum(run(action.command, [stack[x]], global_vars=global_vars, functions=functions))
