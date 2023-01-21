import sys

input = sys.stdin.readline

T = int(input())

'''
골드바흐의 추측 : 2 이상의 모든 짝수는 두 소수의 합으로 나타낼 수 있다.
2 -> NO
나머지 짝수 -> YES
홀수 -> 짝수 + 홀수인데, 소수인 짝수는 2밖에 없으므로 홀수에 2를 뺀 값이 소수인지 판별해야 함
'''

numbers = [False, False] + [True for _ in range(2, int(4000000000001**0.5))]
for i in range(2, int(4000000000001**0.5)+1):
    j = 2
    while i*j <= len(numbers)-1:
        numbers[i*j] = False
        j += 1

def is_prime(n):
    if n > len(numbers):
        for num, flag in enumerate(numbers):
            if flag:
                if n % num == 0:
                    return False
            if num > n//2:
                break
    else:
        return numbers[n]

for _ in range(T):
    A, B = map(int, input().rstrip().split())
    _sum = A+B
    if _sum == 2:
        print('NO')
    elif _sum % 2 == 0:
        print('YES')
    else:
        print('YES') if is_prime(_sum-2) else print('NO')