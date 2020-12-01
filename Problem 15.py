"""Problem is to calculate ways to go from top left of grid to bottom right of grid 20*20
Formula used is C(n, r) = n!/(r!*(n-r)!)
"""


def fact(n):
    a = 1
    for i in range(1, n+1):
        a *= i
    return a


def Comb(n, r):
    b = fact(n)/(fact(r)*fact(n-r))
    return int(b)


print(Comb(10, 1))