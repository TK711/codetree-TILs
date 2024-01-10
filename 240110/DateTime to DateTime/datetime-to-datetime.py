d, h, m = input().split()
d, h, m = int(d), int(h), int(m)

tot = d* 24* 60 + h*60 + m - (11* 24* 60 + 11*60 + 11)

if tot<0:
    print("-1")
else:
    print(tot)