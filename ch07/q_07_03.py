import operator

n = int(input())

t = [tuple(map(int, input().split())) for _ in range(n)]
t.sort(key=operator.itemgetter(1))

cur = 0
for (a, b) in t:
    cur += a
    if b < cur:
        print("No")
        exit(0)
print("Yes")