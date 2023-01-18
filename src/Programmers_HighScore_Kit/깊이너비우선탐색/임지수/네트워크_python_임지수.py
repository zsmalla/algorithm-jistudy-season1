from collections import deque

visited = []


def bfs(start, n, computers):
    global visited

    queue = deque([start])
    visited[start] = True

    while queue:
        x = queue.popleft()
        for nx, is_connect in enumerate(computers[x]):
            if is_connect and not visited[nx]:
                queue.append(nx)
                visited[nx] = True
    return 1


def solution(n, computers):
    global visited
    count = 0
    visited = [False for _ in range(n)]

    for i in range(n):
        if not visited[i]:
            count += bfs(i, n, computers)

    return count