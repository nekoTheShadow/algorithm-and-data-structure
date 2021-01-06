def solve(n, a):
    import bisect
    b = list(sorted(a))
    for i in range(n):
        print(bisect.bisect_left(b, a[i]))

solve(5, [12, 43, 7, 15, 9])
# 2
# 4
# 0
# 3
# 1