import sys

input = sys.stdin.readline

array = [list(map(int, input().rstrip().split())) for _ in range(9)]
blank_idxs = [(r, c) for r in range(9) for c in range(9) if array[r][c] == 0]

def row_check(row, col):
    for i in range(9):
        if i != col and array[row][i] == array[row][col]:
            return False
    return True

def col_check(row, col):
    for i in range(9):
        if i != row and array[i][col] == array[row][col]:
            return False
    return True

def sector_check(row, col):
    for i in range((3 * (row//3)), (3 * (row//3) + 3)):
        for j in range((3 * (col//3)), (3 * (col//3) + 3)):
            if not (i == row and j == col) and array[i][j] == array[row][col]:
                return False
    return True

def premise(row, col):
    return True if row_check(row, col) and col_check(row, col) and sector_check(row, col) else False

def dfs(blank_idx):
    if blank_idx == len(blank_idxs):
        for r in range(9):
            print(*array[r])
        exit(0)

    row, col = blank_idxs[blank_idx]

    for i in range(1, 10):
        array[row][col] = i # 문제 : 9까지 못넣으면 그대로 들어감
        if premise(row, col):
            dfs(blank_idx + 1)
    array[row][col] = 0

dfs(0)
'''
0 0 0 0 0 0 0 0 9
0 0 0 0 0 0 0 0 8
0 0 0 0 0 0 0 0 7
0 0 0 0 0 0 0 0 6
0 0 0 0 0 0 0 0 5
0 0 0 0 0 0 0 0 4
0 0 0 0 0 0 0 0 3
0 0 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0 1

0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
1 2 3 4 5 6 7 8 9

1 2 3 0 0 0 0 0 0
4 5 6 0 0 0 0 0 0
7 8 9 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0

6 0 0 4 1 0 0 0 0
0 2 0 0 6 3 0 0 1
0 0 9 8 0 0 0 0 4
9 0 8 0 7 6 1 0 2
2 6 0 0 0 0 0 9 3
4 0 1 2 9 0 7 0 6
1 0 0 0 0 5 3 0 0
5 0 0 6 3 0 0 7 0
0 0 0 0 4 2 0 0 5

시간초과 예제
0 0 0 0 4 3 0 0 0
0 0 0 0 0 0 1 0 0
0 0 0 0 5 0 0 0 0
0 8 0 7 0 0 0 2 0
0 6 0 0 0 0 0 0 3
0 0 0 0 0 0 0 4 0
0 0 5 8 0 0 6 0 0
4 0 0 1 0 0 0 0 0
3 0 0 0 0 0 5 0 0
'''