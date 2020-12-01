def prime_fac(n):
    i = 1
    a = []
    while i <= n:
        k = 0
        if n % i == 0:
            j = 1
            while j <= i:
                if i % j == 0:
                    k = k+1
                j = j+1
            if k == 2:
                a.append(i)
        i = i+1
    return a


for l in range(2, 200000):
    c = prime_fac(l)
    d = prime_fac(l+1)
    e = prime_fac(l+2)
    f = prime_fac(l+3)
    if len(c) == len(d) and len(c) == 4 and len(e) == 4 and len(f) == 4:
        if c != d and c != e and c != f and d != e and d != f and e != f:
            print(l, l+1, l+2, l+3)