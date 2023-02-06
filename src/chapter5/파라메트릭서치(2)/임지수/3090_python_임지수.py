import sys
from copy import deepcopy

input = sys.stdin.readline

N, T = map(int, input().rstrip().split())
A = list(map(int, input().rstrip().split()))

def can_make_nums(diff, nums, n_ops):
    for i in range(N-1):
        gap = nums[i+1]-nums[i]
        if gap > diff:
           nums[i+1] -= (gap-diff)
           n_ops -= (gap-diff)
        if n_ops < 0 : return False

    for i in range(N-1, 0, -1):
        gap = nums[i-1] - nums[i]
        if gap > diff:
            nums[i-1] -= (gap-diff)
            n_ops -= (gap-diff)
        if n_ops < 0 : return False

    return nums

low, high = 0, 1000000000
while low <= high:
    mid = (low+high)//2
    after_A = can_make_nums(mid, deepcopy(A), T)
    if after_A:
        high = mid-1
    else:
        low = mid+1

print(*can_make_nums(low, deepcopy(A), T))
