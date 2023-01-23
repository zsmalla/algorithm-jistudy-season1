import sys

input = sys.stdin.readline

n = int(input().rstrip())
glasses = [int(input().rstrip()) for _ in range(n)]

dp = [0 for _ in range(n)]
if n >= 1:
    dp[0] = glasses[0]
if n >= 2:
    dp[1] = glasses[0]+glasses[1]
if n >= 3:
    dp[2] = max(dp[1], dp[0]+glasses[2], glasses[1]+glasses[2])
if n >= 4:
    for i in range(3, n):
        dp[i] = max(glasses[i]+glasses[i-1]+dp[i-3],\
                    glasses[i]+dp[i-2],\
                    dp[i-1])
print(max(dp))
