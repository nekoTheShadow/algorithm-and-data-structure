import itertools, bisect

n, m = map(int, input().split())
p = [int(input()) for _ in range(n)]
p.append(0)

q = list(sorted(set(x+y for x, y in itertools.product(p, repeat=2))))
ans = 0
for x in q:
    if m-x >= 0:
        i = bisect.bisect(q, m-x)
        if i < len(q) and q[i] == m-x:
            ans = max(ans, x+q[i])
        else:
            ans = max(ans, x+q[i-1])
print(ans)

#=> https://atcoder.jp/contests/joi2008ho/submissions/19237487