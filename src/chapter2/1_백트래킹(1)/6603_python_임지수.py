'''
combinations를 활용한 풀이

import sys
from itertools import combinations

input = sys.stdin.readline

while True:
    ary = list(map(int, input().rstrip().split()))
    if ary[0] == 0 : break

    k, nums = ary[0], ary[1:]
    combs = combinations(nums, 6)
    for com in combs:
        print(*list(com))
    print()

'''

import sys

input = sys.stdin.readline

def dfs(idx, nums, visited, answers):
    if len(answers) == 6:
        print(*answers)
        return

    for i in range(idx, len(nums)):
        if not visited[i]:
            visited[i] = True
            answers.append(nums[i])
            dfs(i, nums, visited, answers)

            answers.pop()
            visited[i] = False


while True:
    ary = list(map(int, input().rstrip().split()))
    if ary[0] == 0 : break
    k, nums = ary[0], ary[1:]
    visited = [False for _ in range(len(nums))]
    answers = []
    dfs(0, nums, visited, answers)
    print()
