import sys

input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
coins = [int(input().rstrip()) for _ in range(n)]
dp = [1] + [0 for _ in range(1, k+1)]

for coin in coins:
    for i in range(1, k+1):
        if i >= coin:
            dp[i] += dp[i-coin]
print(dp[k])
'''
    1   2   3   4   5   6   7   8   9   10
1   1   1   1   1   1   1   1   1   1   1
2   0   1   1   2   2   3   3   4   4   5
5   0   0   0   0   1   1   2   2   3   4  
    1   2   2   3   4   5   6   7   8   10
'''