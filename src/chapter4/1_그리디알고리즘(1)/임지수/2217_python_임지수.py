import sys

input = sys.stdin.readline

N = int(input())
ropes = sorted([int(input()) for _ in range(N)], reverse = True)
result = []

for i in range(N):
    result.append(ropes[i]*(i+1))
print(max(result))
