b = []
c = []
f = []
for i in range(2, 3000):
	a = i*(3*i-1)/2
	b.append(a)
for i in range(2, len(b)):
	for j in range(i, len(b)):
		d = abs(b[i] - b[j])
		e = b[i]+b[j]
		if d in b and e in b:
			c.append(d)
print(min(c))