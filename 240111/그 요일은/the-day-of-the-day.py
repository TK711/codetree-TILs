m1, d1, m2, d2 = input().split()
m1, d1, m2, d2 = int(m1),int(d1),int(m2),int(d2)
mat_day = input()

#print(m1, d1, m2, d2)

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
name_of_days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
#print(num_of_days[m1])
elasped_day = 0

# m1,d1 = monday
# m2, d2 = ?
#m1 d1 > m2 d2

while not (m1 == m2 and d1 == d2):
    if m1 < m2 or (m1 == m2 and d1 < d2):
        d1 += 1
        elasped_day += 1
        if d1 > num_of_days[m1]:
            m1 += 1
            d1 = 1
    else:
        d1 -= 1
        elasped_day -= 1
        if d1 < 1:
            m1 -= 1
            d1 = num_of_days[m1]

elasped_day = abs(elasped_day)
day = elasped_day//7
remain = elasped_day%7

for idx, i in enumerate(name_of_days):
    if mat_day == i:
        day = idx
if day <= remain:
    day += 1

print(day)