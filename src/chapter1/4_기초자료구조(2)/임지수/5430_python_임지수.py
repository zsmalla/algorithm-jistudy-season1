import sys
import re
from collections import deque
input = sys.stdin.readline

num_of_testCase = int(input().rstrip())
for _ in range(num_of_testCase):
    funcs = list(input().rstrip())
    n = int(input().rstrip())
    ary = deque(re.findall('[0-9]+', input().rstrip()))
    reverse = False
    for func in funcs:
        if func == 'R':
            reverse = not reverse
        else:
            if ary:
                ary.popleft() if not reverse else ary.pop()
            else:
                ary = 'error'
                break
    if ary != 'error':
        print('[' + ','.join(ary) + ']') if not reverse else print('['+','.join(reversed(ary))+']')
    else:
        print('error')