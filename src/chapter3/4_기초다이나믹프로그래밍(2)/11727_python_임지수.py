import sys

input = sys.stdin.readline

def tabulation(n):
    if dp[n] > 0:
        return dp[n]
    else:
        dp[n] = 2 * tabulation(n-2) + tabulation(n-1)
        return dp[n]

n = int(input())

dp = [0, 1, 3] + [0 for _ in range(2, n+1)] if n > 2 else [0, 1, 3]
print(tabulation(n)%10007)