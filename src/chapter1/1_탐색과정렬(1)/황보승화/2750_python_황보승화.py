# 이거 아래 코드로 했을 때는 정답인데 위 코드로 했을 때는 틀렸다는데 이유를 모르겠어...
def counting_sort(arr):
    count = [0] * (max(arr) + 1)

    for num in arr:
        count[num] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    result = [0] * (len(arr))

    for num in arr:
        idx = count[num]
        result[idx - 1] = num
        count[num] -= 1

    for l in result:
        print(l)


N = int(input())
arr = []

for i in range(N):
    arr.append(int(input()))

counting_sort(arr)

# ---------------------------
# N = int(input())
# arr = []

# for i in range(N):
#   arr.append(int(input()))

# for j in range(len(arr)):
#   for k in range(len(arr)):
#     if arr[j] < arr[k]:
#         arr[j], arr[k] = arr[k], arr[j]

# for l in arr:
#   print(l)