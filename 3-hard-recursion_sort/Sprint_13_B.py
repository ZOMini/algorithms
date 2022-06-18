# https://contest.yandex.ru/contest/24735/problems/B/
# B. Эффективная быстрая сортировка
# ID 66379349

# import random
# Сильно помогло https://gb.ru/posts/python_sort
from dataclasses import dataclass


@dataclass(order=False,frozen = True)
class One_Man:
    login: str
    resolved: int
    penalty: int

    def __gt__(self, other: 'One_Man') -> bool:
        return (
            (-self.resolved, self.penalty, self.login)
            > (-other.resolved, other.penalty, other.login)
        )

    def __repr__(self):
        return self.login

def eff_quicksort(nums, start, end):
    if start >= end: 
        return
    m_start, m_end = start, end
    pivot = nums[(end + start) // 2] # nums[random.randint(start, end)]
    while m_start <= m_end:
        while nums[m_start] < pivot: m_start += 1
        while nums[m_end] > pivot: m_end -= 1
        if m_start <= m_end:
            nums[m_start], nums[m_end] = nums[m_end], nums[m_start]
            # print(nums)
            m_start, m_end = m_start + 1, m_end - 1
    eff_quicksort(nums, start, m_end)
    eff_quicksort(nums, m_start, end)
    return nums

# def presort_edit(one_man):
#     # Иначе будет не правильно сортировать.
#     one_man[1] = - int(one_man[1]) 
#     one_man[2] = int(one_man[2])
#     return [one_man[1], one_man[2], one_man[0]]

if __name__ == '__main__':
    mans = int(input())
    array = list()
    for _ in range(mans):
        login, resolved, penalty = input().strip().split(' ') # [имя,бал,штраф]
        array.append(One_Man(login, int(resolved), int(penalty)))
    result_array = eff_quicksort(array, 0, len(array)-1)
    for i in range(mans):
        print(array[i])


# def test_list_sort(arr:list):  # [[a],[b]]
#     return arr[0] < arr[1]
# x_x = [[1, -9, 'aaaa'],[1, -9, 'aaab']]
# print (test_list_sort(x_x))
