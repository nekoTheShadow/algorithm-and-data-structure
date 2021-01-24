a = [
    ".#....#.",
    ".#.#....",
    "...#.##.",
    "#.##...#",
    "...###.#",
    ".#.....#",
    ".....#..",
    "........",
]

h, w = 8, 8
start_x, start_y = 7, 0
goal_x, goal_y = 0, 7

d = [[float('inf')]*w for _ in range(h)]
stack = []
prev = {}

d[start_x][start_y] = 0
stack.append((start_x, start_y))
while stack:
    x, y = stack.pop()
    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        nx, ny = x+dx, y+dy
        if 0 <= nx < h and 0 <= ny < w and a[nx][ny] == '.' and d[x][y]+1 < d[nx][ny]:
            d[nx][ny] = d[x][y]+1
            prev[(nx, ny)] = (x, y)
            stack.append((nx, ny))

b = list(map(list, a))
cur_x, cur_y = goal_x, goal_y
while (cur_x, cur_y) != (start_x, start_y):
    b[cur_x][cur_y] = "$"
    cur_x, cur_y = prev[(cur_x, cur_y)]

b[start_x][start_y] = "S"
b[goal_x][goal_y] = "G"
for row in b:
    print(''.join(row))