list1 = [77, 5, 5 , 22, 13, 55, 97, 7, 769, 1, 0 ,9]
n = len(list1)
while n > 1:
    n -= 1
    for i in range(n):
        if list1[i] > list1[i+1]:
            list1[i], list1[i+1] = list1[i+1], list1[i]

print(list1)