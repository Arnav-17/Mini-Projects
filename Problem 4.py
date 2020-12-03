def Pal(n):
	for i in range(len(str(n))):
		if str(n)[i] != str(n)[len(str(n))-1-i]:
			break
	else:
		return 'yay'
a = []
for i in range(100, 1000):
	for j in range(100,1000):
		b = i*j
		if Pal(b) =='yay':
			a.append(b)
print(max(a))