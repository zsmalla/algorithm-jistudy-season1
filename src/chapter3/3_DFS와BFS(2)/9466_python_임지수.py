import sys
from collections import deque
sys.setrecursionlimit(111111) #충분한 재귀 깊이를 주어 오류를 예방

input = sys.stdin.readline

def dfs(start):
    global result
    visited[start] = True
    cycle.append(start)
    choice = choices[start]

    if visited[choice]:
        for idx, st in enumerate(cycle):
            if st == choice:
                result += idx
                return
        result += len(cycle)
        return
    else:
        dfs(choice)

'''
def bfs(start):
    queue = deque([start])
    visited[start] = True
    cycle = [start]
    while queue:
        nxt = queue.popleft()
        choice = choices[nxt]-1

        for idx, t in enumerate(cycle):
            if t == choice:
                return idx

        if not visited[choice]:
            queue.append(choice)
            cycle.append(choice)
            visited[choice] = True
    return len(cycle)
'''

T = int(input())
for _ in range(T):
    n = int(input())
    choices = [0] + list(map(int, input().rstrip().split()))
    visited = [True] + [False for _ in range(n)]
    result = 0
    for start in range(1, n+1):
        if not visited[start]:
            cycle = []
            dfs(start)
    print(result)