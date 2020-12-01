single_digits = 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'
double_digits = 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'
triple_digits = 'hundred'
unique_nums = 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'
b = []
for j in range(1001):
    b.append(str(j))

"""The problem 17 is to add words of numbers 1 to 1000 and find the letters of that final word. 

This function converts number to word for numbers 1 to 1000"""


def Covert_to_words(n):
    a = str(n)
    if len(a) == 1:
        for i in range(1, 10):
            if i < 10:
                if a == b[i]:
                    return single_digits[i-1]
    elif len(a) == 2:
        for i in range(11, 20):
            if a == b[i]:
                return unique_nums[i-11]
        for i in range(2, 10):
            for k in range(1, 10):
                if a == b[int(str(i)+str(k))]:
                    return double_digits[i-1] + single_digits[k - 1]
        for i in range(1, 10):
            for k in range(9):
                if a == b[int(str(i)+str(k))]:
                    return double_digits[i-1]
    elif len(a) == 3:
        for i in range(1, 10):
            for k in range(1, 10):
                for l in range(1, 10):
                    if k == 1:
                        if a == b[int(str(i)+str(k)+str(l))]:
                            return single_digits[i-1] + 'hundredand' + unique_nums[l-1]
                    else:
                        if a == b[int(str(i)+str(k)+str(l))]:
                            return single_digits[i-1] + 'hundredand' + double_digits[k-1] + single_digits[l-1]
                for l in range(9):
                    if l == 0:
                        if a == b[int(str(i) + str(k) + str(l))]:
                            return single_digits[i-1] + 'hundredand' + double_digits[k-1]
            for k in range(9):
                if k == 0:
                    for l in range(1, 10):
                        if a == b[int(str(i) + str(k) + str(l))]:
                            return single_digits[i-1] + 'hundredand' + single_digits[l-1]
            for k in range(9):
                for l in range(9):
                    if k == 0 and l == 0:
                        if a == b[int(str(i) + str(k) + str(l))]:
                            return single_digits[i-1] + 'hundred'

    elif len(a) == 4:
        return 'onethousand'


d = ''
for m in range(1, 1001):
    d += Covert_to_words(m)
print(len(d))
