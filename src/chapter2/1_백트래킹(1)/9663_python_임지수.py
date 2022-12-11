import sys

input = sys.stdin.readline

def promise(idx):
    for row in range(idx):
        if board[row] == board[idx] or abs(board[row]-board[idx]) == idx-row:
                return False
    return True

def backtracking(idx):
    global count

    if idx == N:
        count += 1
        return

    for i in range(N):
        board[idx] = i
        if promise(idx):
            backtracking(idx+1)

N = int(input())
count = 0
board = [-1 for _ in range(N)]
backtracking(0)
print(count)
