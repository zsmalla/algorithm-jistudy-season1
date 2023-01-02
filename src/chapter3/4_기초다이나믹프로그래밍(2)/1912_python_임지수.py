import sys

input = sys.stdin.readline

n = int(input())
numList = list(map(int, input().rstrip().split()))

for i in range(1, n):
    numList[i] = max(numList[i], numList[i-1]+numList[i])

print(max(numList))