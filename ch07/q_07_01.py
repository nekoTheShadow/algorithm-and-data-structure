import collections

a = [2, 4, 6, 8, 10]
b = [3, 6, 9, 12]

p = collections.deque(a)
q = collections.deque(b)
while p and q:
    if p[0] < q[0]:
        x = p.popleft()
        y = q.popleft()
        print('{0} < {1}'.format(x, y))
    else:
        q.popleft()
