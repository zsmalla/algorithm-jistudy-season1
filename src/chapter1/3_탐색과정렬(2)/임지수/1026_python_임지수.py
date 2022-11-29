import sys

input = sys.stdin.readline

N = int(input())
A = sorted(list(map(int, input().rstrip().split())))
B = sorted(list(map(int, input().rstrip().split())), reverse=True)
S = 0

for a, b in zip(A, B):
    S += a*b

print(S)
