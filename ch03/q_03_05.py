n = int(input())
a = list(map(int, input().split()))

ans = float('inf')
for v in a:
    c = 0
    while v % 2 == 0:
        c += 1
        v /= 2
    ans = min(ans, c)

print(ans)

#=> https://atcoder.jp/contests/abc081/submissions/18427780