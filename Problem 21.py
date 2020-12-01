a = []
c = []
e = set()
def d(n):
	m = 0
	for k in range(1, n):
		if n % k == 0:
			a.append(k)
			m += k
	return m
q = 0
for i in range(1, 10000):
	b = d(i)
	if d(b) == i and i != b:
		q += i + b

print(q//2)