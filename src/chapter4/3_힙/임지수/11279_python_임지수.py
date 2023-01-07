import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    x = int(input())
    if x == 0:
        if not heap:
            print(0)
        else:
            print(-1*heappop(heap))
    else:
        heappush(heap, -1*x)