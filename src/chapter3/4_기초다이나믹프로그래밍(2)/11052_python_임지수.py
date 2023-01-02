import sys

input = sys.stdin.readline

N = int(input())
cards = [0]+list(map(int, input().rstrip().split()))
dp = [0, cards[1]]

for i in range(2, N+1):
    tmp = [cards[i]]
    for j in range(1, i):
        tmp.append(dp[i-j]+cards[j])
    dp.append(max(tmp))

print(dp[N])