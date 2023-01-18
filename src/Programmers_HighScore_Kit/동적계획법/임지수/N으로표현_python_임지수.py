def solution(N, number):
    dp = []
    for cnt in range(1, 9):
        n_set = set()
        n_set.add(int(str(N)*cnt))
        for i in range(cnt-1):
            for op1 in dp[i]:
                for op2 in dp[-i-1]:
                    n_set.add(op1+op2)
                    n_set.add(op1*op2)
                    n_set.add(op1-op2)
                    if op2 != 0:
                        n_set.add(op1/op2)
        if number in n_set:
            return cnt
        dp.append(n_set)
    return -1