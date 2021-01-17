class UnionFind(object):
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n
    

    def find(self, x):
        if self.parent[x] == x:
            return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        
        if self.size[x] < self.size[y]:
            x, y = y, x
        
        self.parent[y] = x
        self.size[x] += self.size[y]
        return True

def main():
    n, m = map(int, input().split())
    a = [None]*m
    b = [None]*m
    for i in range(m):
        a[i], b[i] = map(int, input().split())
        a[i] -= 1
        b[i] -= 1
    
    ans = 0
    for i in range(m):
        uf = UnionFind(n)
        for j in range(m):
            if i != j:
                uf.union(a[j], b[j])
        if len(set(uf.find(j) for j in range(n))) > 1:
            ans += 1
    
    print(ans)

if __name__ == '__main__':
    main()

#=> https://atcoder.jp/contests/abc075/submissions/19492389