import sys

input = sys.stdin.readline

def get_odd_primenumber_under(n):
    is_primes = [False, False] + [True for _ in range(2, n+1)]
    for i in range(2, n+1):
        j = 2
        while i*j <= n:
            if is_primes[i*j]:
                is_primes[i*j] = False
            j += 1
    return [num for num, is_prime in enumerate(is_primes) if is_prime and num % 2 != 0]

odd_primenumbers = get_odd_primenumber_under(1000000)

while True:
    n = int(input())
    if n == 0 : break
    find_flag = False
    odd_primenumber_under_n = []

    for num in odd_primenumbers:
        if num > n:
            break
        odd_primenumber_under_n.append(num)

    for i in range(len(odd_primenumber_under_n)):
        for j in range(len(odd_primenumber_under_n)-1, i-1, -1):
            if odd_primenumber_under_n[i]+odd_primenumber_under_n[j] == n:
                print(f'{n} = {odd_primenumber_under_n[i]} + {odd_primenumber_under_n[j]}')
                find_flag = True
                break
        if find_flag:
            break

    if not find_flag:
        print("Goldbach's conjecture is wrong.")