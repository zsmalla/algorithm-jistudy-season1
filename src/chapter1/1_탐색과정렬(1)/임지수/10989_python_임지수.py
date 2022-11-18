import sys

input = sys.stdin.readline

N = int(input())
count = [0] * 10000

for _ in range(N):
    count[int(input())-1] += 1
for i, c in enumerate(count):
    while c > 0:
        print(i+1)
        c-=1