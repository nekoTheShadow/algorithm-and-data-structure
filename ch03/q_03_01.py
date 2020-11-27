n = 10
a = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]
v = 3

found_id = -1
for i in range(n):
    if a[i] == v:
        found_id = i

print(found_id) #=> 8