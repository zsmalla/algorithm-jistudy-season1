import sys

input = sys.stdin.readline

def can_make_lan_of(n):
    result = 0
    for lan in lans:
        result += lan//n
    return result

def get_maximum_len(low, high):
    while low <= high:
        mid = (low+high)//2
        if can_make_lan_of(mid) >= N:
            low = mid+1
        else:
            high = mid-1
    return high

K, N = map(int, input().rstrip().split())
lans = [int(input()) for _ in range(K)]

print(get_maximum_len(1, max(lans)))
