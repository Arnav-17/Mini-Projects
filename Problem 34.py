def Fac(n):
	a = 1
	for i in range(1,n+1):
		a*=i
	return a
i = 3
b = 0
"""i cannot be greater than 2540160 Million because 99,99,999 has factorial digit sum = 2540160 
because 9!*6 = 2540160"""
while i < 2540160:  
	c = 0
	for j in range(len(str(i))):
		c += Fac(int(str(i)[j]))
	if i == c:
		b+=i
	i+=1
print(b)
