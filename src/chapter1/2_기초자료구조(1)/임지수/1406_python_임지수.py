import sys
input = sys.stdin.readline

from collections import deque

left = deque(input().rstrip())
right = deque()

for _ in range(int(input())):
    command = input().split()
    if command[0] == 'L':
        if left:
            right.appendleft(left.pop())
    elif command[0] == 'D':
        if right:
            left.append(right.popleft())
    elif command[0] == 'B':
        if left:
            left.pop()
    else:
        left.append(command[1])

left.extend(right)
print(''.join(left))