from math import ceil


def solution(progresses, speeds):
    need_dates = [ceil((100 - progress) / speed) for progress, speed in zip(progresses, speeds)]
    date = 0
    count = 0
    answer = []

    for need_date in need_dates:
        if date < need_date:
            if count != 0:
                answer.append(count)
            date = need_date
            count = 1
        else:
            count += 1

    answer.append(count)

    return answer

