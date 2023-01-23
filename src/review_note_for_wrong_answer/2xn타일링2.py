import sys

input = sys.stdin.readline

n = int(input().rstrip())
dp = [0, 1, 3]
if n < 3:
    print(dp[n])
else:
    for i in range(3, n+1):
        dp.append(2*dp[i-2]+dp[i-1])
    print(dp[-1]%10007)
'''
n = 1 -> 1
n = 2 -> 3
n = 3 -> 2*(n(1)) + 1*(n(2))
'''