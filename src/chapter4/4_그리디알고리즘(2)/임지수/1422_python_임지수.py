import sys
from functools import cmp_to_key

input = sys.stdin.readline

def cmp(x : int, y : int):
    if int(str(x)+str(y)) > int(str(y)+str(x)):
        return -1
    else:
        return 1

K, N = map(int, input().rstrip().split())
num_list = [int(input().rstrip()) for _ in range(K)]
max_value = max(num_list)
for _ in range(K, N):
    num_list.append(max_value)
num_list.sort(key = cmp_to_key(cmp))

print(*num_list, sep='')
