import sys
sys.setrecursionlimit(10**8)

input = sys.stdin.readline

'''
hint
이 문제의 경우 시작, 도착점이 아닌 임의의 지점(a,b)에서 도착지점 (m-1, n-1) 까지 가는 경우의 수가 구해지면, 
그 이전의 어떤 경로로 (a,b)에 도착하기만 하면 그 때부터의 경우의 수는 다시 구할 필요가 없습니다.
다시 말해서, 도착 지점까지 가는 경우의 수는 도착 지점이 아닌 임의의 점들에서 도착지점까지 가는 경우의 수를 합한 것과 같아진다는 것이죠.

시작 지점에서 출발해서 DP 테이블이 갱신되지 않은 곳(X)을 만난다면, 해당 지점(X)부터 도착 지점까지 갈 수 있는 경로의 수를 그곳에 업데이트 합니다.
X지점의 DP 테이블이 이미 갱신되어 있다면 그 곳이 위에서 말한 부분 최적해가 되므로 그 값을 그대로 전체 정답에 더해주면 됩니다.
'''

def dfs(y, x):
    if y == M-1 and x == N-1:
        return 1

    if dp[y][x] != -1:
        return dp[y][x]

    ways = 0

    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if 0 <= ny < M and 0 <= nx < N and MAP[y][x] > MAP[ny][nx]:
            ways += dfs(ny, nx)

    dp[y][x] = ways

    return dp[y][x]

M, N = map(int, input().rstrip().split())   # M : 세로, N : 가로
MAP = [list(map(int, input().rstrip().split())) for _ in range(M)]
dp = [[-1 for _ in range(N)] for _ in range(M)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

print(dfs(0, 0))
for i in range(len(dp)):
    print(*dp[i], sep = ' | ')
