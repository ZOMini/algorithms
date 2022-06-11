# K. Списочная форма
# https://contest.yandex.ru/contest/23389/problems/K/
n = int(input())
first = list(map(str, input().split()))
second = int(input())
first = int(''.join(first))
result = list(str(first + second))
print(result)
