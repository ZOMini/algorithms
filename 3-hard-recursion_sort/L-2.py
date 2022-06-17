# Рекурсия в сортированном массиве
# https://contest.yandex.ru/contest/24734/problems/L/
# L. Два велосипеда
def main(l, r):
    if r <= l and l != 0:
        return -1
    mid = (l + r) // 2
    if (arr[mid] >= pri and (arr[mid-1]<pri or mid==0)):
        return  mid + 1
    elif pri <= arr[mid]:
        return main(l, mid)
    else:
        return main(mid + 1, r)

n = int(input())
arr = list(map(int, input().split()))
price = int(input())
left = 0
right = n
pri = price
result = ''
res1 = main(left ,right)
result = f'{res1}'
pri = price*2
res2 = main(left, right)
print(f'{result} {res2}')
