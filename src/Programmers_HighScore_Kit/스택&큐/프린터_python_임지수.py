from collections import deque
from heapq import heappush, heappop

def solution(priorities, location):
    priority_heap = []
    queue = deque()
    count = 0
    for idx, priority in enumerate(priorities):
        queue.append((priority, idx))
        heappush(priority_heap,(-priority, priority))

    while queue:
        priority, idx = queue.popleft()
        if priority == priority_heap[0][1]:
            heappop(priority_heap)
            count += 1
            if idx == location:
                return count
        else:
            queue.append((priority, idx))