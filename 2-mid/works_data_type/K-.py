# K. Рекурсивные числа Фибоначчи
# https://contest.yandex.ru/contest/23758/problems/K/
def recurs(n):
    if n == 1 or n == 0: 
        return 1
    return recurs(n-2) + recurs(n-1)
n = int(input())
result = recurs(n)
print (result)
