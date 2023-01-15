from collections import defaultdict, deque


def bfs(start, visited, wire_dict, n):
    queue = deque([start])
    visited[start] = True
    count = 1
    while queue:
        x = queue.popleft()
        for nx in wire_dict[x]:
            if not visited[nx]:
                queue.append(nx)
                visited[nx] = True
                count += 1
    return count


def solution(n, wires):
    answers = []
    for remove_idx in range(len(wires)):
        wire_dict = defaultdict(list)
        num_of_cloud = []

        for idx in range(len(wires)):
            if idx == remove_idx:
                continue
            fr, to = wires[idx]
            wire_dict[fr - 1].append(to - 1)
            wire_dict[to - 1].append(fr - 1)

        visited = [False for _ in range(n)]
        for i in range(n):
            if not visited[i]:
                num_of_cloud.append(bfs(i, visited, wire_dict, n))
        answers.append(abs(num_of_cloud[1] - num_of_cloud[0]))
    return min(answers)