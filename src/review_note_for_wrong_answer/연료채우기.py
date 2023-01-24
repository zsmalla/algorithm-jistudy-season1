import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input().rstrip())

oil_banks = []
for _ in range(N):
    heappush(oil_banks, tuple(map(int, input().rstrip().split())))

L, P = map(int, input().rstrip().split())
can_go = []
count = 0

while P < L:
    while oil_banks and oil_banks[0][0] <= P:
        distance, oil = heappop(oil_banks)
        heappush(can_go, -oil)      # max heap, 얻을 수 있는 연료 양 기준

    if not can_go:
        count = -1
        break
    P -= heappop(can_go)
    count += 1
print(count)
