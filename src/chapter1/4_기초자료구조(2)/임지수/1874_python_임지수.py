import sys

input = sys.stdin.readline

from collections import deque

N = int(input())
ary = deque(range(1, N+1))
stack = deque()
operators = []

for _ in range(N):
    num = int(input())
    while ary and ary[0] <= num:
        stack.appendleft(ary.popleft())
        operators.append('+')
    if stack[0] == num:
        stack.popleft()
        operators.append('-')
    else:
        operators = ['NO']
        break
for operator in operators:
    print(operator)

