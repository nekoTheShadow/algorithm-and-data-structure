def t(n):
    if n == 0: return 0
    if n == 1: return 0
    if n == 2: return 1
    return t(n-1) + t(n-2) + t(n-3)

for i in range(10):
    print(f't({i})={t(i)}')
# t(0)=0
# t(1)=0
# t(2)=1
# t(3)=1
# t(4)=2
# t(5)=4
# t(6)=7
# t(7)=13
# t(8)=24
# t(9)=44