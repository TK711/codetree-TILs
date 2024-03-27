map = [list(map(int,input().split())) for _ in range(4)]
dir = input()

# L = 좌로 한칸씩
# R = 우로 한칸씩
# U = 위로 한칸씩
# D = 밑으로 한칸씩

# 0이면 무시하고 이동
# 같은 수 만나면 합

if dir == 'U':
    for i in range(4):
        temp = []
        for j in range(4):
            if map[j][i] != 0:
                temp.append(map[j][i])
            map[j][i] = 0
        for k in range(len(temp)):
            map[k][i] = temp[k]
    # make *2 and 0
    for l in range(4):
        for m in range(3):
            if map[m][l] == map[m + 1][l]:
                map[m][l] *= 2
                map[m + 1][l] = 0
    # push up
    for i in range(4):
        temp = []
        for j in range(4):
            if map[j][i] != 0:
                temp.append(map[j][i])
            map[j][i] = 0
        for k in range(len(temp)):
            map[k][i] = temp[k]

# D finished
elif dir == 'D':
    # pushdown
    for i in range(4):
        temp = []
        for j in range(3,-1,-1):
            if map[j][i] != 0:
                temp.append(map[j][i])
            map[j][i] = 0
        for k in range(len(temp)):
            map[3-k][i] = temp[k]
    # *2 and make 0
    for l in range(4):
        for m in range(3, -1, -1):
            if map[m][l] == map[m - 1][l]:
                map[m][l] *= 2
                map[m - 1][l] = 0
    # re:pushdown
    for i in range(4):
        temp = []
        for j in range(3,-1,-1):
            if map[j][i] != 0:
                temp.append(map[j][i])
            map[j][i] = 0
        for k in range(len(temp)):
            map[3-k][i] = temp[k]
elif dir == 'L':
    for i in range(4):
        temp = []
        for j in range(4):
            if map[i][j] != 0:
                temp.append(map[i][j])
            map[i][j] = 0
        for k in range(len(temp)):
            map[i][k] = temp[k]
    # *2 and make 0
    for l in range(4):
        for m in range(2):
            if map[l][m] == map[l][m+1]:
                map[l][m] *= 2
                map[l][m+1] = 0
    # push left
    for i in range(4):
        temp = []
        for j in range(4):
            if map[i][j] != 0:
                temp.append(map[i][j])
            map[i][j] = 0
        for k in range(len(temp)):
            map[i][k] = temp[k]


elif dir == 'R':
    for i in range(4):
        temp = []
        for j in range(4):
            if map[i][j] != 0:
                temp.append(map[i][j])
            map[i][j] = 0
        # print(temp)
        for k in range(len(temp)):
            map[i][3-k] = temp[len(temp)-k-1]
    # *2 and make 0
    for l in range(4):
        for m in range(3, 0, -1):
            if map[l][m] == map[l][m-1]:
                map[l][m] *= 2
                map[l][m-1] = 0
    # push right
    for i in range(4):
        temp = []
        for j in range(4):
            if map[i][j] != 0:
                temp.append(map[i][j])
            map[i][j] = 0
        # print(temp)
        for k in range(len(temp)):
            map[i][3-k] = temp[len(temp)-k-1]
# 이동 끝
# 각 방향의 끝부터 하나씩 이동하며 중복 시 앞의 값 *2 뒤의 값 0
# 종료 후 다시 이동
# print()
for i in map:
    print(*i)