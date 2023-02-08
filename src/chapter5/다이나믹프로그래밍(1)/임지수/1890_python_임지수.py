import sys

input = sys.stdin.readline

N = int(input())
MAP = [list(map(int, input().rstrip().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = 1

for r in range(N):
    for c in range(N):
        step = MAP[r][c]
        if not step:
            continue
        if 0 <= r+step < N:
            dp[r+step][c] += dp[r][c]
        if 0 <= c+step < N:
            dp[r][c+step] += dp[r][c]

print(dp[N-1][N-1])

'''
9
3 1 2 2 3 3 1 1 2
1 1 2 1 1 2 3 1 2
2 1 1 3 2 2 1 3 1
3 3 1 1 1 3 1 2 1
3 2 2 2 1 1 3 3 1
3 1 3 2 2 3 1 3 3
3 1 1 2 1 1 1 1 1
2 3 1 3 1 3 2 2 2
3 3 3 2 3 1 3 3 0

4
1 2 2 3
1 1 3 3
3 1 1 3
3 2 1 0
'''