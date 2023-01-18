from collections import deque

def rotate_left(polygon):
    return [[c[i] for c in polygon] for i in range(len(polygon[0]) - 1, -1, -1)]

def make_box(info):
    points, max_min = info
    box_y_len = max_min[0] - max_min[2] + 1
    box_x_len = max_min[1] - max_min[3] + 1
    box = [[0 for _ in range(box_x_len)] for _ in range(box_y_len)]

    min_y, min_x = max_min[2], max_min[3]

    for y, x in points:
        box[y - min_y][x - min_x] = 1

    return box

def match(empty, polygon):
    box = make_box(empty)
    poly = make_box(polygon)

    for idx in range(4):
        if idx != 0:
            poly = rotate_left(poly)
        if box == poly:
            return len(empty[0])

    return 0

def bfs(MAP, start, find, N):
    queue = deque([start])
    points = [[], [0, 0, 50, 50]]  # points, [max_y, max_x, min_y, min_x]
    MAP[start[0]][start[1]] = 2
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while queue:
        y, x = queue.popleft()

        points[0].append([y, x])
        points[1] = [max(y, points[1][0]), max(x, points[1][1]), \
                     min(y, points[1][2]), min(x, points[1][3])]
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if 0 <= ny < N and 0 <= nx < N and MAP[ny][nx] == find:
                queue.append((ny, nx))
                MAP[ny][nx] = 2

    return points

def solution(game_board, table):
    answer = 0
    N = len(game_board)
    polygons = []
    emptys = []
    for i in range(N):
        for j in range(N):
            if table[i][j] == 1:
                polygons.append(bfs(table, (i, j), 1, N))
            if game_board[i][j] == 0:
                emptys.append(bfs(game_board, (i, j), 0, N))

    visited_polygons = [False for _ in range(len(polygons))]
    visited_emptys = [False for _ in range(len(emptys))]

    for empty_idx in range(len(emptys)):
        for polygon_idx in range(len(polygons)):
            if (visited_polygons[polygon_idx] or visited_emptys[empty_idx]) \
                    or (len(emptys[empty_idx][0]) != len(polygons[polygon_idx][0])):
                continue
            tmp = match(emptys[empty_idx], polygons[polygon_idx])
            if tmp:
                visited_polygons[polygon_idx] = True
                visited_emptys[empty_idx] = True
                answer += tmp

    return answer