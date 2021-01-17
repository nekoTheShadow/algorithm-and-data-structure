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
    n, m = map(int, input().split())
    a = [None]*m
    b = [None]*m
    for i in range(m):
        a[i], b[i] = map(int, input().split())
        a[i] -= 1
        b[i] -= 1
    
    uf = UnionFind(n)
    answers = [0]*(m+1)
    answers[m] = n*(n-1)//2

    for i in reversed(range(m)):
        if uf.find(a[i]) == uf.find(b[i]):
            answers[i] = answers[i+1]
        else:
            answers[i] = answers[i+1] - uf.size(a[i])*uf.size(b[i])
        uf.union(a[i], b[i])

    for answer in answers[1:]:
        print(answer)

if __name__ == '__main__':
    main()

#=> https://atcoder.jp/contests/abc120/submissions/19492891