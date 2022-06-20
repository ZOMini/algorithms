# https://contest.yandex.ru/contest/24734/problems/I/
# I. Любители конференций
n = int(input())
arr = list(map(int, input().split()))
k = int(input())
arr.sort()
max_arr = arr[-1]
id_dict = {k:0 for k in reversed(range(1,max_arr+1))}

def solution():
    for i in arr:
        id_dict[i] += 1
    from operator import itemgetter
    id_dict
    sorted_tuple = sorted(id_dict.items(), key=itemgetter(1))
    return sorted_tuple
result_dict = solution()
result_str = ''
result_dict.reverse()
for key, val in result_dict:
    if k == 0:
        break
    result_str += f'{key} '
    k -= 1
print(result_str)
