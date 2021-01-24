import collections

# n: 頂点数
# m: 辺数
n, m = map(int, input().split())

# g[x]: xの隣にあるノードのリスト
g = collections.defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split()) 
    g[a].append(b)
    g[b].append(a)

# parent[x]: xが属するグループ
parent = {}

# 深さ優先探索の場合
for start in range(n):
    stack = [start]
    while stack:
        cur = stack.pop()
        if cur in parent:
            continue
            
        parent[cur] = start
        for nxt in g[cur]:
            stack.append(nxt)

# 幅優先探索の場合
for start in range(n):
    que = collections.deque([start])
    while que:
        cur = que.popleft()
        if cur in parent:
            continue
            
        parent[cur] = start
        for nxt in g[cur]:
            que.append(nxt)

