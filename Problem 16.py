a = str(2**1000)
"""Problem is to calculate sum of digits of 2^1000"""
b = []
for i in a:
    b.append(int(i))
x = 0
for i in range(len(b)):
    x += b[i]
print(x)