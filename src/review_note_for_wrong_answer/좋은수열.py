import sys

input = sys.stdin.readline

def good_nums(nums):
    if len(nums) < 2:
        return True

    for i in range(1, len(nums)//2+1):
        if nums[-i:] == nums[-2*i:-i]:
            return False

    return True

def dfs(idx, nums):

    if not good_nums(nums):
        return

    if idx == N-1:
        print(nums)
        exit(0)

    for i in range(1, 4):
        dfs(idx+1, nums+str(i))

N = int(input().rstrip())
dfs(-1, '')