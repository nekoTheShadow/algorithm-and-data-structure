n = 4
m = 6
a = [1, 2, 3, 4]
b = [3, 4, 5, 6, 7, 8]

s = set(b) 
count = 0
for x in a:
    if x in s:
        count += 1

print(count) #=> 2

# 1. setの構築の計算量がO(m)
# 2. aを舐める計算量がO(n)
# 3. setを利用した存在チェックがO(1)
# よってこのアルゴリズムの計算量はO(n+m)