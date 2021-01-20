n, m = map(int, input().split())
juices = [tuple(map(int, input().split())) for _ in range(n)]
juices.sort()

cost = 0
for a, b in juices:
    x = min(m, b)
    cost += a * x
    m -= x

print(cost)

#=> https://atcoder.jp/contests/abc121/submissions/19537628