# - 葉は0で塗る
# - 子供が全て塗られた頂点について、
#   - 子供が全て1なら0で塗る
#   - 子供に1つでも0があるなら1で塗る
# ---> 0で塗られた頂点が最大安定集合になる。
# 参考: https://www.net.ist.i.kyoto-u.ac.jp/members/shuichi/algintro/alg-4s.pdf
# 参考: q_18_01.pdf

n = 15
edges = [
    (0, 1),
    (0, 2),
    (0, 3),
    (1, 4),
    (1, 5),
    (2, 6),
    (2, 7),
    (3, 8),
    (3, 9),
    (6, 10),
    (6, 11),
    (7, 12),
    (7, 13),
    (9, 14),
]

g = [[] for _ in range(n)]
for x, y in edges:
    g[x].append(y)
    g[y].append(x)

colors = [-1]*n

def dfs(parent, current):
    if colors[current] != -1:
        return colors[current]

    children = g[current]
    if len(children) == 1:
        colors[current] = 0
        return 0
    
    has_zero = False
    for child in g[current]:
        if child == parent:
            continue
        if dfs(current, child) == 0:
            has_zero = True
    
    if has_zero:
        colors[current] = 1
        return 1
    else:
        colors[current] = 0
        return 0

dfs(-1, 0)
print(sum(1 for color in colors if color == 0)) #=> 9
