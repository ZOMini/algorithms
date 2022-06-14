# L. Лишняя буква
# https://contest.yandex.ru/contest/23389/problems/L/
# Алгаритм для больших строк
import string

first = list(str(input()))
second = list(str(input()))
first_len = len(first)
second_len = len(second)
matrix_1 = {x: 0 for x in string.ascii_lowercase}
matrix_2 = {x: 0 for x in string.ascii_lowercase}
for i in first:
    matrix_1[i] += 1
for i in second:
    matrix_2[i] += 1
for i in string.ascii_lowercase:
    if matrix_1[i] != matrix_2[i]:
        print(i)