import sys

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

coins = [int(input()) for _ in range(N)]
result = 0
for coin in reversed(coins):
    result += K//coin
    K %= coin
    if K == 0:
        break
print(result)