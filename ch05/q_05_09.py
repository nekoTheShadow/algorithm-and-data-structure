n = int(input())
a = list(map(int, input().split()))

s = [0]*(n+1)
for i in range(n):
    s[i+1] = s[i] + a[i]

dp = [[-1]*n for _ in range(n)]
def f(l, r):
    if l == r:
        return 0
    if dp[l][r] != -1:
        return dp[l][r]
    dp[l][r] = min(f(l, i) + f(i + 1, r) + s[r + 1] - s[l] for i in range(l, r))
    return dp[l][r]

print(f(0, n-1))

#=> https://atcoder.jp/contests/dp/submissions/20172716

