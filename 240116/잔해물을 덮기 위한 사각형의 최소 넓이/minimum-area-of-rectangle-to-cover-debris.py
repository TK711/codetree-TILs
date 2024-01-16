rec1 = list(input().split())
rec2 = list(input().split())

cnt = 0
lst3 = []
# change 21 to 2001
cor = list([0]*2001 for _ in range(2001))

for x1 in range(int(rec1[0])+1000,int(rec1[2])+1001):
    for y1 in range(int(rec1[1])+1000, int(rec1[3])+1001):
        cor[x1][y1] = 1

for x2 in range(int(rec2[0])+1000,int(rec2[2])+1001):
    for y2 in range(int(rec2[1])+1000, int(rec2[3])+1001):
        cor[x2][y2] = 0

for x3 in range(2001):
    for y3 in range(2001):
        if cor[x3][y3] == 1:
            lst3.append([x3,y3])
if lst3 != []:
    print((max(lst3, key=lambda x: x[0])[0] - min(lst3, key=lambda x: x[0])[0]) * (max(lst3, key=lambda x: x[1])[1] - min(lst3, key=lambda x: x[1])[1]))
else:
    print(0)