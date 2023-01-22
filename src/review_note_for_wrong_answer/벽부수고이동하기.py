import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    queue = deque([(0, 0, 1)])
    visited[0][0][1] = 1

    while queue:
        y, x, broken_chance = queue.popleft()
        if y == N-1 and x == M-1:
            return visited[y][x][broken_chance]

        for d in range(4):
            ny = y+dy[d]
            nx = x+dx[d]
            if 0 <= ny < N and 0 <= nx < M:
                if MAP[ny][nx] == '0' and visited[ny][nx][broken_chance] == 0:
                    queue.append((ny, nx, broken_chance))
                    visited[ny][nx][broken_chance] = visited[y][x][broken_chance]+1
                if MAP[ny][nx] == '1' and broken_chance == 1:
                    queue.append((ny, nx, 0))
                    visited[ny][nx][0] = visited[y][x][1]+1

    return -1


N, M = map(int, input().rstrip().split())
MAP = [list(input().rstrip()) for _ in range(N)]
visited = [[[0, 0] for _ in range(M)] for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

print(bfs())


