import sys

input = sys.stdin.readline

def is_satisfy(B):
    result = 0
    for request in requests:
        result += request if request <= B else B
    return result <= M

def allocate_budget(low, high):
    while low <= high:
        mid = (low+high) // 2
        if is_satisfy(mid):
            low = mid+1
        else:
            high = mid-1
    return high

N = int(input())        # 3 <= N <= 10,000
requests = list(map(int, input().rstrip().split()))     # 1 <= request <= 100,000
M = int(input())        #  N <= M <= 1,000,000,000

max_requests = max(requests)
can_maximum_allocate = allocate_budget(0, M)
print(max_requests if can_maximum_allocate >= max_requests else can_maximum_allocate)