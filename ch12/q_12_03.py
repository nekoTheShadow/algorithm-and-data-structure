import bisect

a = [4,3,5,9,7,1,2,8,6]

# bisect.insortはソート済みの配列に対し、
# 挿入ポイントを2分探索で探し配列に挿入する。
# 2分探索の計算量がO(logN)なので、このアルゴリズムの計算量はO(NlogN)と評価できる
s = []
for v in a:
    bisect.insort(s, v)
    # ここでs[k]とすると、必ずk番目の値が取得できる。
