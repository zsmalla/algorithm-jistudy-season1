import sys

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

dp = [[1 for _ in range(n)] for n in range(2, N+2)]

for n in range(1, N):                        
    for k in range(1, n+1):                      
        dp[n][k] = dp[n-1][k-1]+dp[n-1][k]
        

print(dp[N-1][K] % 10007)
