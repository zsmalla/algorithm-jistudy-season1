import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
MAP = [list(input()) for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
results = []

def bfs(row, col):

    if MAP[row][col] == '1':
        queue = deque([(row, col)])
        MAP[row][col] = '0'
        count = 1
    else:
        queue = deque([])
        count = 0

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny <= N-1 and 0 <= nx <= N-1:
                if MAP[ny][nx] == '1':
                    queue.append((ny, nx))
                    MAP[ny][nx] = '0'
                    count += 1
    return count

for r in range(N):
    for c in range(N):
         result = bfs(r, c)
         if result != 0:
             results.append(result)

print(len(results))
for num in sorted(results):
    print(num)