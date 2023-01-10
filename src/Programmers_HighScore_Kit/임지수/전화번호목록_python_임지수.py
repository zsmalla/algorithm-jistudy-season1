def solution(phone_book):
    phone_book.sort()
    n = len(phone_book)
    for i in range(n-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
#				if phone_book[i+1].startwith(phone_book[i]):
#						return False
    return True

def solution2(phone_book):
    hash_map = {}
    for num in phone_book:
        hash_map[num] = 1
    for num in phone_book:
        tmp = ""
        for n in num:
            tmp += n
            if tmp in hash_map and tmp != num:
                return False
    return True