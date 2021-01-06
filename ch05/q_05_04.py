def solve(n, a, w, k):
    # dp[どこまで見たか][総和] = 選んだ整数の個数の最小値
    dp = [[float('inf')]*(w+1) for _ in range(n+1)]
    dp[0][0] = 0

    for i in range(n):
        for j in range(w+1):
            dp[i+1][j] = min(dp[i+1][j], dp[i][j])
            if j+a[i] <= w:
                dp[i+1][j+a[i]] = min(dp[i+1][j+a[i]], dp[i][j]+1)
    
    return dp[n][w] <= k

print(solve(3, [7, 5, 3], 10, 2)) #=> True
print(solve(3, [7, 5, 3], 10, 1)) #=> False

#=> https://qiita.com/drken/items/a5e6fe22863b7992efdb
#=> 問題 6:　K個以内部分和問題 から引用

