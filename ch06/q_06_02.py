import bisect

n = int(input())
a = list(sorted(map(int, input().split())))
b = list(sorted(map(int, input().split())))
c = list(sorted(map(int, input().split())))

p = [0]*n
for i in range(n):
    p[i] = bisect.bisect_left(a, b[i])

q = [0]*(n+1)
for i in range(n):
    q[i+1] = q[i] + p[i]

ans = 0
for i in range(n):
    x = bisect.bisect_left(b, c[i])
    ans += q[x]

print(ans)

#=> https://atcoder.jp/contests/abc077/submissions/19236929

