def merge_sort(lst):
    N = len(lst)
    if N <= 1:
        return lst
    mid = len(lst)//2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return merge(left, right)

def merge(left, right):
    sorted_list = []
    i, j = 0, 0
    while (i < len(left)) and (j < len(right)):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i+=1
        else:
            sorted_list.append(right[j])
            j+=1

    if i < len(left):
        sorted_list += left[i:]
    if j < len(right):
        sorted_list += right[j:]

    return sorted_list

N = int(input())
lst = [int(input()) for _ in range(N)]
for i in merge_sort(lst):
    print(i)
