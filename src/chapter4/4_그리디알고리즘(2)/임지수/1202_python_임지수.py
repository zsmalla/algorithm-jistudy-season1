import sys
from heapq import heappop, heappush

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
jewells = []
bags = []
count = 0

for j in range(N):
    heappush(jewells, list(map(int, input().rstrip().split())))
for b in range(K):
    heappush(bags, int(input()))
can_steal = []
for _ in range(K):
    bag = heappop(bags)
    while jewells and jewells[0][0] <= bag:
        heappush(can_steal, -heappop(jewells)[1])

    if can_steal:
        count += -heappop(can_steal)
    elif not jewells:
        break

print(count)