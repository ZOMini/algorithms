# https://contest.yandex.ru/contest/23758/problems/L/
# L. Фибоначчи по модулю
n, k = (int(i) for i in input().split())
ab = [1, 1]
d=(10 ** k)
if n < 2:
    fib = 1
else:
    n -= 1
    for i in range(n):
        s = (ab[0] + ab[1]) % d
        ab[0] = ab[1]
        ab[1] = s
        fib = ab[1]
print(fib)


# def recurs(n):
#     if n == 1 or n == 0: 
#         return 1
#     return recurs(n-2) + recurs(n-1)
# n, k = map(int, list(input().split()))
# result = str(recurs(n))
# result = result[k:]
# print (result)
