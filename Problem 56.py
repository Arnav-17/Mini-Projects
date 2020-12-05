a = []
for i in range(100):
	for j in range(100):
		b = i**j
		a.append(str(b))
d = []
for i in range(len(a)):
	c = 0
	for k in range(len(a[i])):
		c+=int(a[i][k])
	d.append(c)
print(max(d))