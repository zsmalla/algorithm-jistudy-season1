import sys
input = sys.stdin.readline

from collections import deque

num_of_testcase = int(input())
for _ in range(num_of_testcase):
    N, M = map(int, input().rstrip().split())
    docs = deque(map(int, input().rstrip().split()))
    maxPriority = max(docs)
    count = 1

    while True:
        if docs[0] >= maxPriority:
            if M == 0:
                break
            else:
                docs.popleft()
                count += 1
                M = (M+len(docs)-1)%len(docs)
                maxPriority = max(docs)
        else:
            docs.rotate(-1)
            M = (M + len(docs) - 1) % len(docs)

    print(count)