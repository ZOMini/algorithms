# J. Факторизация
# https://contest.yandex.ru/contest/23389/problems/J/
import functools

n = int(input())
nums = []
for i in range(2,n + 1):
    if n % i == 0:
        count = 1
        for j in range(2,(i//2 + 1)):
            if(i % j == 0):
                count = 0
                break
        if(count == 1):
            nums.append(i)
# summ = functools.reduce(lambda a, b : a * b, nums)
# if summ != n:
#     nums.append(n - summ)
print(nums)

