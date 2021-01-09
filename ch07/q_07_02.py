n = int(input())

reds = [tuple(map(int, input().split())) for _ in range(n)]
blues = [tuple(map(int, input().split())) for _ in range(n)]

blues.sort()

ans = 0
for i in range(n):
    a, b = blues[i]
    p = -1
    y_max = -float('inf')
    for j in range(n):
        c, d = reds[j]
        if c < a and d < b:
            if y_max < d:
                p = j
                y_max = d
    
    if p != -1:
        ans += 1
        reds[p] = (float('inf'), float('inf'))

print(ans)

#=> https://atcoder.jp/contests/arc092/submissions/19291229