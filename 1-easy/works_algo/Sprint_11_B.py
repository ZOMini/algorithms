# Б. Ловкость рук
# id 65220190
# https://contest.yandex.ru/contest/23390/problems/B/
def _input():
    k = int(input())
    all_num = input()+input()+input()+input()
    return k, all_num

def _sum(i, k, all_num, points):
        i = str(i)
        cur_num = all_num.count(i)
        if cur_num <= k and cur_num != 0:
            points += 1
        return points
        
def second_main():
    k, all_num = _input()
    points = 0
    k = k * 2
    for i in range(1, 10):
        points = _sum(i, k, all_num, points)
    print (points)
    

if __name__ == '__main__':
    second_main()
