import sys

input = sys.stdin.readline

N = int(input().rstrip())

def hanoi(n, start, to, via):
    if n == 1:
        print(start, to)
    else:
        hanoi(n-1, start, via, to)
        print(start, to)
        hanoi(n-1, via, to, start)

print(2**N - 1)
hanoi(N, 1, 3, 2)
