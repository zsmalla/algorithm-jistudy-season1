import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
ary = list(map(int, input().rstrip().split()))
M = int(input())
condition = list(map(int, input().rstrip().split()))

counter_dict = Counter(ary)

for num in condition:
    print(counter_dict[num], end=' ')