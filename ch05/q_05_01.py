n = int(input())
a = [None]*n
b = [None]*n
c = [None]*n
for i in range(n):
    a[i], b[i], c[i] = map(int, input().split())

# dp[何日目][前日に何をしたのか] = 幸福度
dp = [[-float('infinity')]*3 for _ in range(n+1)]
dp[0][0] = 0
dp[0][1] = 0
dp[0][2] = 0

for i in range(n):
    dp[i+1][0] = max(dp[i+1][0], max(dp[i][1], dp[i][2])+a[i])
    dp[i+1][1] = max(dp[i+1][1], max(dp[i][2], dp[i][0])+b[i])
    dp[i+1][2] = max(dp[i+1][2], max(dp[i][0], dp[i][1])+c[i])
print(max(dp[n]))

#=> https://atcoder.jp/contests/dp/submissions/19195607