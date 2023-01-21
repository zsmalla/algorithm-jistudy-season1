from collections import deque
import sys

input = sys.stdin.readline

string = input().rstrip()
M = int(input())
operations = [input().rstrip().split() for _ in range(M)]

def solution(string, operations):
    cursor_left, cursor_right = deque(string), deque()

    for operation in operations:
        if operation[0] == 'L':
            if cursor_left:
                cursor_right.appendleft(cursor_left.pop())
        elif operation[0] == 'D':
            if cursor_right:
                cursor_left.append(cursor_right.popleft())
        elif operation[0] == 'B':
            if cursor_left:
                cursor_left.pop()
        else:
            cursor_left.append(operation[1])

    print(''.join(cursor_left)+''.join(cursor_right))

solution(string, operations)