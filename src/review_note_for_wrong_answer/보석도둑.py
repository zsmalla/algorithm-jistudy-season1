import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
jewels = []
for _ in range(N):
    heappush(jewels, tuple(map(int, input().rstrip().split())))     # min heap, 보석 무게 순
bags = sorted([int(input().rstrip()) for _ in range(K)])
jewels_can_into_bag = []
result = 0

for bag in bags:
    while jewels and jewels[0][0] <= bag:
        M, V = heappop(jewels)
        heappush(jewels_can_into_bag, -V)   # max heap, 보석 가격 순

    if jewels_can_into_bag:
        result -= heappop(jewels_can_into_bag)

print(result)
