num = int(input())

lst = [0] * 2001

pivot = 1000
previous = "A"
for i in range(num):
    n, dire = input().split()
    if previous == dire:
        if dire == "R":
            for _ in range(int(n)):
                pivot += 1
                lst[pivot] += 1

        else:
            for _ in range(int(n)):
                pivot -= 1
                lst[pivot] += 1
    else:
        if dire == "R":
            lst[pivot] += 1
            for _ in range(int(n)):
                pivot += 1
                lst[pivot] += 1

        else:
            lst[pivot] += 1
            for _ in range(int(n)):
                pivot -= 1
                lst[pivot] += 1
    previous = dire

# find range and subtract it. check bigger than 1 and find end.
# if end is finished, subtract it anyway.
prev = False
start = 0
fin = 0
tot = 0
for k in range(2001):
    if lst[k] > 1:
        if prev == False:
            start = k
            prev = True
    else:
        if prev == True:
            tot += abs(start - (k-1))
            prev = False
            start = 0
print(tot)