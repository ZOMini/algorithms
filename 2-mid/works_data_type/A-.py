# Матрица. Список списков. Транспонирование матрицы.
# A. Мониторинг
# https://contest.yandex.ru/contest/23758/problems/A/
n = int(input()) #line
m = int(input()) #column
matrix_in = [[0] * m for i in range(n)]
matrix_out = [[0] * n for i in range(m)]
for idx in range(0,n):
    matrix_in[idx] = list(map(int, input().split()))
print (matrix_in)
for line in range(0,n):
    for column in range(0,m):
        matrix_out[column][line] = matrix_in[line][column]
print (matrix_out)
