n = 4
m = 6
a = [1, 2, 3, 4]
b = [3, 4, 5, 6, 7, 8]
k = 10

s = set(b) 
ok = False
for x in a:
    if (k-x) in s:
        ok = True

print(ok) #=> True