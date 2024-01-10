d, h, m = input().split()
d, h, m = int(d), int(h), int(m)

start = 11* 24* 60 + 11*60 + 11
passed = d* 24* 60 + h*60 + m
            
print(passed-start)