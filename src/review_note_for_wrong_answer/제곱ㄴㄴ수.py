import sys

input = sys.stdin.readline

_min, _max = map(int, input().rstrip().split())
is_square_list = [False for _ in range(_min, _max+1)] # min ~ max
count = len(is_square_list)
i = 2

while i**2 <= _max:
    square = i**2
    j = _min//square if not _min%square else _min//square+1
    while square*j <= _max:
        if not is_square_list[_min-square*j]:
            is_square_list[_min-square*j] = True
            count-=1
        j+=1
    i+=1

print(count)