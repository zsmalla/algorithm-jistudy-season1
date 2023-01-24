import sys

input = sys.stdin.readline

N, C = map(int, input().rstrip().split())
points = sorted([int(input().rstrip()) for _ in range(N)])

def can(D):
    cnt = 1
    last = 0
    for i in range(1, N):
        if points[i]-points[last] >= D:
            cnt += 1
            last = i
    return cnt >= C

low, high = 1, points[-1]-points[0]
while low <= high:
    mid = (low+high)//2
    if can(mid):
        low = mid+1
    else:
        high = mid-1
print(high)
