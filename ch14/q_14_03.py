import collections

n, m = map(int, input().split())
g = collections.defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    g[u-1].append(v-1)
s, t = map(lambda s: int(s)-1, input().split())

q = collections.deque()
d = {}
q.append((s, 0))
d[(s, 0)] = 0
while q:
    cur, par = q.popleft()
    for nxt in g[cur]:
        nxt_par = (par+1)%3
        if not (nxt, nxt_par) in d:
            d[(nxt, nxt_par)] = d[(cur, par)] + 1
            q.append((nxt, nxt_par))

if (t, 0) in d:
    print(d[(t, 0)]//3)
else:
    print(-1)

#=> https://atcoder.jp/contests/abc132/submissions/19832514