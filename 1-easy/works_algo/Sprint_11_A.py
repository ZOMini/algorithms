# A. Ближайший ноль
# id 65220917
# https://contest.yandex.ru/contest/23390/problems/A/
def _input():
    input()
    all_num = input().split()
    return len(all_num), all_num


def first_main():
    n, all_num = _input()
    distance = []
    null_position = None
    for i, elem in enumerate(all_num):
        if elem == '0':
            null_position = i
            distance.append(0)
            continue
        if (elem != '0' and null_position != None):
            distance.append(i - null_position)
        else:
            distance.append(n)
    null_position = None
    for i, elem in reversed(list(enumerate(all_num))):
        if elem == '0':
            null_position = i
            continue
        if (elem != '0' and null_position != None and int(distance[i]) > null_position - i):
            distance[i] = (null_position - i)
    print(*distance)

if __name__ == '__main__':
    first_main()
