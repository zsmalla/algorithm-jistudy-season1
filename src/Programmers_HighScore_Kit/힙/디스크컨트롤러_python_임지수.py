from heapq import heappush, heappop, heapify


def solution(jobs):
    n = len(jobs)
    heapify(jobs)
    can_do = []
    time, answer = 0, 0
    while True:
        while jobs and jobs[0][0] <= time:
            request, process = heappop(jobs)
            heappush(can_do, (process, request))

        if not can_do and jobs:
            time = jobs[0][0]
            continue

        if can_do:
            process, request = heappop(can_do)
            done = time + process
            answer += (done - request)
            time = done
        else:
            break

    return answer // n