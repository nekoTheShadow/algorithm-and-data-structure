a = [6,4,3,7,2,9,1,5,8]
n = 9

b = [(a[i], i) for i in range(n)]
b.sort()

d = {}
for i in range(n):
    d[b[i][0]] = i+1


for i in range(n):
    print(f"a[{i}]={a[i]} --> {d[a[i]]}番目")

# 計算量はsortがボトルネックになってO(NlogN) 
# a[0]=6 --> 6番目
# a[1]=4 --> 4番目
# a[2]=3 --> 3番目
# a[3]=7 --> 7番目
# a[4]=2 --> 2番目
# a[5]=9 --> 9番目
# a[6]=1 --> 1番目
# a[7]=5 --> 5番目
# a[8]=8 --> 8番目