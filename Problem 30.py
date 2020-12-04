i = 2
b = 0
"""i cannot have more than 7 digits because sum of 5th power digits of a 7 digit number 
cannot be more than 413343. Because 9^5*6 = 413343"""
while len(str(i)) < 7:
	a = 0
	for j in range(len(str(i))):
		a += int(str(i)[j])**5
	if i == a:
		b+=i
	i+=1
print(b)