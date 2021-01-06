n = int(input())
p = list(map(int, input().split()))

w = sum(p)
dp = [[False]*(w+1) for _ in range(n+1)]
dp[0][0] = True

for i in range(n):
    for j in range(w+1):
        dp[i+1][j] = dp[i+1][j] or dp[i][j]
        if j+p[i] <= w:
            dp[i+1][j+p[i]] = dp[i+1][j+p[i]] or dp[i][j]

ans = 0
for i in range(w+1):
    if dp[n][i]:
        ans += 1
print(ans)

#=> https://atcoder.jp/contests/tdpc/submissions/19235282