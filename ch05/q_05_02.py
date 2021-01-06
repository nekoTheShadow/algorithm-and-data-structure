from typing import List

def solve(n: int, a: List[int], w: int) -> bool:
    dp = [[False]*(w+1) for _ in range(n+1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(w+1):
            dp[i+1][j] = dp[i+1][j] or dp[i][j]
            if j+a[i] <= w:
                dp[i+1][j+a[i]] = dp[i+1][j+a[i]] or dp[i][j]
    return dp[n][w]

print(solve(5, [1,3,7,10,13], 21)) #=> True
print(solve(5, [2,4,6,8,10], 19)) #=> False

#=> https://ja.wikipedia.org/wiki/%E9%83%A8%E5%88%86%E5%92%8C%E5%95%8F%E9%A1%8C