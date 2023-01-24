import sys
from functools import cmp_to_key

input = sys.stdin.readline

def cmp(x, y):
    if int(str(x)+str(y)) < int(str(y)+str(x)):
        return 1
    else:
        return -1

K, N = map(int, input().rstrip().split())
numbers = [int(input().rstrip()) for _ in range(K)]
numbers += [max(numbers) for _ in range(N-K)]
numbers.sort(key = cmp_to_key(cmp))

print(*numbers, sep='')