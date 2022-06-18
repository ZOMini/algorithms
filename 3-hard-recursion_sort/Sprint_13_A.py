# Массив отсортирован, но начало не извесно.
# A. Поиск в сломанном массиве
# https://contest.yandex.ru/contest/24735/problems/A/ 

def broken_search(nums, target) -> int:
    start = 0
    end = len(nums) - 1
    while start <= end:
        middle = (start + end) // 2
        if target == nums[middle]:
            return middle
        if nums[start] <= nums[middle]:
            if target < nums[middle] and target >= nums[start]:
                end = middle - 1
            else:
                start = middle + 1
        else: # if nums[start] > nums[middle]:
            if target > nums[middle] and target <= nums[end]:
                start = middle + 1
            else:
                end = middle -1
    return -1


# def test():
#     arr = [5]
#     print(broken_search(arr, 5))

# test()
