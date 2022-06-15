# H. Скобочная последовательность
# https://contest.yandex.ru/contest/23758/problems/H/
def solution(input_str:str):
    n = len(input_str)
    if n % 2 != 0:
        return False
    for i in range(0, int(n/2)):
        left = input_str[i]
        right = input_str[n-1]
        value = is_true.get(left)
        if right == value:
            i += 1
            n -= 1
            continue
        elif right != value:
            return False
    return True
is_true = {'{':'}' , '[':']' , '(':')'}
print(solution('[{(())}]'))
