import sys

input = sys.stdin.readline

N = int(input())
roads = list(map(int, input().rstrip().split()))
oil_prices = list(map(int, input().rstrip().split()))
before_price = oil_prices[0]
distance_using_before_oil_price = 0
result = 0

for city_idx in range(1, N):
    if before_price < oil_prices[city_idx]:
        distance_using_before_oil_price += roads[city_idx-1]
    else:
        distance_using_before_oil_price += roads[city_idx - 1]
        result += before_price * distance_using_before_oil_price

        distance_using_before_oil_price = 0
        before_price = oil_prices[city_idx]

result += distance_using_before_oil_price*before_price

print(result)