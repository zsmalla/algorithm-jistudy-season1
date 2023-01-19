def can(n, times, mid):
    cnt = 0
    for time in times:
        cnt += mid // time
    return True if cnt >= n else False


def solution(n, times):
    low, high = 1, n * max(times)

    while low <= high:
        mid = (low + high) // 2
        if can(n, times, mid):
            high = mid - 1
        else:
            low = mid + 1

    return low