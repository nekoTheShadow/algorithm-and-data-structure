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

def main():
    import collections
    
    N, K, L = map(int, input().split())
    p = [None]*K
    q = [None]*K
    r = [None]*L
    s = [None]*L
    for i in range(K):
        p[i], q[i] = map(lambda s: int(s)-1, input().split())
    for i in range(L):
        r[i], s[i] = map(lambda s: int(s)-1, input().split())
    
    uf1 = UnionFind(N)
    uf2 = UnionFind(N)
    for i in range(K):
        uf1.union(p[i], q[i])
    for i in range(L):
        uf2.union(r[i], s[i])

    d = collections.Counter((uf1.find(i), uf2.find(i)) for i in range(N))
    ans = ' '.join(str(d[(uf1.find(i), uf2.find(i))]) for i in range(N))
    print(ans)

if __name__ == '__main__':
    main()

#=> https://atcoder.jp/contests/abc049/submissions/19493181