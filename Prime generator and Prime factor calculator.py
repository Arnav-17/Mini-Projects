import numpy as np
def prime_identifier(n):
	for i in range(2, int(np.sqrt(n)) +1):
		if n % i == 0:
			return 'It is a composite number'
			break
	else:
		return "It is a prime number"

def prime_generator(n):
	for i in range(2,n):
		for j in range(2, int(np.sqrt(i))+1):
			if i % j == 0:
				break
		else:
			print(i)
	return "programme ended"


def prime_fac(n):
	for i in range(2, int(np.sqrt(n))+1):
		if n % i == 0:
			print(i)

print(prime_identifier(102))