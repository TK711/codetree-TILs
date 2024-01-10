d, h, m = input().split()
d, h, m = int(d), int(h), int(m)

if d <11:
    print(-1)
elif d == 11 and h<11:
    print(-1)
elif d == 11 and h==11 and c<11:
    print(-1)
else:
    start = 11* 24* 60 + 11*60 + 11
    passed = d* 24* 60 + h*60 + m
                
    print(passed-start)