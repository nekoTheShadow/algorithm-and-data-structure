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

def bfs():
    color = [-1]*n
    que = collections.deque()
    color[0] = 0
    que.append(0)
    while que:
        cur = que.popleft()
        for nxt in g[cur]:
            if color[nxt] == -1:
                if color[cur] == color[nxt]:
                    return False
                color[nxt] = 1-color[cur]
                que.append(nxt)
    return True
    