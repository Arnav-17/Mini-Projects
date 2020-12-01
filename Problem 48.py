# Problem is to calculate sum of 1^1 + 2^2 + 3^3 + ... + 1000^1000
a = 0
for i in range(1, 1001):
    a += i**i
print(a)