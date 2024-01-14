rep = int(input())



count = 0

#print(lst)
#print(lst[1],lst[1][2])

leng = 201
lst = [[0] * leng for _ in range(leng)]

for i in range(rep):


    a1, b1, a2, b2 = input().split()
    a1, b1, a2, b2 = 100 + int(a1),100 + int(b1),100 + int(a2),100 + int(b2)

    for i in range(a1, a2):
        for j in range(b1, b2):
            lst[i][j] = 1

for i in range(leng):
    for j in range(leng):
        if lst[i][j] >= 1:
            count += 1

print(count)