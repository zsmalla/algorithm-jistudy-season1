'''
import sys
input = sys.stdin.readline

from itertools import combinations

N, S = map(int, input().rstrip().split())
nums = list(map(int, input().rstrip().split()))
count = 0

for i in range(1, N+1):
    comb = combinations(nums, i)
    for p in comb:
        if sum(p) == S:
            count += 1

print(count)
'''


import sys
input = sys.stdin.readline

count = 0
N, S = map(int, input().rstrip().split())
nums = list(map(int, input().rstrip().split()))
visited = [False for _ in range(N)]

def dfs(sequence, sequence_size, idx, visited):
    global count

    if len(sequence) == sequence_size:
        if sum(sequence) == S:
            count += 1
        return

    for i in range(idx, len(nums)):
        if not visited[i]:
            visited[i] = True
            sequence.append(nums[i])
            dfs(sequence, sequence_size, i, visited)

            sequence.pop()
            visited[i] = False

for SEQUENCE_SIZE in range(1, N+1):
    dfs([], SEQUENCE_SIZE, 0, visited)

print(count)


'''
import sys
input = sys.stdin.readline

count = 0
N, S = map(int, input().rstrip().split())
nums = list(map(int, input().rstrip().split()))

def back_tracking(idx, res):
    global count

    if idx >= N:
        return

    res += nums[idx]

    if res == S:
        count += 1

    back_tracking(idx+1, res)
    back_tracking(idx+1, res-nums[idx])

back_tracking(0, 0)
print(count)
'''