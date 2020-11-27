n = 10
a = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]
v = 1

c = 0
for i in range(n):
    if a[i] == v:
        c += 1
print(c) #=> 4
