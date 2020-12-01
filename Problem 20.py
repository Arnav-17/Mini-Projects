"""Problem is to calculate sum of digits of 100!"""
a = 1
for i in range(1, 101):
    a *= i
c = str(a)
b = []
for i in c:
    b.append(int(i))
x = 0
for i in range(len(b)):
    x += b[i]
print(x)