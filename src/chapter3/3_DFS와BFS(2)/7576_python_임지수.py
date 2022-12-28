import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().rstrip().split())
box = [list(map(int, input().rstrip().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

tomato = []
check = 0
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            tomato.append((i, j, 0))
            visited[i][j] = True
        elif box[i][j] == 0:
            check += 1
queue = deque(tomato)
due = 0

while queue:
    y, x, cnt = queue.popleft()
    for d in range(4):
        ny, nx = y+dy[d], x+dx[d]
        if 0 <= ny <= N-1 and 0 <= nx <= M-1 and box[ny][nx] == 0 and not visited[ny][nx]:
            queue.append((ny, nx, cnt+1))
            visited[ny][nx] = True
            check -= 1
            due = max(due, cnt+1)

print(due) if check == 0 else print(-1)