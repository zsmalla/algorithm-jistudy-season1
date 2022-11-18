import sys

input = sys.stdin.readline

def binary_search(arr, target):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            high = mid-1
        else:
            low = mid+1
    return False

N = int(input())
arr = sorted(list(map(int, input().split())))
M = int(input())
targets = map(int, input().split())

for target in targets:
    print(1) if binary_search(arr, target) else print(0)