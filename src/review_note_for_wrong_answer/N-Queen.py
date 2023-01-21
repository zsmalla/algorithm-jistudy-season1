# 퀸 : 가로, 세로, 대각선 공격 가능

import sys

input = sys.stdin.readline

def can_NQ(row):
    for i in range(row):
        if abs(row - i) == abs(queens[row] - queens[i]) or queens[i] == queens[row]:
            return False
    return True

def dfs(row):
    global answer

    if row == N:
        answer += 1
        return

    for i in range(N):
        queens[row] = i
        if can_NQ(row):
            dfs(row+1)

N = int(input())
answer = 0
queens = [0 for _ in range(N)]
dfs(0)

print(answer)