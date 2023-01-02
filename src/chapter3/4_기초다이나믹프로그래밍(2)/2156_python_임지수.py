import sys

input = sys.stdin.readline

n = int(input())
p = [0]+[int(input()) for _ in range(1, n+1)]
dp = [0]

if n >= 1:
    dp.append(p[1])
if n >= 2:
    dp.append(p[1]+p[2])
if n >= 3:
    dp.append(max(p[1]+p[2], p[2]+p[3], p[1]+p[3]))

for i in range(4, n+1):
    dp.append(max(dp[i-3]+p[i-1]+p[i], dp[i-2]+p[i], dp[i-1]))

print(dp[n])