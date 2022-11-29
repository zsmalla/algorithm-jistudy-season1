import sys

input = sys.stdin.readline
lst = []

N = int(input())
for _ in range(N):
    d = input().rstrip()
    if d not in lst:
        lst.append(d)
lst.sort(key = lambda x : (len(x), x))

for x in lst:
    print(x)
