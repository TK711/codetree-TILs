lst = [0] * 202
mid = 100
count = 0
count2 = 0
prev = 0
prev_dir = None
#시작점과 끝점에도 +1 필요
flag = False

num = int(input())

for i in range(num):
    a, b = input().split()
    a = int(a)
    if prev_dir != b:
        lst[mid] += 1
    prev_dir = b
    if b == 'L':
        for i in range(a):

            mid -= 1
            lst[mid] += 1

    else:
        for i in range(a):
            mid += 1
            lst[mid] += 1



for j in lst:
    #print(flag)
    #print(count)

    if j >= 2:
        if flag == True:
            count += 1
        else:
            flag = True

    else: # j가 0보다 작음
        if flag == True:
            flag = False
            count2 += count
            count = 0

print(count2)