month, day, t_month, t_day = input().split()

month, day, t_month, t_day = int(month), int(day), int(t_month), int(t_day)

elapsed_days = 1  # t_day +1 is not in func

#                  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    if month == t_month and day == t_day:
        break

    elapsed_days += 1
    day += 1

    if day > num_of_days[month]:
        month += 1
        day = 1

print(elapsed_days)