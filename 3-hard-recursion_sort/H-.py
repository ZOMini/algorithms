# Сортировка вставками + компаратор
# H. Большое число
# https://contest.yandex.ru/contest/24734/problems/H/
n = int(input())
arr = list(map(str, input().split()))

def is_first_high(c_1, c_2):  # функция-компаратор
    return c_1[0:] > c_2[0:]

# воспользуемся уже знакомой сортировкой вставками
def insertion_sort_by_comparator(array, less):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        # заменим сравнение item_to_insert < array[j-1] на компаратор less
        while j > 0 and less(item_to_insert, array[j-1]):
            array[j] = array[j-1]
            j -= 1
            array[j] = item_to_insert
    return array
print("".join(insertion_sort_by_comparator(arr, is_first_high)))
