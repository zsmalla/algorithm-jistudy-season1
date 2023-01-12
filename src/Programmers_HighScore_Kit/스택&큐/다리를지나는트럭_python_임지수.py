from collections import deque


def solution(bridge_length, weight, truck_weights):
    trucks = deque(truck_weights)
    on_bridge = deque([0 for _ in range(bridge_length)])
    sum_on_bridge = 0
    answer = 0
    while trucks:
        answer += 1
        sum_on_bridge -= on_bridge.popleft()

        if trucks and sum_on_bridge + trucks[0] <= weight:
            sum_on_bridge += trucks[0]
            on_bridge.append(trucks.popleft())
        else:
            on_bridge.append(0)

    return answer + bridge_length