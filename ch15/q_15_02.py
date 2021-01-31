class UnionFind(object):
    def __init__(self, n):
        self.parents = list(range(n))
        self.sizes = [1]*n
    
    def size(self, x):
        return self.sizes[self.find(x)]

    def find(self, x):
        if self.parents[x] == x:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        
        if self.sizes[x] < self.sizes[y]:
            x, y = y, x
        self.parents[y] = x
        self.sizes[x] += self.sizes[y]
        return True

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    edges = []
    for _ in range(m):
        s, t, c = map(int, input().split())
        edges.append((c, s-1, t-1))
    
    uf = UnionFind(n)
    edges.sort()
    res = []
    for c, s, t in edges:
        if uf.find(s) != uf.find(t):
            uf.union(s, t)
            res.append(c)
    
    res.sort()
    print(res[(n-1)//2])

#=> https://atcoder.jp/contests/jag2012autumn/submissions/19834193