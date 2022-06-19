# Эффективное сравнение 2-х списков.
# https://contest.yandex.ru/contest/24734/problems/D/
# D. Печеньки
n = int(input())
n_c = list(map(int, input().split()))
m = int(input())
m_c = list(map(int, input().split()))
# n = 10
# n_c = [8,5,5,8,6,9,8,2,4,7]
# m = 8
# m_c = [9,8,1,1,1,5,10,8]
def solution():
    n_c.sort()
    m_c.sort()
    result = 0
    m_c_len = len(m_c)
    idx_m = 0
    for idx_n in range (0,len(n_c)):
        while idx_m < m_c_len:
            if n_c[idx_n] <= m_c[idx_m]:
                result += 1
                idx_m += 1
                break
            idx_m += 1
    return result
print(solution())
