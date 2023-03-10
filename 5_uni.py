a = [77, 5, 5 , 22, 13, 55, 97, 7, 769, 1, 0 ,9]
b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

c = []
d = []
e = []

k = list(set(a))

n = len(b)
for i in range(n):
    if b[i] in k:
        c.append(b[i])
for i in range(len(a)):
    if a[i] not in b:
        d.append(a[i])

e = list(set(a + b))
print('交集: ', c)
print('差集: ', d)
print('聯集: ', sorted(e))