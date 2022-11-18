import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    heappush(heap, int(input()))
while heap:
    print(heappop(heap))