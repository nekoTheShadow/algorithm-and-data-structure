import sys

sys.setrecursionlimit(10**9+7)

n = int(input())
x = [None]*(n-1)
y = [None]*(n-1)
for i in range(n-1):
    x[i], y[i] = [int(s) - 1 for s in input().split()]

g = [[] for _ in range(n)]
for i in range(n-1):
    g[x[i]].append(y[i])
    g[y[i]].append(x[i])

memo = {}
def f(parent, current, color):
    key = (current, color)
    if key in memo:
        return memo[key]

    ans = 1
    if color == 0:
        # 自分自身が黒ならば、子供はすべて白
        for child in g[current]:
            if child == parent:
                continue
            ans *= f(current, child, 1)
    else:
        # 自分自身が白ならば、子供は黒または白
        for child in g[current]:
            if child == parent:
                continue
            ans *= f(current, child, 0) + f(current, child, 1)
    
    memo[key] = ans % (10**9+7)
    return memo[key]

ans = (f(-1, 0, 0) + f(-1, 0, 1)) % (10**9+7)
print(ans)

#=> https://atcoder.jp/contests/dp/submissions/20026220

