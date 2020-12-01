import numpy as np
# c = []
# for i in range(2, 1000):
# 	for j in range(2, i):
# 		if i % j == 0:
# 			break
# 	else:
# 		c.append(i)
# for 
# for b in c:
# 	for i in range(10):
# 		y = x**2 + a*x + b
# 		counter = 0
# 		while y % i != 0:
# 			counter += 1
# 		c.append(f'{counter} {y}')
# 	print(max(c))

def primes(n):
	for j in range(2, n):
		if j >1:
			for i in range(2, int(np.sqrt(j))):
				if j % i == 0:
					break
			else:
				print(j) 

print(primes(50))
# def primes(n):
# 	for num in range(n):  
# 	   if num > 1:  
# 	       for i in range(2,num):  
# 	           if (num % i) == 0:  
# 	               break  
# 	       else:  
# 	           print(num)  