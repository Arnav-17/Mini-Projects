a = []
"""Problem is to find the number having longest collatz chain below 1 million"""


def collatz(n):
    counter = 0
    while n > 1:
        if n % 2 == 1:
            n = 3 * n + 1
            counter += 1
        elif n % 2 == 0:
            n = n / 2
            counter += 1
    return counter


largest_number = 0
large_seq = 0

for i in range(1000000, 1, -1):
    a = collatz(i)
    if a > large_seq:
        largest_number = i
        large_seq = a

print(largest_number)
