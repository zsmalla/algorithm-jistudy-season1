import sys

input = sys.stdin.readline

def check(tmp, i):
    if i < 2:
        return True
    if operators[i-2] == '<':
        if tmp[i-2] < tmp[i-1]:
            return True
    else:
        if tmp[i-2] > tmp[i-1]:
            return True
    return False

def dfs(result):
    i = len(result)

    if not check(result, i):
        return

    if i == k+1:
        results.append(result)
        return

    for num in numbers:
        if not visited[int(num)]:
            visited[int(num)] = True
            dfs(result+num)
            visited[int(num)] = False

numbers = list('0123456789')

k = int(input())
operators = input().rstrip().split()
result = ''
results = []
visited = [False for _ in range(10)]

for num in numbers:
    visited[int(num)] = True
    dfs(result+num)
    visited[int(num)] = False

print(results[-1], results[0])

