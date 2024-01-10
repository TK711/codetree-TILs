d, h, m = input().split()
d, h, m = int(d), int(h), int(m)
a, b, c = 11, 11, 11
if d<= 11 and h <11 and m<11:
    print("-1")
else:
    elasped_time = 0

    while True:
        if a == d and b == h and c == m:
            break
        elasped_time += 1
        c += 1
        if c == 60:
            b += 1
            c = 0
        
        if b == 24:
            a += 1
            b = 0
        
            
    print(elasped_time)