import itertools
import numpy as np
a = '1234567'
d = itertools.permutations(a)
c = []
for j in list(d):
	b = ''
	for i in range(len(j)):
		b += j[i]
	c.append(int(b))
g = []
for i in range(2, len(c)):
	for j in range(2, int(np.sqrt(c[i]))+1):
		if c[i] % j == 0:
			break
	else:
		g.append(c[i])
print(max(g))
