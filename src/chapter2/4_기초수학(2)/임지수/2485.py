import sys

input = sys.stdin.readline

N = int(input())
trees = []
results = 1e9
diff = 1e9

for _ in range(N):
    tree = int(input())
    trees.append(tree)

for i in range(len(trees)-1):
    diff = min(diff, trees[i+1] - trees[i])

location = [0 for _ in range(trees[-1]+1)]

for l in trees:
    location[l] = 1

for d in range(diff, 1, -1):
    count = 0
    for l in range(1, trees[-1]+1, diff):
        if location[l] == 0:
            count += 1
    results = min(results, count)

print(results)