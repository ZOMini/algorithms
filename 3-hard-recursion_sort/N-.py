# Сортировка слиянием. Матрица списков.
# N. Клумбы
# https://contest.yandex.ru/contest/24734/problems/N/

# n = int(input())
# arr = []
# for _ in range(0, n):
#     arr.append(list(input().split()))

nums = [[7,9],[7,8],[2,3],[6,10]]
n = 4
def merge_sort(nums): 
    if len(nums) > 1: 
        mid = len(nums)//2
        left = nums[:mid] 
        right = nums[mid:]
        merge_sort(left) 
        merge_sort(right) 
        l = r = k = 0
        while l < len(left) and r < len(right): 
            if left[l] < right[r]: 
                nums[k] = left[l] 
                l+=1
            else: 
                nums[k] = right[r] 
                r+=1
            k+=1
        while l < len(left): 
            nums[k] = left[l] 
            l+=1
            k+=1
        while r < len(right): 
            nums[k] = right[r] 
            r+=1
            k+=1

def solution(nums):
    result = [nums[0]]
    for i in range(1, len(nums)):
        if nums[i][0] == result[-1][0]:
            result[-1][0] = result[i][0]
        elif nums[i][0] > result[-1][0] and nums[i][1] > result[-1][1]:
            result.append(nums[i])
    return result
        
merge_sort(nums)
print(nums)
result = solution(nums)
for i in result:
    print(*i, sep=' ')
