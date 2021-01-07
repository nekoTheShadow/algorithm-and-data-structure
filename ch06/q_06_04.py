from typing import List

def is_ok(n: int, c: int, x: List[int], m: int) -> bool:
    q = [x[0]]
    for i in range(1, n):
        if q[-1] + m <= x[i]:
            q.append(x[i])
    return len(q) >= c

n, c = map(int, input().split())
x = [int(input()) for _ in range(n)]
x.sort()

ok = -1
ng = 1000000000 + 1

while abs(ok-ng) > 1:
    mi = (ok+ng) // 2
    if is_ok(n, c, x, mi):
        ok = mi
    else:
        ng = mi
print(ok)

#=> http://poj.org/problem?id=2456