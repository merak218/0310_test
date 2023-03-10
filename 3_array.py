list1 = [*range(10)]

sum1 = 0
sum2 = 0

list_even = []
list_odd = []

for i in range(len(list1)):
    if list1[i]%2 == 0:
        sum2 += int(list1[i])
        list_even.append(list1[i])
    else:
        sum1 += int(list1[i])
        list_odd.append(list1[i])
print(sum1-sum2)
print('奇數:', list_odd)
print('偶數:', list_even)
