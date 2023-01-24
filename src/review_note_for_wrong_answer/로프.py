import sys

# input
input = sys.stdin.readline

N = int(input().rstrip())
ropes = [int(input().rstrip()) for _ in range(N)]
# ---
ropes.sort(reverse = True)
selected_ropes = []
_max = 0
for rope in ropes:
    selected_ropes.append(rope)
    _max = max(rope*len(selected_ropes), _max)
print(_max)
