import sys
from collections import deque
input = sys.stdin.readline

def bfs(r, c):
    queue = deque([(r, c)])
    MAP[r][c] += 1
    cnt = 1
    while queue:
        y, x = queue.popleft()
        for d in range(4):
            ny, nx = y+dy[d], x+dx[d]
            if 0 <= ny < N and 0 <= nx < M and MAP[ny][nx]==0:
                queue.append((ny, nx))
                MAP[ny][nx] += 1
                cnt+=1
    return cnt

N, M, K = map(int, input().rstrip().split())
MAP = [[0 for _  in range(M)] for _ in range(N)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    for row in range(y1, y2):
        for col in range(x1, x2):
            MAP[row][col] += 1

result = []

for r in range(N):
    for c in range(M):
        if MAP[r][c] == 0:
            result.append(bfs(r, c))

result.sort()
print(len(result))
print(*result)