"""Answer will take a very long time"""

for k in range(1, 100000000):
    a = []
    x = 0
    for j in range(k):
        x += j
    for i in range(1, x+1):
        if x % i == 0:
            a.append(i)
    if len(a) > 500:
        print(k-1)
        break
