import sys

input = sys.stdin.readline

def get_chicken_distance(chicken_points):
    result = 0
    for house in housePoints:
        middle_distance = 1e9
        for chicken in chicken_points:
            middle_distance = min(middle_distance, abs(house[0]-chicken[0])+abs(house[1]-chicken[1]))
        result += middle_distance
    return result

def dfs(idx, chicken_stores):
    if len(chicken_stores) == M:
        distances.append(get_chicken_distance(chicken_stores))
        return

    for i in range(idx, num_of_chickenstore):
        chicken_stores.append(chickenPoints[i])
        dfs(i+1, chicken_stores)
        chicken_stores.pop()

N, M = map(int, input().split())
array = [list(map(int, input().rstrip().split())) for _ in range(N)]
housePoints = []
chickenPoints = []
distances = []

for r in range(N):
    for c in range(N):
        if array[r][c] == 1:
            housePoints.append((r, c))
        elif array[r][c] == 2:
            chickenPoints.append((r, c))

num_of_chickenstore = len(chickenPoints)
dfs(0, [])
print(min(distances))