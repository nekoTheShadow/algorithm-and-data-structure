def prime_division(n):
    x = 2
    d = {}
    while x * x <= n:
        while n % x == 0:
            n //= x
            d[x] = d.get(x, 0) + 1
        x += 1
    if n > 1:
        d[n] = d.get(n, 0) + 1
    return d

def phi(n):
    for p in prime_division(n):
        n = (n*(p-1))//p
    return n

def lcm(x, y):
    import math
    return x*y//math.gcd(x, y)

def solve(a, m):
    if pow(a, m, m) == 0: return m
    if a == 1 or m == 1: return 1

    phi_m = phi(m)
    return pow(a, solve(a, phi_m), lcm(phi_m, m))

q = int(input())
for i in range(q):
    a ,m = map(int,input().split())
    print(solve(a,m))

#=> https://atcoder.jp/contests/tenka1-2017/submissions/20588461
# <参考> https://drken1215.hatenablog.com/entry/2018/03/09/003000