import sys

input = sys.stdin.readline

N = int(input())
divisors = sorted(list(map(int, input().rstrip().split())))
print(divisors[0]*divisors[-1])
