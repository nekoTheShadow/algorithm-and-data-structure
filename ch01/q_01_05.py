result = [
    "09 ## 09 10 11 12 ## 16",
    "08 ## 08 ## 12 13 14 15",
    "07 06 07 ## 13 ## ## 16",
    "## 05 ## ## 12 11 10 ##",
    "03 04 05 ## ## ## 09 ##",
    "02 ## 04 05 06 07 08 ##",
    "01 02 03 04 05 ## 07 08",
    "00 01 02 03 04 05 06 07",
]

cost = []
for line in result:
    row = line.split(' ')
    cost.append(list(float('inf') if ch=='##' else int(ch) for ch in row))

goal_x, goal_y = 0, 7
h, w = len(cost), len(cost[0])

stack = [[(goal_x, goal_y)]]
paths = []
while stack:
    path = stack.pop()
    x, y = path[-1]
    if cost[x][y] == 0:
        paths.append(path)
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x+dx, y+dy
        if 0 <= nx < h and 0 <= ny < w and cost[x][y]-1 == cost[nx][ny]:
            stack.append([*path, (nx, ny)])

for path in paths:
    answer = list(line.split(' ') for line in result)
    for x, y in path:
        answer[x][y] = 'XX'
    for row in answer:
        print(' '.join(row))
    print('-----------------------')

# あるマスのコストがNの場合、コストがN-1のマスが直前のマスである。
# この規則に従って全探索すれば良い

# 09 ## XX XX XX 12 ## XX
# 08 ## XX ## XX XX XX XX
# 07 XX XX ## 13 ## ## 16
# ## XX ## ## 12 11 10 ##
# XX XX 05 ## ## ## 09 ##
# XX ## 04 05 06 07 08 ##
# XX 02 03 04 05 ## 07 08
# XX 01 02 03 04 05 06 07
# -----------------------
# 09 ## XX XX XX XX ## XX
# 08 ## XX ## 12 XX XX XX
# 07 XX XX ## 13 ## ## 16
# ## XX ## ## 12 11 10 ##
# XX XX 05 ## ## ## 09 ##
# XX ## 04 05 06 07 08 ##
# XX 02 03 04 05 ## 07 08
# XX 01 02 03 04 05 06 07
# -----------------------
