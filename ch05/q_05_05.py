n = int(input())
w = int(input())
a = list(map(int, input().split()))

dp = [[False]*(w+1) for _ in range(n+1)]
dp[0][0] = True
for i in range(n):
    for j in range(w+1):
        dp[i+1][j] |= dp[i][j]
        if j+a[i] <= w:
            dp[i+1][j+a[i]] |= dp[i+1][j]

if dp[n][w]:
    print('YES')
else:
    print('NO')