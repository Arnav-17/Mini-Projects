import random
from itertools import permutations
def mymethod():
	a = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
	d = []
	for i in range(10000000):
		c = ''
		for k in range(40):
			b = random.choice(a)
			if b not in c:
				c += b
			else:
				continue
		if c not in d:
			d.append(c)
		else:
			continue 
	x = sorted(d)
	print(x)

# OR

answer = ''.join(list(permutations('0123456789'))[999999])
print(answer)