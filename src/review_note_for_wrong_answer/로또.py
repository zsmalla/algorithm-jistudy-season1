import sys

input = sys.stdin.readline

def dfs(select, idx):
    if len(select) == 6:
        answer.append(select)
        return

    if idx == k:
        return

    for i in range(idx, k):
        visited[i] = True
        dfs(select + [numbers[i]], i+1)
        visited[i] = False


while True:
    case = list(map(int, input().rstrip().split()))

    if not case[0]:
        break

    k, numbers = case[0], case[1:]
    answer = []
    visited = [False for _ in range(k)]

    dfs([], 0)

    for comb in answer:
        print(*comb)

    print()