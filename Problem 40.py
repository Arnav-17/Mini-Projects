a = str(0.1)
for i in range(2, 1000001):
	b = str(i)
	a += b
a +=str(1)
print(int(a[2])*int(a[11])*int(a[101])*int(a[1001])*int(a[10001])*int(a[100001])*int(a[1000001]))
