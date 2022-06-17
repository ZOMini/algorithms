# Рекурсия в сортированном массиве
# https://contest.yandex.ru/contest/24734/problems/L/
# L. Два велосипеда
n = int(input())
array = list(map(int, input().split()))
s = int(input())
result = []
def solution(arr, s, left, right):
    if right <= left:
        result.append(-1)
        if len(result) > 0: 
            return
        result.append(-1)
        return
    mid = (left + right) // 2
    if arr[mid] >= s and arr[mid-1] < s:
        result.append(mid+1)
        s = s*2
        if len(result)>1:
            return
        solution(arr, s, mid+1, right)
    elif arr[mid] < s:
        solution(arr, s, left, mid)
    else:
        solution(arr, s, mid+1, right)
solution(array, s, 0, n-1)
print(f'{result[0]} {result[1]}')
