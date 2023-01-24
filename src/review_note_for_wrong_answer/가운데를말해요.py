import sys
from heapq import heappush, heappop

input = sys.stdin.readline

'''
최대힙 / 최소힙
1,2,5 / 7, 9

최대힙, 최소힙으로 구성, 양 쪽 개수 맞춰서 삽입
삽입 후 양쪽 힙 비교 후 최대힙[0] > 최소힙[0]이면 교환
'''
N = int(input().rstrip())
max_heap, min_heap = [], []
for _ in range(N):
    if len(max_heap) == len(min_heap):
        heappush(max_heap, -int(input().rstrip()))
    else:
        heappush(min_heap, int(input().rstrip()))
    if min_heap and -max_heap[0] > min_heap[0]:
        tmp_max = -heappop(max_heap)
        tmp_min = heappop(min_heap)
        heappush(min_heap, tmp_max)
        heappush(max_heap, -tmp_min)
    print(-max_heap[0])