import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N = int(input())
gas_stations = []   # min heap
for _ in range(N):
    heappush(gas_stations, list(map(int, input().rstrip().split())))
L, P = map(int, input().rstrip().split())
count = 0
can_visit = []  # max heap

while P < L:
    while gas_stations and gas_stations[0][0] <= P:         # 현재 연료로 갈 수 있는 주유소들
        distance, gas = heappop(gas_stations)
        heappush(can_visit, (-gas, distance))

    if not can_visit:
        count = -1
        break

    P -= heappop(can_visit)[0]
    count += 1

print(count)

'''
갈 수 있는 곳을 max heap에 관리 => 가장 많이 주는 곳 부터 가자
'''
