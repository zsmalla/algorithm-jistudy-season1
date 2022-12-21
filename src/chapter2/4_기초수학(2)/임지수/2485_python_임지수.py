import sys

input = sys.stdin.readline

def gcd(a, b):
    while b != 0:
        r = a % b
        a, b = b, r
    return a

N = int(input())
trees = []
diffs = []
count = 0

for _ in range(N):
    tree = int(input())
    trees.append(tree)

for i in range(len(trees)-1):
    diffs.append(trees[i+1] - trees[i])

diffs.sort()
final_gcd = diffs[0]

for idx in range(1, len(diffs)):
    final_gcd = gcd(final_gcd, diffs[idx])

for diff in diffs:
    count += diff//final_gcd -1

print(count)
