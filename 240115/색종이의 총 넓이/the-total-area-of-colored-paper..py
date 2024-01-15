count = 0

lst = [[0]*200 for _ in range(200)]

num = int(input())

#lst = lst = [[0 for _ in range(leng)] for _ in range(leng)]



for i in range(num):
    x,y  = input().split()
    x, y =int(x)+100, int(y)+100

    for i in range(x,x+8):
        for j in range(y,y+8):
            lst[i][j] = 1


for i in range(200):
    for j in range(200):
        if lst[i][j] >= 1:
            count += 1

print(count)