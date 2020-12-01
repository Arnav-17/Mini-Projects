a = []
for i in range(10, 100):
	for j in range(10, 100):
		if i%10 !=0 and j %10 !=0:
			if str(i)[0] == str(j)[0]:
				if i/j < 1:
					a = int(str(i)[1])
					b = int(str(j)[1])
					if a/b == i/j:
						print(i,j)
			if str(i)[0] == str(j)[1]:
				if i/j < 1:
					a = int(str(i)[1])
					b = int(str(j)[0])
					if a/b == i/j:
						print(i,j)

			if str(i)[1] == str(j)[0]:
				if i/j < 1:
					a = int(str(i)[0])
					b = int(str(j)[1])
					if a/b == i/j:
						print(i,j)

			if str(i)[1] == str(j)[1]:
				if i/j < 1:
					a = int(str(i)[0])
					b = int(str(j)[0])
					if a/b == i/j:
						print(i,j)


			