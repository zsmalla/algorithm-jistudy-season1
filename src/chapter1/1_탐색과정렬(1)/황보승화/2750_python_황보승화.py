#1번
# heapq 라이브러리 사용
import heapq

def heapsort(iterable):
    h = []
    result = []

    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)  # heapq.heappush() : 힙에서 원소를 삽입할 때

    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))  # heapq.heappop() : 합에서 원소를 꺼낼 때 항상 가장 작은 원소를 꺼낸다.

    return result

N = int(input())
unsorted_list = []

for i in range(N):
    unsorted_list.append(int(input()))

result = heapsort(unsorted_list)
for j in result:
    print(j)

#----------------------------------------------------

# 2번
# N = int(input())
# arr = []

# for i in range(N):
#   arr.append(int(input()))

# for j in range(len(arr)):
#   for k in range(len(arr)):
#     if arr[j] < arr[k]:
#         arr[j], arr[k] = arr[k], arr[j]

# for l in arr:
#   print(l)