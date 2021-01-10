s = '(()(())())(()())'
stack = []
for i, ch in enumerate(s):
    if ch == '(':
        stack.append(i)
    else:
        j = stack.pop()
        print(f'pair {j} {i}')