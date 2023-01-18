answer = 0


def dfs(numbers, idx, count, target):
    global answer

    if idx == len(numbers):
        if count == target:
            answer += 1
        return

    dfs(numbers, idx + 1, count + numbers[idx], target)
    dfs(numbers, idx + 1, count - numbers[idx], target)


def solution(numbers, target):
    global answer

    dfs(numbers, 0, 0, target)

    return answer