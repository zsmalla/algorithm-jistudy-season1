import sys

input = sys.stdin.readline

def cut_tree(n):
    result = 0
    for tree in trees:
        if tree > n:
            result += tree-n

    return result

def get_minimal_height(low, high):
    while low <= high:
        mid = (low + high) // 2
        cuttedTree = cut_tree(mid)
        if cuttedTree < M:
            high = mid-1
        else:
            low = mid+1
    return high


N, M = map(int, input().rstrip().split())
trees = list(map(int, input().rstrip().split()))
print(get_minimal_height(0, max(trees)))