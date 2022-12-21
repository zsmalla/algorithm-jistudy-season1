import sys

input = sys.stdin.readline

def get_primenumber_under(n):
    is_primes = [False, False] + [True for _ in range(2, n+1)]
    for i in range(2, int(n**0.5)+1):
        j = 2
        while i*j <= n:
            if is_primes[i*j]:
                is_primes[i*j] = False
            j += 1
    return is_primes

def is_prime(n):
    if n > len(primenumbers):
        for num, primeFlag in enumerate(primenumbers):
            if primeFlag:
                if n % num == 0:
                    return False
            if num > n//2:        # 정렬된 소수 배열
                break
    else:
        if not primenumbers[n]:
            return False
    return True

T = int(input())
# 골드바흐의 추측 : 4보다 큰 짝수는 두 소수의 합으로 나타낼 수 있다.
# 2 -> x
# 3 -> x
# 짝수 -> o
# 홀수 -> 두 수의 합이 홀수가 되는 경우는 짝수 + 홀수 -> 소수 중 짝수는 2밖에 없다.
# 따라서 홀수의 경우 해당 수에서 2를 뺀 값이 소수인지를 확인하면 된다.
#   -> 해당 수를 sqrt(n) 내의 소수들로 나눠서 나눠지면 소수가 아닌 것으로 판별할 수 있다.
primenumbers = get_primenumber_under(2*(10**6))

for t in range(T):
    A, B = map(int, input().rstrip().split())
    sum_AB = A+B
    if sum_AB == 2 or sum_AB == 3:
        print('NO')
        continue
    elif sum_AB % 2 == 0:
        print('YES')
        continue
    else:
        print('YES') if is_prime(sum_AB-2) else print('NO')