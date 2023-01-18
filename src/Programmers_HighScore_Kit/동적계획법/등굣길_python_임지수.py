def solution(m, n, puddles):
    MAP = [[1 if j == 0 or i == 0 else 0 for j in range(m)] for i in range(n)]

    if puddles[0]:
        for x, y in puddles:
            MAP[y - 1][x - 1] = 'X'
            if x == 1:
                for r in range(y, n):
                    MAP[r][x - 1] = 0
            if y == 1:
                for c in range(x, m):
                    MAP[y - 1][c] = 0

    for y in range(1, n):
        for x in range(1, m):
            if MAP[y][x] == 'X':
                continue
            up = 0 if MAP[y - 1][x] == 'X' else MAP[y - 1][x]
            left = 0 if MAP[y][x - 1] == 'X' else MAP[y][x - 1]
            MAP[y][x] = up + left
    return MAP[-1][-1] % 1000000007