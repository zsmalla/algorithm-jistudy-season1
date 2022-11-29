import sys

input = sys.stdin.readline

from collections import deque

N = int(input())
for _ in range(N):
    stack = deque()
    fail_flag = False
    PSs = list(input().rstrip())
    for PS in PSs:                  # 열림 괄호 : insert / 닫힘 괄호 : 스택 pop
        if PS == '(':
            stack.append('(')
        else:
            if not stack:           # 스택이 빈 상태에서 닫힘 괄호 -> no VPS
                fail_flag=True
                break
            else:
                stack.pop()
    print('YES') if not stack and not fail_flag else print('NO')    # 모든 연산 후 스택에 남아있는 경우 -> no VPS