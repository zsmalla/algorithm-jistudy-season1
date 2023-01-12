from collections import deque

def solution(s):
    stack = deque()
    for bracket in s:
        if bracket == '(':
            stack.append(bracket)
        else:
            if not stack:
                return False
            else:
                stack.pop()
    return True if not stack else False