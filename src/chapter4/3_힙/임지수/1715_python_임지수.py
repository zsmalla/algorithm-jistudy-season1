import sys
from heapq import heappop, heappush

input = sys.stdin.readline

N = int(input())
if N == 1:
    print(0)
    exit(0)
heap = []
for _ in range(N):
    heappush(heap, int(input()))
count = 0
while heap:
    weighted_card_pack = heappop(heap) + heappop(heap)
    count += weighted_card_pack
    if not heap:
        break
    else:
        heappush(heap, weighted_card_pack)

print(count)