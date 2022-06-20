# ----
# E. Покупка домов
# https://contest.yandex.ru/contest/24734/problems/E/
n, k = list(map(int,input().split()))
arr = list(map(int, input().split()))

def solution():
    arr.sort()
    idx = 0
    result = []
    if len(arr) == 1 and arr[0] <= k:
        return 1
    elif len(arr) == 1 and arr[0] > k:
        return 0
    while sum(result) + arr[idx] <= k:
        result.append(arr[idx])
        idx += 1
    return len(result)
print(solution())
