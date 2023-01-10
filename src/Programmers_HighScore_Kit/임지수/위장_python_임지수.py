from collections import defaultdict
from itertools import combinations


def solution(clothes):
    answer = 1

    kinds = defaultdict(int)
    for clothe, kind in clothes:
        kinds[kind] += 1
    for num_of_kind in kinds.values():
        answer *= (num_of_kind + 1)

    return answer - 1


def solution1(clothes):  # 시간초과 (케이스 1)
    answer = 0
    kinds = defaultdict(int)
    for clothe, kind in clothes:
        kinds[kind] += 1
    for i in range(1, len(kinds) + 1):
        combs = combinations(kinds, i)
        for comb in combs:
            tmp = 1
            for kind in comb:
                tmp *= kinds[kind]
            answer += tmp
    return answer