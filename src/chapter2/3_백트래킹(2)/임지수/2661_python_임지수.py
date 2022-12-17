import sys

input = sys.stdin.readline

N = int(input())

def new_judge(st):      # 좋은 수열 판단 코드 참고
    for i in range(1, len(st)//2+1):
        if st[-i:] == st[-2*i:-i]:
            return False
    return True


def dfs(st):
    if not new_judge(st):
        return -1

    if len(st) == N:
        print(st)
        return 0

    for s in range(1, 4):
        st += str(s)
        if dfs(st) == 0:
            return 0
        st = st[:-1]

dfs('')