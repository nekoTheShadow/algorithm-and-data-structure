n = 10
a = [8,7,3,4,10,9,2,6,5,1]

# もっとも小さいものを求める
m1 = float('inf')
for i in range(n):
    m1 = min(m1, a[i])

# もっとも小さい値を除く、小さい値を求める
m2 = float('inf')
for i in range(n):
    if a[i] == m1:
        continue
    m2 = min(m2, a[i])

print(m2) #=> 2
