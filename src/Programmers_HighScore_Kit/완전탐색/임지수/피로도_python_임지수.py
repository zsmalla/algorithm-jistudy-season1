from itertools import permutations
from collections import deque

def solution(k, dungeons):      # solution using permutation
    permu = permutations(dungeons, len(dungeons))
    answer = 0
    for case in permu:
        queue = deque(case)
        HP = k
        count = 0
        while queue and HP >= queue[0][0]:
            dungeon = queue.popleft()
            HP -= dungeon[1]
            count += 1
        answer = max(answer, count)

    return answer

visited = []
answer = 0

def dfs(HP, dungeons, count):
    global answer

    if answer < count:
        answer = count

    for i in range(len(dungeons)):
        if not visited[i] and dungeons[i][0] <= HP:
            visited[i] = True
            dfs(HP - dungeons[i][1], dungeons, count + 1)
            visited[i] = False

def solution1(k, dungeons):     # solution using backtracking
    global answer, visited

    visited = [False for _ in range(len(dungeons))]
    dfs(k, dungeons, 0)

    return answer
