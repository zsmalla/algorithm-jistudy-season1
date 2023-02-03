import sys

input = sys.stdin.readline

def can_check(time):
    return sum([time//t for t in lst]) >= M

N, M = map(int, input().rstrip().split())
lst = [int(input().rstrip()) for _ in range(N)]

low, high = 1, int(1e18)

while low <= high:
    mid = (low+high)//2
    if can_check(mid):
        high = mid-1
    else:
        low = mid+1

print(low)