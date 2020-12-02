a = []
b = []
c = []
n = 100000
for i in range(n):
	a.append(i/2*(i+1))
for i in range(n):
	b.append(i/2*(3*i-1))
for i in range(n):
	e = i*(2*i-1)
	if e in (a and b):
		print(e)
	