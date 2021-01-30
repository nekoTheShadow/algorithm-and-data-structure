import collections, functools

n, m = map(int, input().split())
g = collections.defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    g[a-1].append((b-1, -c))

negative = False
dist = [float('inf')]*n
dist[0] = 0 
for time in range(n*2+1):
    for v in range(n):
        if dist[v] == float('inf'):
            continue
        for w, c in g[v]:
            if dist[w] > dist[v] + c:
                dist[w] = dist[v] + c
                if w == n-1 and time == n*2:
                    negative = True

if negative:
    print('inf')
else:
    print(-dist[n-1])