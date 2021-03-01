def median5(a, lo, hi):
    # in-place insertion sort
    for i in range(lo+1, hi+1):
        j = i
        while lo <= j-1 and a[j-1] > a[j]:
            a[j-1], a[j] = a[j], a[j-1]
            j -= 1
    return a[(lo+hi)//2]

def get_pivot(a, lo, hi):
    i = lo
    medians = []
    while i <= hi:
        medians.append(median5(a, i, min(i+4, hi)))
        i += 5
    if len(medians) == 1:
        return medians[0]
    else:
        return kth_element(medians, len(medians)//2+1)

def partition(a, lo, hi):
    pivot = get_pivot(a, lo, hi)
    i = lo
    j = hi
    while True:
        while a[i] < pivot: i += 1
        while a[j] > pivot: j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]
        else:
            return j

def quick_select(a, lo, hi, k):
    i = partition(a, lo, hi)
    if i == k-1:
        return a[i]
    elif i < k-1:
        return quick_select(a, i+1, hi, k)
    else:
        return quick_select(a, lo, i-1, k)

def kth_element(a, k):
    return quick_select(a, 0, len(a)-1, k)


a = [8,34,32,2,22,20,10,26,6,28,4,14,18,12,30,24,16]
print(kth_element(a, 1)) #=> 2
print(kth_element(a, 5)) #=> 10
print(kth_element(a, 9)) #=> 18
print(kth_element(a, 13)) #=> 26
print(kth_element(a, 17)) #=> 34

# <<参考>>
# https://naoyat.hatenablog.jp/entry/median-of-medians
# https://ja.wikipedia.org/wiki/%E4%B8%AD%E5%A4%AE%E5%80%A4%E3%81%AE%E4%B8%AD%E5%A4%AE%E5%80%A4
