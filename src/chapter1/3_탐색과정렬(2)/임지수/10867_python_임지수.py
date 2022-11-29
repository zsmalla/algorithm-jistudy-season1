import sys

input = sys.stdin.readline

N = int(input())

ary = sorted(set(map(int, input().rstrip().split())))
print(*ary)