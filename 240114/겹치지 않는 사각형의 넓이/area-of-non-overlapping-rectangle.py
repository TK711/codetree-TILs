#num = int(input())

leng = 21
count = 0
maxx, minx, maxy, miny = 0, leng+1, 0, leng+1

lst = lst = [[0 for _ in range(leng)] for _ in range(leng)]



for i in range(2):
    a1,b1,a2,b2 = input().split()
    a1, b1, a2, b2 = int(a1),int(b1),int(a2),int(b2)

    for i in range(a1,a2):
        for j in range(b1,b2):
            lst[i][j] = 1

a1, b1, a2, b2 = input().split()
a1, b1, a2, b2 = int(a1), int(b1), int(a2), int(b2)
for i in range(a1,a2):
    for j in range(b1,b2):
        lst[i][j] = 0

for i in range(leng):
    for j in range(leng):
        if lst[i][j] >= 1:
            count += 1

print(count)