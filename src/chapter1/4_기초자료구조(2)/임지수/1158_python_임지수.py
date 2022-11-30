import sys

input = sys.stdin.readline

from collections import deque

N, K = map(int, input().rstrip().split())
ary = deque(range(1, N+1))

print('<', end='')
for _ in range(N-1):
    ary.rotate(-(K-1))
    print(ary.popleft(), end=', ')
print(ary.popleft(), end='>')