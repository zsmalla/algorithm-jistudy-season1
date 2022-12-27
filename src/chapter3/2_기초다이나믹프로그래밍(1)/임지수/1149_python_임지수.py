import sys

input = sys.stdin.readline

N = int(input())
costs = [list(map(int, input().rstrip().split())) for _ in range(N)]

for house in range(1, N):
    costs[house][0] += min(costs[house-1][1], costs[house-1][2])
    costs[house][1] += min(costs[house-1][0], costs[house-1][2])
    costs[house][2] += min(costs[house-1][0], costs[house-1][1])

print(min(costs[-1]))