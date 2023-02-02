import sys
from collections import deque, defaultdict

input = sys.stdin.readline

def bfs(st_idx, things_weight):
    queue = deque([st_idx])
    visited[st_idx] = True
    while queue:
        idx = queue.popleft()

        if idx == end_idx-1:
            return True

        for nxt_idx, bridge_weight in MAP[idx]:
            if not visited[nxt_idx] and bridge_weight >= things_weight:
                queue.append(nxt_idx)
                visited[nxt_idx] = True

    return False

N, M = map(int, input().rstrip().split())
MAP = defaultdict(list)
max_weight = 0

for _ in range(M):
    A, B, C = map(int, input().rstrip().split())
    max_weight = max(max_weight, C)
    MAP[A-1].append((B-1, C))
    MAP[B-1].append((A-1, C))

start_idx, end_idx = map(int, input().rstrip().split())

low, high = 1, max_weight

while low <= high:
    visited = [False for _ in range(N)]
    mid = (low + high) // 2
    if bfs(start_idx-1, mid):
        low = mid+1
    else:
        high = mid-1

print(high)

'''
6 9
1 2 7
1 3 8
1 4 7
1 6 9
2 3 7
3 4 7
3 5 7
4 5 7
4 6 7
6 3
'''