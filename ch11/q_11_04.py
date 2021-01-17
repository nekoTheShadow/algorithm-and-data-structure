class WeightUnionFind(object):
    def __init__(self, n):
        self.parents = list(range(n))
        self.sizes = [1]*n
        self.weights = [0]*n
    
    def size(self, x):
        return self.sizes[self.find(x)]

    def find(self, x):
        if self.parents[x] == x:
            return x
        
        y = self.find(self.parents[x])
        self.weights[x] += self.weights[self.parents[x]]
        self.parents[x] = y
        return y

    def union(self, x, y, w):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return self.weights[y]-self.weights[x] == w
        
        if self.sizes[rx] < self.sizes[ry]:
            x, y = y, x
            rx, ry = ry, rx
            w *= -1

        self.parents[ry] = rx
        self.weights[ry] = w - self.weights[y] + self.weights[x]
        self.sizes[rx] += self.sizes[ry]
        return True

def main():
    n, m = map(int, input().split())
    wuf = WeightUnionFind(n)
    for i in range(m):
        l, r, d = map(int, input().split())
        if not wuf.union(l-1, r-1, d):
            return "No"
    return "Yes"

if __name__ == '__main__':
    print(main())

#=> https://atcoder.jp/contests/arc090/submissions/19493648
