def Fib(n):
	if n>2:
		return Fib(n-1) + Fib(n-2)
	elif n == 2:
		return 2
	else:
		return 1
i = 0
x = 0
while Fib(i)<4000000:
	if Fib(i)%2 == 0:
		x+=Fib(i)
	i+=1
print(x)