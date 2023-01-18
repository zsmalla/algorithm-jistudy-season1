from collections import deque

def get_diff(x, other):
    count = 0
    for i in range(len(x)):
        if x[i] != other[i]:
            count += 1
    return count

def solution(begin, target, words):
    n = len(words)
    visited = [False for _ in range(n)]
    queue = deque([(begin, 0)])

    while queue:
        x, cnt = queue.popleft()
        if x == target:
            return cnt

        for idx in range(n):
            if not visited[idx] and get_diff(x, words[idx]) == 1:
                queue.append((words[idx], cnt + 1))
                visited[idx] = True
    return 0
