import collections

n = 8
g = {}
g[0] = [5]
g[1] = [3, 6]
g[2] = [5, 7]
g[3] = [0, 7]
g[4] = [1, 2, 6]
g[5] = []
g[6] = [7]
g[7] = [0]


h = {x: [] for x in range(n)}
for x in g:
    for y in g[x]:
        h[y].append(x)

deg = {x: len(g[x]) for x in range(n)}
que = collections.deque()
for x in deg:
    if deg[x] == 0:
        que.append(x)

order = []
while que:
    cur = que.popleft()
    order.append(cur)
    for nxt in h[cur]:
        deg[nxt] -= 1
        if deg[nxt] == 0:
            que.append(nxt)

order.reverse()
print(order) #=> [4, 1, 6, 3, 2, 7, 0, 5]