import sys

input = sys.stdin.readline

N = int(input())

def get_primenumber_under_n(N):
    is_primes = [False, False] + [True for i in range(2, N+1)]
    for i in range(2, int(N**0.5)+1):
        j = 2
        while i*j <= N:
            if is_primes[i*j]:
                is_primes[i*j] = False
            j += 1
    return [i for i, is_prime in enumerate(is_primes) if is_prime]

primenumber_under_n = get_primenumber_under_n(N)
count = 0
for i in range(len(primenumber_under_n)):
    tmp = 0
    for j in range(i, len(primenumber_under_n)):
        tmp += primenumber_under_n[j]
        if tmp == N:
            count += 1
            break
        elif tmp > N:
            break
print(count)