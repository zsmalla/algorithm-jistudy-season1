import sys

input = sys.stdin.readline

def dp(n):
    if memo[n] != 0:
        return memo[n]
    else:
        memo[n] = dp(n-1) + dp(n-2)
        return memo[n]

n = int(input())
if n < 3:
    print(n)
    exit(0)
memo = [0 for _ in range(n+1)]
memo[1], memo[2] = 1, 2
print(dp(n)%10007)