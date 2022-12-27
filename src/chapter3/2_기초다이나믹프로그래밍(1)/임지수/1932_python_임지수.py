import sys

input = sys.stdin.readline

n = int(input())
triangle = [list(map(int, input().rstrip().split())) for _ in range(n)]
for row in range(1, n):
    for i in range(len(triangle[row])):
        if i == 0:
            triangle[row][i] += triangle[row-1][i]
        elif i == len(triangle[row])-1:
            triangle[row][i] += triangle[row-1][i-1]
        else:
            triangle[row][i] += max(triangle[row-1][i-1], triangle[row-1][i])
print(max(triangle[-1]))