import sys

input = sys.stdin.readline

N = int(input())

schedule = sorted([list(map(int, input().rstrip().split())) for _ in range(N)], key = lambda x : (x[1], x[0]))
tmp = 0
result = 0

for start, end in schedule:
    if start >= tmp:
        result += 1
        tmp = end

print(result)
