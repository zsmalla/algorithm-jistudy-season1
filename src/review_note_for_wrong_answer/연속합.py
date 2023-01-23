import sys

input = sys.stdin.readline

n = int(input().rstrip())
numbers = list(map(int, input().rstrip().split()))
dp = [0 for _ in range(n)]
dp[0] = numbers[0]
for i in range(1, n):
    dp[i] = max(dp[i-1]+numbers[i], numbers[i])

print(max(dp))
