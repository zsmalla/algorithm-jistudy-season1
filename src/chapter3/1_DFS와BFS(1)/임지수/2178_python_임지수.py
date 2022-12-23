import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
MAP = [list(input()) for _ in range(N)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs():
    queue = deque([(0, 0, 1)])
    while queue:
        row, col, cnt = queue.popleft()
        if row == N-1 and col == M-1:
            return cnt
        for i in range(4):
            ny, nx = row+dy[i], col+dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if MAP[ny][nx] == '1':
                    queue.append((ny, nx, cnt+1))
                    MAP[ny][nx] = '0'

print(bfs())
