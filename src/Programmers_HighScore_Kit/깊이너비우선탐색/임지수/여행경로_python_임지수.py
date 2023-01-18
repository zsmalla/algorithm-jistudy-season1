from collections import defaultdict

answer = []


def dfs(MAP, nxt, left, N, route):
    global answer

    if left == 0:
        answer.append(route)
        return

    for ticket_idx in range(len(MAP[nxt])):
        if not MAP[nxt][ticket_idx][1]:
            MAP[nxt][ticket_idx][1] = True
            dfs(MAP, MAP[nxt][ticket_idx][0], left - 1, N, route + [MAP[nxt][ticket_idx][0]])
            MAP[nxt][ticket_idx][1] = False


def solution(tickets):
    global answer
    tickets.sort(key=lambda x: x[1])  # 알파벳 순서가 앞서는 경로 우선
    ticket_dict = defaultdict(list)

    for fr, to in tickets:
        ticket_dict[fr].append([to, False])

    dfs(ticket_dict, 'ICN', len(tickets), len(tickets), ['ICN'])
    print(answer)
    return answer[0]