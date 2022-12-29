import sys
from collections import deque

input = sys.stdin.readline


M, N, H = map(int, input().rstrip().split())
box = [[list(map(int, input().rstrip().split())) for _ in range(N)] for _ in range(H)]
visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]
tomato = []
check = 0

for h in range(H):
    for n in range(N):
        for m in range(M):
            if box[h][n][m] == 1:
                tomato.append((h, n, m, 0))
                visited[h][n][m] = True
            elif box[h][n][m] == 0:
                check += 1

queue = deque(tomato)
dz = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dx = [0, 0, 0, 0, -1, 1]
due = 0

while queue:
    z, y, x, cnt = queue.popleft()
    due = max(due, cnt)
    for d in range(6):
        nz, ny, nx = z+dz[d], y+dy[d], x+dx[d]
        if 0 <= nz <= H-1 and 0 <= ny <= N-1 and 0 <= nx <= M-1:
            if box[nz][ny][nx] == 0 and not visited[nz][ny][nx]:
                queue.append((nz, ny, nx, cnt+1))
                visited[nz][ny][nx] = True
                check-=1

print(due) if check == 0 else print(-1)