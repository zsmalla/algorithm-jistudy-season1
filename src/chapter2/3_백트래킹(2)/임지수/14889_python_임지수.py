
''' 풀이 1 : combinations와 반복문을 이용한 풀이
import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())
ability = [list(map(int, input().rstrip().split())) for _ in range(N)]
members = set(range(1, N+1))
team1s = combinations(members, N//2)
ability_diffs = []
for team1 in team1s:
    team2 = set(members)-set(team1)
    team1s_ability = 0
    team2s_ability = 0
    for m1, m2 in combinations(team1, 2):
        team1s_ability += ability[m1-1][m2-1]
        team1s_ability += ability[m2-1][m1-1]
    for m1, m2 in combinations(team2, 2):
        team2s_ability += ability[m1-1][m2-1]
        team2s_ability += ability[m2-1][m1-1]
    ability_diffs.append(abs(team1s_ability-team2s_ability))
print(min(ability_diffs))
'''
# 풀이 2 : DFS와 Back-Tracking을 활용한 풀이
import sys
from itertools import combinations

input = sys.stdin.readline

def dfs(idx, team1):
    global ability_diff

    if len(team1) == N//2:
        team2 = set(members) - set(team1)
        team1s_ability = 0
        team2s_ability = 0
        for m1, m2 in combinations(team1, 2):
            team1s_ability += ability[m1][m2]
            team1s_ability += ability[m2][m1]
        for m1, m2 in combinations(team2, 2):
            team2s_ability += ability[m1][m2]
            team2s_ability += ability[m2][m1]
        ability_diff = min(ability_diff, abs(team1s_ability-team2s_ability))
        return

    for i in range(idx, N):
        team1.append(i)
        dfs(i, team1)
        team1.pop()

N = int(input())
ability = [list(map(int, input().rstrip().split())) for _ in range(N)]
members = list(range(N))
ability_diff = int(1e9)
dfs(0, [])
print(ability_diff)