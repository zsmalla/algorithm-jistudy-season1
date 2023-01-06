import sys

input = sys.stdin.readline

N, C = map(int, input().rstrip().split())
houses = sorted([int(input()) for _ in range(N)])

def can_set_more(term):
    before = houses[0]
    count = 1
    for i in range(1, N):
        if houses[i]-before >= term:
            count += 1
            before = houses[i]
    if count >= C:
        return True

def setting(low, high):
    while low <= high:
        mid = (low+high)//2
        if can_set_more(mid):
            low = mid+1
        else:
            high = mid-1
    return high

print(setting(1, houses[-1]-houses[0]))
