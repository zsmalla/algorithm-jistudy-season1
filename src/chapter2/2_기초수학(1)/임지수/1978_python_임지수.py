import sys

input = sys.stdin.readline

def prime_numbers_under_N(N):
    array = [False, False] + [True for _ in range(2, N+1)]

    for i in range(2, int(N**0.5)+1):
        if array[i]:
            j = 2
            while i*j <= N:
                array[i*j] = False
                j += 1
    return [i for i, j in enumerate(array) if i >= 2 and j]

N = int(input())
nums = list(map(int, input().rstrip().split()))
prime_numbers_under_max_num = prime_numbers_under_N(max(nums))
print(len([prime_number for prime_number in nums if prime_number in prime_numbers_under_max_num]))
