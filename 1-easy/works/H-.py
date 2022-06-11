# H. Двоичная система
# https://contest.yandex.ru/contest/23389/problems/H/
first_bin = str(input())
second_bin = str(input())
len_f=len(first_bin)
len_s=len(second_bin)
if len_f >= len_s: 
    second_bin = '0'*(len_f-len_s) + second_bin
else:
    first_bin = '0'*(len_s-len_f) + first_bin
def summ_bin():
    result = ''
    next_idx = 0
    for i in range(len(first_bin)-1, -1, -1):
        temp_bin = int(first_bin[i]) + int(second_bin[i]) + next_idx
        if temp_bin == 3: 
            next_idx = 1
            result += '1'
        elif temp_bin == 2:
            next_idx = 1
            result += '0'            
        elif temp_bin == 1:
            next_idx = 0
            result += '1'
        elif temp_bin == 0:
            next_idx = 0
            result += '0'
    if next_idx == 1:
        result += '1'
    return result[::-1]
print (summ_bin())
