import numpy as np
def prime_generator(n):
	x = []
	a = 0
	for i in range(2,n):
		for j in range(2, int(np.sqrt(i))+1):
			if i % j == 0:
				break
		else:
			a+=i
	return a
print(prime_generator(2000000))
			