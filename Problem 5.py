import functools as fn
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def lcmm(*args):
    return fn.reduce(lcm, args)
print(lcmm(*range(1,21)))