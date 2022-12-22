import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

MAP = [False for _ in range(0, 100001)]

def bfs():
    queue = deque([(N, 0)])
    MAP[N] = True
    while queue:
        x, cnt = queue.popleft()
        if x == K:
            return cnt

        for nx in [x+1, x-1, 2*x]:
            if 0 <= nx <= 100000 and not MAP[nx]:
                queue.append((nx, cnt+1))
                MAP[nx] = True
print(bfs())