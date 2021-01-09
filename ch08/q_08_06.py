import collections

n = 6
m = 9
a = [1, 2, 2, 3, 3, 3]
b = [2, 2, 3, 3, 3, 4, 4, 4, 4]

c = collections.Counter(b)
ans = 0
for x in a:
    ans += c[x]
print(ans) #=> 13

# 1. Counterの構築の計算量がO(m)
# 2. aを舐める計算量がO(n)
# 3. CounterへのアクセスはO(1)
# よってこのアルゴリズムの計算量はO(n+m)