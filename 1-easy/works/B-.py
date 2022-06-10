# B. Чётные и нечётные числа
# https://contest.yandex.ru/contest/23389/problems/B/
fishki = list(map(int, input().split()))
res = fishki[0] % 2
for i in fishki[1:3]:
    if i % 2 == res:
        if i == fishki[2]: 
            print('WIN')
            break
        continue
    elif i % 2 != res:
        print ('FAIL')
        break
