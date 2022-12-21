import sys

input = sys.stdin.readline

min_, max_ = map(int, input().rstrip().split())

check_range = [False for _ in range(min_, max_+1)]
count = len(check_range)
i = 2
while i*i <= max_:
    square = i*i
    j = min_//square if min_%square==0 else min_//square+1
    while square*j <= max_:
        if not check_range[min_-square*j]:
            check_range[min_-square*j] = True
            count -= 1
        j += 1
    i += 1

print(count)