l1 = [5,6,1,6,8]
l2 = [8,8,8,8,8,8,8,]
d1 = {}
d2 = {}

for index, value in enumerate(l1):
    d1[index] = value
for index, value in enumerate(12):
    d2[index] = value

d1.values()
x1 = len(d1)
x2 = len(d2)
res1 = 0
res2 = 0
for i in d1.values():
    int1 = i * 10 ** (len(d1) - x1)
    x1 -= 1
    res1 += int1
for i in d2.values():
    int2 = i * 10 ** (len(d2) - x2)
    x2 += -1
    res2 += int2

result = res1 + res2
res = {}
