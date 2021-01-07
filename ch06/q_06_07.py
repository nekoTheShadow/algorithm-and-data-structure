class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
  
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
  
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

# 転倒数の個数を数える。
def inversion(a):
    mi = min(a)
    if mi <= 0:
        for i in range(len(a)):
            a[i] += mi*-1+1

    bit = Bit(max(a))
    ans = 0
    for i in range(len(a)):
        bit.add(a[i], 1)
        ans += i + 1 - bit.sum(a[i])    
    return ans

n = int(input())
a = list(map(int, input().split()))

def is_ok(k):
    b = [0]*n
    c = [0]*(n+1)
    d = [0]*(n+1)

    for i in range(n):
        b[i] = 1 if a[i] <= k else 0
    for i in range(n):
        c[i+1] = c[i]+b[i]
    for i in range(n+1):
        d[i] = 2*c[i] - i

    d.reverse()
    return n*(n+1)//4 < inversion(d)

ok = max(a)+1
ng = 0
while abs(ok-ng) > 1:
    mi = (ok+ng)//2
    if is_ok(mi):
        ok = mi
    else:
        ng = mi

print(ok)

# 参考
# https://www.creativ.xyz/arc101-d-916/
# https://ikatakos.com/pot/programming_algorithm/dynamic_programming/inversion

#=> https://atcoder.jp/contests/arc101/submissions/19252381 (PyPy3)