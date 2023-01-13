def is_h(h, citations):
    return len([i for i in citations if i >= h]) >= h


def solution1(citations):
    low, high = 1, len(citations)

    while low <= high:
        mid = (low + high) // 2
        if is_h(mid, citations):
            low = mid + 1
        else:
            high = mid - 1
    return high


def solution(citations):
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if citations[i] < i + 1:
            return i
    return len(citations)
