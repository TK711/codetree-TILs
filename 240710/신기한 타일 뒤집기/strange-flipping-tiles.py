num = int(input())

mx = 1000
pivot = 500
lst = [ 0 for _ in range(mx * 2 +1)]

for _ in range(num):
    dist, dire = input().split()
    dist = int(dist)
    for checker in range(dist):
        if dire == "L":
            lst[pivot] = 1
            if checker != dist - 1:
                pivot -= 1
        else:
            lst[pivot] = 2
            if checker != dist - 1:
                pivot += 1

total_white = 0
total_black = 0

for a in lst:
    if a == 1:
        total_white += 1
    elif a == 2:
        total_black += 1
print(total_white, total_black)