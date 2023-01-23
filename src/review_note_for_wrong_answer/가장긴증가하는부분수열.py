import sys

input = sys.stdin.readline

N = int(input().rstrip())
numbers = list(map(int, input().rstrip().split()))

dp = [1 for _ in range(N)]
for i in range(N):
    for j in range(i):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[j]+1, dp[i])
print(max(dp))

'''
23 24 25 1 2 3 4 5 6 7 26
'''