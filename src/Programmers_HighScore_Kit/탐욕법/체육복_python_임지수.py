def solution(n, lost, reserve):
    is_reserve = [1 for i in range(n)]
    for st in reserve:
        is_reserve[st-1] += 1
    for st in lost:
        is_reserve[st-1] -= 1
    for i in range(n):
        if is_reserve[i] == 0:
            if i-1 >= 0 and is_reserve[i-1] == 2:
                is_reserve[i] += 1
                is_reserve[i-1] -= 1
                continue
            if i+1 <= n-1 and is_reserve[i+1] == 2:
                is_reserve[i] += 1
                is_reserve[i+1] -= 1
    print(is_reserve)
    return len([i for i in is_reserve if i >= 1])