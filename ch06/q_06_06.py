a, b, c = map(int, input().split())

def f(t):
    import math
    return a*t + b*math.sin(c*t*math.pi)

ok = 10**10
ng = -1

while True:
    mi = (ok+ng)/2
    if abs(f(mi)-100) <= 10**-6:
        print(mi)
        exit(0)

    if f(mi) >= 100:
        ok = mi
    else:
        ng = mi

#=> https://atcoder.jp/contests/abc026/submissions/19251390