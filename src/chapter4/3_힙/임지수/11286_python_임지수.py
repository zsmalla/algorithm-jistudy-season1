import sys
from heapq import heappop, heappush

input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    x = int(input())
    if x != 0:
        heappush(heap, (abs(x), x))
    else:
        if not heap:
            print(0)
        else:
            print(heappop(heap)[1])
