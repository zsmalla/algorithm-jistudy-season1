import sys

input = sys.stdin.readline

numOfTestcase = int(input())

def back_tracking(res, add):
    global count

    if res >= n:
        return

    res += add

    if res == n:
        count += 1

    back_tracking(res, 1)
    back_tracking(res, 2)
    back_tracking(res, 3)

for _ in range(numOfTestcase):
    count = 0
    n = int(input())

    back_tracking(0, 0)
    print(count)