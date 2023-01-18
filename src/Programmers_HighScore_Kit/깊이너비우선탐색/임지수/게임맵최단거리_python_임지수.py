from collections import deque


def solution(maps):
    N, M = len(maps), len(maps[0])
    visited = [[False for _ in range(M)] for _ in range(N)]
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    queue = deque([(0, 0, 1)])
    visited[0][0] = True

    while queue:
        y, x, cnt = queue.popleft()

        if y == N - 1 and x == M - 1:
            return cnt

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if 0 <= ny < N and 0 <= nx < M and maps[ny][nx] and not visited[ny][nx]:
                queue.append((ny, nx, cnt + 1))
                visited[ny][nx] = True

    return -1

