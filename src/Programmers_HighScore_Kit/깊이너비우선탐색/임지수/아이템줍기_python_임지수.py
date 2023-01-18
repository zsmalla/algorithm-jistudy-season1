from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2

    MAP = [[0 for _ in range(102)] for _ in range(102)]

    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x * 2, r)
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                if (y == y1 or y == y2 or x == x1 or x == x2) and MAP[y][x] != 2:
                    MAP[y][x] = 1
                else:
                    MAP[y][x] = 2

    queue = deque([(characterY, characterX, 0)])
    MAP[characterY][characterX] = 0
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while queue:
        y, x, cnt = queue.popleft()

        if y == itemY and x == itemX:
            return cnt // 2

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < 102 and 0 <= nx < 102 and MAP[ny][nx] == 1:
                queue.append((ny, nx, cnt + 1))
                MAP[ny][nx] = 0
