def solution(arr):
    result = [arr[0]]
    for idx in range(len(arr)):
        if arr[idx] != result[-1]:
            result.append(arr[idx])
    return result