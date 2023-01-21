import sys

input = sys.stdin.readline

N = int(input().rstrip())

def gcd(a, b):
    while b != 0:
        r = a % b
        a, b = b, r

    return a

trees_location = [int(input().rstrip()) for _ in range(N)]
gap = [trees_location[i+1]-trees_location[i] for i in range(N-1)]
final_gcd = min(gap)
answer = 0

for idx in range(1, len(gap)):
    final_gcd = gcd(gap[idx], final_gcd)

for g in gap:
    answer += g//final_gcd-1

print(answer)