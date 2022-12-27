import sys

input = sys.stdin.readline

T = int(input())
dp = [0, 1]+[-1 for _ in range(2, 41)]
zero_one = [(1, 0), (0, 1)]
for i in range(2, 42):
    zero_one.append((zero_one[i-1][0]+zero_one[i-2][0], zero_one[i-1][1]+zero_one[i-2][1]))
for _ in range(T):
    n = int(input())
    print(*zero_one[n])