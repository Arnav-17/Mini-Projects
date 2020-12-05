import numpy as np
from statistics import mode
a = []
for i in range(1,999):
	for j in range(1,999):
		p = i+j+np.sqrt(i**2+j**2)
		if p == int(p) and p <= 1000:
			a.append(p)
print(mode(a))
