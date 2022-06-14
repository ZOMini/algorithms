# I. Степень четырёх
# https://contest.yandex.ru/contest/23389/problems/I/
num = int(input())
x = 4
degree = [2,3,4,5,6]
tuple_res = tuple(map(lambda y: x ** y, degree))
if num in tuple_res:
    print('True')
else:
    print('False')

