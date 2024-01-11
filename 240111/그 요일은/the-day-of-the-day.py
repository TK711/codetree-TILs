m1, d1, m2, d2 = input().split()
m1, d1, m2, d2 = int(m1), int(d1), int(m2), int(d2)
mat_day = input()

num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
name_of_days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

count = 0
today = 0

# if m1 > m2 or (m1 == m2 and d1 > d2):  # if m1d1 is later than m2d2
#     m1, m2 = m2, m1
#     d1, d2 = d2, d1
#     today = (today - (d1 % 7) + 7) % 7  # adjust the starting day

if not (m1 > m2 or (m1 == m2 and d1 > d2)):  # if m1d1 is later than m2d2
    while not (m1 == m2 and d1 == d2):
        if name_of_days[today] == mat_day:
            count += 1
        d1 += 1
        today = (today + 1) % 7

        if d1 > num_of_days[m1]:
            m1 += 1
            d1 = 1

    if name_of_days[today] == mat_day:
        count += 1
else:
    while not (m1 == m2 and d1 == d2):
        #print("m1, d1, m2, d2",m1, d1, m2, d2)
        if name_of_days[today] == mat_day:
            count += 1
        d1 -= 1
        today = (today + 1) % 7

        if d1 < 1:
            m1 -= 1
            d1 = num_of_days[m1]

    if name_of_days[today] == mat_day:
        count += 1

print(count)