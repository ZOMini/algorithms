# Матрица - списки списков - [[],[],[]] - генератор
# C. Соседи
# https://contest.yandex.ru/contest/23389/problems/C/
lines = int(input())
columns = int(input())
matrix = [[0] * columns for i in range(lines)]
for i in range(0, lines):
    matrix[i] = list(map(int, input().split()))
targ_line = int(input())
targ_column = int(input())

# lines = 4
# columns = 3
# matrix = [[1,2,3],[0,2,6],[7,4,1],[2,7,0]]
# targ_line = 3
# targ_column = 0


def find_in_matrix():
    result = []
    if targ_column == 0: result += str(matrix[targ_line][targ_column+1])
    elif targ_column == columns-1: result += str(matrix[targ_line][targ_column-1])
    else: 
        result += str(matrix[targ_line][targ_column+1])
        result += str(matrix[targ_line][targ_column-1])
    if targ_line == 0: result += str(matrix[targ_line+1][targ_column])
    elif targ_line == lines-1: result += str(matrix[targ_line-1][targ_column])
    else:
        result += str(matrix[targ_line+1][targ_column])
        result += str(matrix[targ_line-1][targ_column])
    return result
result = find_in_matrix()
result.sort()
print(" ".join(result))

# Альт. решение.
# def neighbors(matrix, y, x):
#     h = []
#     if x + 1 < len(matrix[0]):
#         h.append(matrix[y][x + 1])
#     if x - 1 >= 0:
#         h.append(matrix[y][x - 1])
#     if y + 1 < len(matrix):
#         h.append(matrix[y + 1][x])
#     if y - 1 >= 0:
#         h.append(matrix[y - 1][x])
#     return h


# n = int(input())
# m = int(input())
# matrix = [list(map(int, input().split())) for i in range(n)]
# y, x = int(input()), int(input())
# print(*sorted(neighbors(matrix, y, x)))
