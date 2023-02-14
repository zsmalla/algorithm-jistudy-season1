import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input().rstrip())
nums = list(map(int, input().rstrip().split()))
dp = []

def change(ary, num):
    '''
    :param ary: dp 배열
    :param num: 대치할 수
    num보다 큰 수 중 최솟값과 대치 (이진탐색 이용)
    :return: None
    '''

    low, high = 0, len(ary)
    while low <= high:
        mid = (low + high) // 2
        if ary[mid] >= num:
            high = mid-1
        else:
            low = mid+1
    ary[low] = num

for i in range(N):
    if not dp or dp[-1] < nums[i]:
        dp.append(nums[i])
    else:
        # change(dp, nums[i])                         # 이진 탐색 직접 구현
        dp[bisect_left(dp, nums[i])] = nums[i]    # bisect 모듈 활용

print(len(dp))