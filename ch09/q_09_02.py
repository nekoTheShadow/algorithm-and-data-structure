def calc(stmt):
    import string
    stack = []
    for ch in stmt.split():
        if ch.isdigit():
            stack.append(int(ch))
        else:
            y = stack.pop()
            x = stack.pop()
            stack.append(eval(f'{x} {ch} {y}'))
    return stack[0]

print(calc('3 4 + 1 2 - *')) #=> -7