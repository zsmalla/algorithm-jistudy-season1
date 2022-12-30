import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

def bfs():
    global cz_count
    queue = deque([(0, 0)])
    visited[0][0] = True
    while queue:
        y, x = queue.popleft()
        before = MAP[y][x]
        if before == 1:
            cz_count -= 1
            MAP[y][x] = 0
            continue
        for d in range(4):
            ny, nx = y+dy[d], x+dx[d]
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((ny, nx))

MAP = [list(map(int, input().rstrip().split())) for _ in range(N)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
cz_count, tm_count = 0, 0
for row in range(N):
    for col in range(M):
        if MAP[row][col] == 1:
            cz_count += 1

while cz_count > 0:
    visited = [[False for _ in range(M)] for _ in range(N)]
    tm_count += 1
    tmp = cz_count
    bfs()

print(tm_count)
print(tmp)