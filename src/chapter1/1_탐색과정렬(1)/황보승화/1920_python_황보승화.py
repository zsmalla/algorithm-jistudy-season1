#2022-12-13
def binary_search(array, key, low, high):
    while low <= high:
        mid = (low + high) // 2 # '/'는 소수 나눗셈, '//'는 정수 나눗셈(버림)
        if array[mid] == key:
            return True
        elif array[mid] > key:
            high = mid - 1
        else :
            low = mid + 1
    return False

N = int(input())
arr_N = list(map(int, input().split())) # map : 문자열 -> 정수
arr_N.sort() # 정렬

M = int(input())
arr_M = list(map(int, input().split()))

for i in arr_M:
    if binary_search(arr_N, i, 0, N-1): # 아~ 이거 괜찮다!!
        print(1)
    else:
        print(0)

# ----------------------------------------------
# for i in arr_M :
#     if i in arr_N :
#         print(1)
#     else :
#         print(0)
# ----------------------------------------------
#
# arr = input().split() -> 문자열
#
# for i in arr_N: # arr_N의 값을 순서대로 순회
# for i in range(len(arr_N)): # arr_N의 인덱스를 순서대로 순회
#
# a=[1, 2, 3]
# print(a in b) # b 안에 a 값이 있는지 검사