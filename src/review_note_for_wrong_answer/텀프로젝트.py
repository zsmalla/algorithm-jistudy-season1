import sys
sys.setrecursionlimit(111111)
input = sys.stdin.readline

def dfs(idx):
    global result
    visited[idx] = True
    team.append(idx)

    for num, t in enumerate(team):
        if t == choices[idx]:
            result += (len(team)-num)
            return

    if not visited[choices[idx]]:
        dfs(choices[idx])

T = int(input().rstrip())

for _ in range(T):
    n = int(input().rstrip())
    choices = list(map(lambda x : int(x)-1, input().rstrip().split()))
    visited = [False for _ in range(n)]
    result = 0
    for i in range(n):
        if not visited[i]:
            team = []
            dfs(i)

    print(n-result)