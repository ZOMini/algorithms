# F. Палиндром
# https://contest.yandex.ru/contest/23389/problems/F/
str_input = str(input())
len_str_input = int(len(str_input))
if str_input.isalnum() and (len_str_input % 2) == 0:
    for i in range(0, int(len_str_input/2)):
        if str_input[i] == str_input[len_str_input-i-1]:
            result = 'True'
            continue
        result = 'False'
    print(result)
else: print('False')
