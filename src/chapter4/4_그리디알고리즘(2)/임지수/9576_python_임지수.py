import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().rstrip().split())
    scopes = sorted([list(map(int, input().rstrip().split())) for _ in range(M)], key = lambda x : x[1])
    visited = [False for _ in range(N+1)]
    count = 0
    for a, b in scopes:
        for i in range(a, b+1):
            if not visited[i]:
                visited[i] = True
                count += 1
                break

    print(count)