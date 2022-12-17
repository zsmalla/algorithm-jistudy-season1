# heapq 라이브러리 사용
import heapq

N = int(input())
result = []

for i in range(N):
    heapq.heappush(result,input())
for l in range(N):
    print(heapq.heappop(result))


