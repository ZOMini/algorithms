# Сортировка пересчетом O(n). Если есть возможность пересчитать элементы(их не много и часто повторяются).
# G. Гардероб
# https://contest.yandex.ru/contest/24734/problems/G/

n = int(input())
arr = list(map(int, input().split()))
col = {a : 0 for a in range(0,3)} 
result = []
def solution():
    for i in arr:
        col[i] += 1
    for k, v in col.items():
        _str = (str(k) +' ') * v
        result.append(_str)
        
solution()
print(*result, sep='')
