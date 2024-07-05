num = int(input())
box = [[0] * 202 for _ in range(202)]

for turn in range(num):
    x1, y1, x2, y2 = list(map(int,input().split()))
    x1 += 100
    y1 += 100
    x2 += 100
    y2 += 100
    if turn%2 == 0:
        for i1 in range(x1,x2):
            for i2 in range(y1,y2):
                box[i2][i1] = 1

    else:
        for i3 in range(x1,x2):
            for i4 in range(y1,y2):
                box[i4][i3] = 2

total_cnt = 0

for i5 in range(202):
    for i6 in range(202):
        if box[i6][i5] == 2:
            total_cnt += 1
print(total_cnt)