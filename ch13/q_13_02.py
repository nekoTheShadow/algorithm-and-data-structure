import collections

# n: 頂点数
# m: 辺数
n, m, s, t = map(int, input().split())

# g[x]: xの隣にあるノードのリスト
g = collections.defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split()) 
    g[a].append(b)
    g[b].append(a)

que = collections.deque([s])
visited = set()
while que:
    cur = que.popleft()
    if cur in visited:
        continue

    visited.add(cur)
    for nxt in g[cur]:
        que.append(nxt)

if t in visited:
    print("Yes")
else:
    print("No")