import sys

input = sys.stdin.readline

def binary_search(lst, target):
    low, high = 0, len(lst)-1
    while low <= high:
        mid = (low+high)//2
        if lst[mid] == target:
            return True
        elif lst[mid] < target:
            low = mid+1
        else:
            high = mid-1
    return False

N = int(input())
lst = sorted(list(map(int, input().split())))
M = int(input())
cards = list(map(int, input().split()))

for card in cards:
    print(1, end=' ') if binary_search(lst, card) else print(0, end=' ')