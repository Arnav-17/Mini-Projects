"""This problem is to calculate largest prime factor of given number"""
import numpy as np
a = []
def prime_fac(n):
    for i in range(4, int(np.sqrt(n))+1):
        if n % i == 0:
            for j in range(2, int(np.sqrt(i))+1):
                if i%j==0:
                    break
            else:
                a.append(i)

    return max(a)


print(prime_fac(600851475143))