import bisect

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

# マスに書かれている数値の中でmi以上の値がk個以上あるか
ng = min(a)*min(b)-1
ok = max(a)*max(b)+1
while abs(ok-ng) > 1:
    mi = (ok+ng)//2

    cnt = 0
    for x in a:
        if x <= mi:
            y = mi//x
            cnt += bisect.bisect(b, y)

    if k <= cnt:
        ok = mi
    else:
        ng = mi

print(ok)

#=> https://atcoder.jp/contests/arc037/submissions/19251145