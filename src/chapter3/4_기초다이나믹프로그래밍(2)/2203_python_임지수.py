import sys

input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
coins = [int(input()) for _ in range(n)]
dp = [1]+[0 for _ in range(1, k+1)]

for coin in coins:
    for j in range(1, k+1):
        if j-coin >= 0:
            dp[j] += dp[j-coin]

print(dp[k])