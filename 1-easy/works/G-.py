# G. Работа из дома
# https://contest.yandex.ru/contest/23389/problems/G/
num = int(input())
def binar():
    result = ''
    inter = num
    while inter > 1:
        bi = inter % 2
        inter = inter // 2
        result += str(bi)
        # print(f'inter= {inter} bi={bi} result= {result}')
    result += str(inter)
    return result[::-1]
print (binar())
