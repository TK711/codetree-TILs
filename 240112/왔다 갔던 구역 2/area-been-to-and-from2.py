lst = [0] * 202
mid = 100
count = 0

num = int(input())

for i in range(num):
    a, b = input().split()
    a = int(a)

    if b == 'L':
        for i in range(a):
            mid -= 1
            lst[mid] += 1
    else:
        for i in range(a):
            mid += 1
            lst[mid] += 1
    
for j in lst:
    if j>=2:
        count += 1

print(count)