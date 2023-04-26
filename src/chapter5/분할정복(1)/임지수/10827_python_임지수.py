# 실수 a와 정수 b가 주어졌을 때, a의 b제곱을 정확하게 계산하는 프로그램을 작성
# 첫째 줄에 a와 b가 주어진다. (0 < a < 100, 1 ≤ b ≤ 100) a는 최대 소수점 9자리이며, 소수가 0으로 끝나는 경우는 없다. a는 항상 소수점이 포함되어 있다.
'''
3.141592 3 => 31.006257328285746688
0.1 10 => 0.0000000001
1.01 5 => 1.0510100501
'''

import sys

input = sys.stdin.readline

def main():
    a, b = input().rstrip().split()
    e = (len(a) -1) - a.find('.')       # 소수점 위치
    a = a.replace('.', '')              # 소수점 제거
    result = str(int(a) ** int(b))      # 정수 제곱 연산
    e *= int(b)                         # 소숫점도 그만큼 연산
    if len(result) < e:
        result = '0'*(e-len(result)) + result   # 정수로 변환할 때 숫자가 부족한 경우

    result = result[:-e] + '.' + result[-e:]    # 최종 소수점 삽입

    print(result) if result[0] != '.' else print('0' + result)      # 예외 처리

if __name__ == '__main__':
    main()