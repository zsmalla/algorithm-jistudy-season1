import sys

input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    lst.append(tuple(map(int, input().split())))
for x, y in sorted(lst, key=lambda t : (t[0], t[1])):
    print(x, y)