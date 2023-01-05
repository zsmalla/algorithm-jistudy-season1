import sys

input = sys.stdin.readline

def is_goal_during(n):
    return ((A-B)*(n-1)+A) >= V

def get_due(low, high):
    while low <= high:
        mid = (low+high) // 2
        if is_goal_during(mid):
            high = mid - 1
        else:
            low = mid + 1
    return low

A, B, V = map(int, input().rstrip().split())
print(get_due(1, V))
