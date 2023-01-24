import sys

T = int(input().rstrip())
for _ in range(T):
    N, M = map(int, input().rstrip().split())
    books = [True] + [False for _ in range(1, N+1)]
    ranges = sorted([list(map(int, input().rstrip().split())) for _ in range(M)],\
                    key = lambda x : x[1])
    cnt = 0

    for start, end in ranges:
        for i in range(start, end+1):
            if not books[i]:
                cnt += 1
                books[i] = True
                break
    print(cnt)

'''
1
3 3
2 3
2 2
2 3
3
'''