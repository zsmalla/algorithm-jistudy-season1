import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    queue = deque([(0, 0, 1)])
    visited[0][0][1] = 1
    # visited[y][x][0] : 벽을 부순 후 경로
    # visited[y][x][1] : 벽을 부수기 전 경로
    while queue:
        y, x, cnt = queue.popleft()     # cnt : 벽 부술 수 있는 기회(최대 1)
        print(y, x, cnt)
        if y == N-1 and x == M-1:
            return visited[y][x][cnt]

        for d in range(4):
            ny, nx = y+dy[d], x+dx[d]
            if 0 <= ny <= N-1 and 0 <= nx <= M-1:
                if MAP[ny][nx] == '0' and visited[ny][nx][cnt] == 0:   # 이동
                    queue.append((ny, nx, cnt))
                    visited[ny][nx][cnt] = visited[y][x][cnt]+1
                if MAP[ny][nx] == '1' and cnt == 1:                    # 벽 부순 후 이동
                    queue.append((ny, nx, 0))                          # 다른 경로에서는 다른 벽을 부수게 됨
                    visited[ny][nx][0] = visited[y][x][1]+1
    return -1

N, M = map(int, input().rstrip().split())
MAP = [list(input().rstrip()) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

print(bfs())

'''
5 5
00100
00000
10010
00101
00010
'''