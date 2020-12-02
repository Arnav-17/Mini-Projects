import itertools
a = '1234567890'
d = itertools.permutations(a)
c = []
for j in list(d):
	b = ''
	for i in range(len(j)):
		b += j[i]
	c.append(b)
g = []
for i in range(len(c)):
	f = ''
	for j in range(1,4):
		f+= c[i][j]
	f = int(f)
	if f%2 == 0:
		g.append(str(c[i]))
h = []
for i in range(len(g)):
	f = ''
	for j in range(2,5):
		f+= g[i][j]
	f = int(f)
	if f%3 == 0:
		h.append(str(g[i]))
k = []
for i in range(len(h)):
	f = ''
	for j in range(3,6):
		f+= h[i][j]
	f = int(f)
	if f%5 == 0:
		k.append(str(h[i]))
l = []
for i in range(len(k)):
	f = ''
	for j in range(4,7):
		f+= k[i][j]
	f = int(f)
	if f%7 == 0:
		l.append(str(k[i]))
m = []
for i in range(len(l)):
	f = ''
	for j in range(5,8):
		f+= l[i][j]
	f = int(f)
	if f%11 == 0:
		m.append(str(l[i]))
n = []
for i in range(len(m)):
	f = ''
	for j in range(6,9):
		f+= m[i][j]
	f = int(f)
	if f%13 == 0:
		n.append(str(m[i]))
o = []
for i in range(len(n)):
	f = ''
	for j in range(7,10):
		f+= n[i][j]
	f = int(f)
	if f%17 == 0:
		o.append(int(n[i]))
x = 0
for i in o:
	x+=i
print(x)