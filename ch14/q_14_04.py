import itertools, collections

h, w = map(int, input().split())
c = [input() for _ in range(h)]

start_i = start_j = goal_i = goal_j = -1
for i, j in itertools.product(range(h), range(w)):
    if c[i][j] == 's':
        start_i, start_j = i, j
    if c[i][j] == 'g':
        goal_i, goal_j = i, j

q = collections.deque()
d = [[float('inf')]*w for _ in range(h)]
q.append((start_i, start_j))
d[start_i][start_j] = 0
while q:
    i, j = q.popleft()
    for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        ni, nj = i+di, j+dj
        if 0 <= ni < h and 0 <= nj < w:
            if c[ni][nj] == '#':
                if d[i][j]+1 < d[ni][nj]:
                    d[ni][nj] = d[i][j]+1
                    q.append((ni, nj))
            else:
                if d[i][j] < d[ni][nj]:
                    d[ni][nj] = d[i][j]
                    q.appendleft((ni, nj))

if d[goal_i][goal_j] <= 2:
    print('YES')
else:
    print('NO')

#=> https://atcoder.jp/contests/arc005/submissions/19833039