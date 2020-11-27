import collections

def f(a):
    lo = 0
    hi = 100

    count = 0
    while hi-lo > 1:
        count += 1
        mi = (lo+hi)//2
        if a < mi:
            hi = mi
        else:
            lo = mi
    return count

print(max(map(f, range(100)))) #=> 7

# 6回では確実に当てることはできない (2^6=64なので)
# 7回では確実に当てることができる