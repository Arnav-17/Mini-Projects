days = 0
a = 0
b = []
for year in range(1901, 2001):
    if year % 4 == 0:
        for month in range(1, 13):
            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                for date in range(1, 32):
                    days += 1
                    a = days % 7
                    if date == 1 and a == 6:
                        b.append(date)
            elif month == 4 or month == 6 or month == 9 or month == 11:
                for date in range(1, 31):
                    days += 1
                    a = days % 7
                    if date == 1 and a == 6:
                        b.append(date)
            else:
                for date in range(1, 30):
                    days += 1
                    a = days % 7
                    if date == 1 and a == 6:
                        b.append(date)
    else:
        for month in range(1, 13):
            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                for date in range(1, 32):
                    days += 1
                    a = days % 7
                    if date == 1 and a == 6:
                        b.append(date)
            elif month == 4 or month == 6 or month == 9 or month == 11:
                for date in range(1, 31):
                    days += 1
                    a = days % 7
                    if date == 1 and a == 6:
                        b.append(date)
            elif month == 2:
                for date in range(1, 29):
                    days += 1
                    a = days % 7
                    if date == 1 and a == 6:
                        b.append(date)
print(len(b))