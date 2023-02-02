import sys
from collections import deque
from math import sqrt, ceil
input = sys.stdin.readline

'''
최대 K번 내려서 갈 수 있을 때 최소 연료통의 크기
=> 최대 K번 경유할 때 최소 거리
=> 최소 연료통을 L로 할 때 K번 내려서 S -> T 도착이 가능할지
'''

n, k = map(int, input().rstrip().split())
locations = [tuple(map(int, input().rstrip().split())) for _ in range(n)] + [(10000, 10000)]

def get_need_fuel(p1:tuple, p2:tuple):
    l2_norm = sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
    return ceil(l2_norm/10)

def search(fuel):
    queue = deque([(0, 0, 0)])

    while queue:
        x, y, cnt = queue.popleft()

        if x == 10000 and y == 10000 and cnt <= k+1:
            return True

        for idx in range(n+1):
            if not visited[idx] and get_need_fuel((x, y), locations[idx]) <= fuel:
                queue.append((locations[idx][0], locations[idx][1], cnt+1))
                visited[idx] = True
    return False

low, high = 1, get_need_fuel((0,0),(10000,10000))
while low <= high:
    mid = (low+high)//2
    visited = [False for _ in range(n+1)]
    if search(mid):
        high = mid-1
    else:
        low = mid+1

print(low)