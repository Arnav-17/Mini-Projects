a = []
for i in range(201):
	for j in range(101):
		for k in range(41):
			if (i+2*j + 5*k) % 10 == 0 and i+2*j + 5*k<= 200:
				a.append([i,2*j, 5*k])
"""
Sum of 1p, 2p, 5p must be a factor of 10. This analysis helps in reducing number of steps
"""

b = []
for l in range(len(a)):
	for i in range(21):
		for j in range(11):
			for k in range(5):
				c = a[l][0]+a[l][1]+a[l][2]
				if (c + 10*i+20*j + 50*k) == 100 or (c + 10*i+20*j + 50*k) == 200 or (c + 10*i+20*j + 50*k) == 0:
					b.append([a[l][0],a[l][1],a[l][2], 10*i,20*j,50*k])

""" Sum of amount of coins of 1p, 2p, 5p, 10p, 20p, 50p must be either 0 or 100 or 200. 
Now for every Sum of amount of coins of 1p, 2p, 5p, 10p, 20p, 50p there will be a corresponding 100p.
In simpler words, There is no choice to select 100p.
"""
# appending this list because we left out one element which is no coins but a 2 Euro coin.
b.append([0,0,0,0,0,0])

print(len(b))