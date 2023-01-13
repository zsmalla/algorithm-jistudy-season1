from collections import deque


def solution(prices):
    answer = [0 for _ in range(len(prices))]
    upper = deque()

    for idx, price in enumerate(prices):
        while upper and price < prices[upper[-1]]:
            j = upper.pop()
            answer[j] = idx - j
        upper.append(idx)

    while upper:
        j = upper.pop()
        answer[j] = (len(prices) - 1) - j

    return answer