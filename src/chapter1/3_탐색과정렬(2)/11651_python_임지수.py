import sys

input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    lst.append(tuple(map(int, input().split())))
for x, y in sorted(lst, key=lambda t : (t[1], t[0])):
    print(x, y)