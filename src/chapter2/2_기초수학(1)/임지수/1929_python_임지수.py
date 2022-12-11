import sys

input = sys.stdin.readline

m, n = map(int, input().rstrip().split())
array = [False, False] + [True for _ in range(2, n+1)]

for i in range(2, int(n**0.5)+1):
    if array[i]:
        j = 2
        while i*j <= n:
            array[i*j] = False
            j += 1

prime_in_range = [i for i, j in enumerate(array) if i >= m and j]
for prime in prime_in_range:
    print(prime)
