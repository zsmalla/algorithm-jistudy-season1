import sys

input = sys.stdin.readline

X = int(input())
dp = [0 for _ in range(X+1)]

for idx in range(2, X+1):
    if idx%6 == 0:
        dp[idx] = min(dp[idx-1]+1, dp[idx//3]+1, dp[idx//2]+1)
    elif idx%3 == 0:
        dp[idx] = min(dp[idx-1]+1, dp[idx//3]+1)
    elif idx%2 == 0:
        dp[idx] = min(dp[idx-1]+1, dp[idx//2]+1)
    else:
        dp[idx] = dp[idx-1]+1

''' 죄적화
for idx in range(2, X+1):
	dp[idx] = dp[idx-1]+1
	if idx%3 == 0:
		dp[idx] = min(dp[idx], dp[idx//3]+1)
    if idx%2 == 0:
        dp[idx] = min(dp[idx], dp[idx//2]+1)
'''
print(dp[X])