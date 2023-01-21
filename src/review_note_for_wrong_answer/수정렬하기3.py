# N개의 수가 주어졌을 떄, 이를 오름차순으로 정렬하는 프로그램을 작성
# 시간제한 5초
# 메모리 제한 8MB

import sys

input = sys.stdin.readline

N = int(input())
numbers = [int(input()) for _ in range(N)]

def solution(N, numbers):
    counter = [0 for i in range(10001)]
    for num in numbers:
        counter[num] += 1
    for num, count in enumerate(counter):
        if count > 0:
            for _ in range(count):
                print(num)

solution(N, numbers)