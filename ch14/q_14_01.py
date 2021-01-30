import collections, functools, sys

sys.setrecursionlimit(10**8)

n, m = map(int, input().split())
g = collections.defaultdict(list)
for _ in range(m):
    x, y = map(int, input().split())
    g[x-1].append(y-1)

@functools.lru_cache(maxsize=None)
def f(cur):
    ans = 0
    for nxt in g[cur]:
        ans = max(ans, f(nxt)+1)
    return ans

print(max(f(cur) for cur in range(n)))

#=> https://atcoder.jp/contests/dp/submissions/19787235