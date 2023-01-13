from heapq import heappush, heappop, nlargest


def solution(operations):
    min_heap = []
    for operation in operations:
        op, value = operation.split()
        if op == 'I':
            heappush(min_heap, int(value))
        else:
            if min_heap:
                if value == '1':
                    min_heap.pop(min_heap.index(nlargest(1, min_heap)[0]))
                else:
                    heappop(min_heap)

    return [nlargest(1, min_heap)[0], min_heap[0]] if min_heap else [0, 0]