import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N = int(input())
left_heap, right_heap = [], []  # left : 최대 힙, right : 최소 힙
answer = []
for i in range(N):
    num = int(input())

    if len(left_heap) == len(right_heap):
        heappush(left_heap, (-num, num))
    else:
        heappush(right_heap, (num, num))

    if right_heap and left_heap[0][1] > right_heap[0][1]:
        left_root_value = heappop(left_heap)[1]
        right_root_value = heappop(right_heap)[1]
        heappush(left_heap, (-right_root_value, right_root_value))
        heappush(right_heap, (left_root_value, left_root_value))
    answer.append(left_heap[0][1])

for median in answer:
    print(median)