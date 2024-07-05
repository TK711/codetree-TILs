num = int(input())

lst = [0] * 2001

pivot = 1000

for i in range(num):
    n, dire = input().split()
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
tot = 0
cnt = 0
prev = False
for k in range(2001):
    if lst[k] > 1:
        tot += 1
        if prev == False:
            prev = True
            cnt +=1
    else:
        prev = False

print(tot-cnt)