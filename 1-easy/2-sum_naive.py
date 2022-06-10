# Сумма 2-х (наивно)
# https://contest.yandex.ru/contest/26365/problems/D/
n = int(input())
fishki = list(map(int, input().split()))
k = int(input())

def new_func(n, fishki, k):
    for i in range(n):
        for i_2 in range(i+1,n):
            if fishki[i] + fishki[i_2] == k:
                print (f'{fishki[i]} {fishki[i_2]}')
                return    
    print ('None')
new_func(n, fishki, k)
