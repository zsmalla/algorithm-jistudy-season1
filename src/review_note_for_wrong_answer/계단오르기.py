import sys

input = sys.stdin.readline

N = int(input().rstrip())
stairs = [int(input().rstrip()) for _ in range(N)]

if N == 1:
    print(stairs[0])
elif N == 2:
    print(stairs[0]+stairs[1])
else:
    dp = [0 for i in range(N)]
    dp[0], dp[1] = stairs[0], stairs[0]+stairs[1]
    for i in range(2, N):
        dp[i] = max(stairs[i]+stairs[i-1]+dp[i-3], stairs[i]+dp[i-2])
    print(dp[-1])