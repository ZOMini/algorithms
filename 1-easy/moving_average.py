# Скользяцие средние / Moving average
# https://contest.yandex.ru/contest/26365/problems/C/
n = int(input())
qi = list(map(int, input().split()))
k = int(input())
qi_1 = int()
for i in range(k):
    qi_1 += qi[i]
qi_sort = list()    
qi_sort.append(qi_1/k)    
current_sum = qi_sort[0]*k
for i in range(n-k):
    current_sum -= qi[i] 
    current_sum += qi[(i+k)]
    current_avg = current_sum/k
    qi_sort.append(current_avg)
d = ' '.join([str(item) for item in qi_sort])    
print (d)
