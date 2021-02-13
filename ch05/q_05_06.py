n = int(input())
w = int(input())
a = list(map(int, input().split()))
m = list(map(int, input().split()))

dp = [[float('inf')]*(w+1) for _ in range(n+1)]
dp[0][0] = 0
for i in range(n):
    for j in range(w+1):
        if dp[i][j] != float('inf'):
            dp[i+1][j] = min(dp[i+1][j], 0)
        if j+a[i] <= w and dp[i+1][j] < m[i]:
            dp[i+1][j+a[i]] = min(dp[i+1][j+a[i]], dp[i+1][j]+1)

if dp[n][w]:
    print('YES')
else:
    print('NO')