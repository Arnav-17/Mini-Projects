a = ['0', '1']
for i in range(2, 10000):
	b = int(a[i-1]) + int(a[i-2])
	a.append(str(b))
	if len(a[i]) == 1000:
		print(i)
		break
