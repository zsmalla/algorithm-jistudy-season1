import sys

input = sys.stdin.readline

N = int(input().rstrip())
houses = [list(map(int,input().rstrip().split())) for _ in range(N)]

for i in range(1, N):
    houses[i][0] += min(houses[i-1][1], houses[i-1][2])
    houses[i][1] += min(houses[i-1][0], houses[i-1][2])
    houses[i][2] += min(houses[i-1][0], houses[i-1][1])
print(min(houses[-1]))