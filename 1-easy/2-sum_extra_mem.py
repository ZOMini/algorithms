# Сумма 2-х, через set(),макс скорость, с доп. памятью.
# https://contest.yandex.ru/contest/26365/problems/E/
n = int(input())
fishki = list(map(int, input().split())) #неубывание, или добавить sort().
k = int(input())
new = set()

def twosum_with_sort(fishki, k, n):
    for a in fishki:
        y = k - a 
        if y in new:
            print (f'{a} {y}')
            return
        else:
            new.add(a)    

    print ('None')

twosum_with_sort(fishki, k, n)
