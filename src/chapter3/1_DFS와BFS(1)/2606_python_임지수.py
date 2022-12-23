import sys
from collections import deque, defaultdict

input = sys.stdin.readline

N = int(input())
M = int(input())
connect_map = defaultdict(deque)
for _ in range(M):
    node1, node2 = map(int, input().rstrip().split())
    connect_map[node1].append(node2)
    connect_map[node2].append(node1)
visited = [False for _ in range(N+1)]

def bfs():
    queue = deque([1])
    visited[1] = True
    cnt = 0
    while queue:
        node = queue.pop()
        for near_node in connect_map[node]:
            if not visited[near_node]:
                queue.append(near_node)
                visited[near_node] = True
                cnt += 1
    return cnt

print(bfs())