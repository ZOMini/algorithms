# Cортировка пузырьком. O(n^2)
# https://contest.yandex.ru/contest/24734/problems/J/
# J. Пузырёк
n = int(input())
arr = list(map(int, input().split()))
trig = True
first = True
while trig:
    trig = False
    for i in range(0, n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            trig =True
            first=False
    if trig or first:
        print(*arr, sep=' ')
