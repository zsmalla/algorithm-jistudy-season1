# 가장 빠른 방법! - 백준 통과(O)
import sys
import heapq

N = int(input())
result = []

for i in range(N):
    result.append(int(sys.stdin.readline().rstrip()))

result.sort()
for i in result:
    print(i)

#--------------------------------------------------
#
# heapq 라이브러리 사용 - 백준 통과(X)
# import heapq
#
# N = int(input())
# result = []
#
# for i in range(N):
#     heapq.heappush(result,input())
# for l in range(N):
#     print(heapq.heappop(result))