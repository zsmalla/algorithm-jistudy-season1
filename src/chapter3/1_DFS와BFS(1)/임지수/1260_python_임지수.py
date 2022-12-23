import sys
from collections import deque, defaultdict
import heapq

input = sys.stdin.readline

N, M, V = map(int, input().rstrip().split())
graph = defaultdict(list)

for _ in range(M):
    node1, node2 = map(int, input().rstrip().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

for i in range(1, N+1):
    graph[i].sort()

def dfs(node:int, visited:list):
    visited.append(node)

    for next_node in graph[node]:
        if next_node not in visited:
            dfs(next_node, visited)

    return visited
def bfs(node:int, visited:list):
    queue = deque([node])
    visited.append(node)

    while queue:
        current_node = queue.popleft()
        for next_node in graph[current_node]:
            if next_node not in visited:
                queue.append(next_node)
                visited.append(next_node)

    return visited

print(*dfs(V, []))
print(*bfs(V, []))