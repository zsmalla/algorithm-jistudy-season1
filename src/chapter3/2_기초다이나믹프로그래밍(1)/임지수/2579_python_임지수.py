import sys

input = sys.stdin.readline

N = int(input())
stairs = [int(input()) for _ in range(N)]
dp = [-1 for _ in range(N)]

try:
    dp[0] = stairs[0]
    dp[1] = max(stairs[0]+stairs[1], stairs[1])
    dp[2] = max(stairs[0]+stairs[2], stairs[1]+stairs[2])

    for i in range(3, N):
        dp[i] = max(dp[i-2]+stairs[i], dp[i-3]+stairs[i-1]+stairs[i])

except IndexError:      # N < 3일 경우 예외 처리
    pass

finally:
    print(dp[-1])