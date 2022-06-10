# D. Хаотичность погоды
# https://contest.yandex.ru/contest/23389/problems/D/
n = int(input())
work_list = list(map(int, input().split()))
def find_temp():
    result = []
    # Лучше result = 0, далее result += 1, но ладно)
    if work_list[0] > work_list[1]: result.append(work_list[0])
    if work_list[n-1] > work_list[n-2]: result.append(work_list[n-1])
    for i in range(1, n-2):
        if work_list[i] > work_list[i+1] and work_list[i] > work_list[i-1]:
            result.append(work_list[0])
    return len(result)
print(find_temp())
