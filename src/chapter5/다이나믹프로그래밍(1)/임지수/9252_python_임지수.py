import sys

input = sys.stdin.readline

str1, str2 = input().rstrip(), input().rstrip()
# str1 : ACAYKP
# str2 : CAPCAK
n1, n2 = len(str1), len(str2)

dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]

for i in range(1, n1+1):
    for j in range(1, n2+1):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])

if dp[i][j]:
    LCS = ''

    while dp[i][j]:
        if str1[i-1] == str2[j-1]:
            LCS += str1[i-1]
            i, j = i-1, j-1
        else:
            if dp[i-1][j] < dp[i][j-1]:
                j -= 1
            else:
                i -= 1

    print(LCS[::-1])
