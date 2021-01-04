def g(n, v, ok3, ok5, ok7):
    ans = 0
    if v <= n:
        if ok3 and ok5 and ok7: ans += 1
        ans += g(n, v*10+3, True, ok5, ok7)
        ans += g(n, v*10+5, ok3, True, ok7)
        ans += g(n, v*10+7, ok3, ok5, True)
    return ans

n = int(input())
print(g(n, 0, False, False, False))

#=> https://atcoder.jp/contests/abc114/submissions/19195190