# 1 = / and 2 = \
# 1 = right and down, left and up /
# 2 = right and up, left and down \


#        up    down  right  left
# dire = [[1,0],[-1,0],[0,1],[0,-1]]
def pinball(y,x,dr,time):
    # print(f'y, {y} x, {x} dr, {dr} time {time}')
    global mx
    if mp[y][x] == 0:
        pass
    elif mp[y][x] == 1:
        if dr == 0:
            dr = 2
        elif dr == 1:
            dr = 3
        elif dr == 2:
            dr = 0
        elif dr == 3:
            dr = 1
    elif mp[y][x] == 2:
        if dr == 0:
            dr = 3
        elif dr == 1:
            dr = 2
        elif dr == 2:
            dr = 1
        elif dr == 3:
            dr = 0

    # go 1 step and check
    if 0 <= y + dire[dr][0] < size and 0 <= x + dire[dr][1] < size:
        # inside
        pinball(y + dire[dr][0], x + dire[dr][1], dr, time +1)
    else:
        # outside
        # break
        if time > mx:
            mx = time
        return


size = int(input())
mp = list(list(map(int, input().split())) for _ in range(size))


dire = [[-1,0],[1,0],[0,1],[0,-1]]
mx = 0

mx = 0
time = 0
# top
for i in range(size):
    a = 0
    b = 0
    pinball(a,b + i,1,1)

# left side
for i in range(size):
    a = 0
    b = 0
    pinball(a+i, b,2,1)

# right side
for i in range(size):
    a = 0
    b = size-1
    pinball(a + i, b, 3, 1)

# bottom side
for i in range(size):
    a = size-1
    b = 0
    pinball(a, b + i, 0, 1)

# 시작점에서 한 방향으로 계속 이동, 1, 2 만나면 방향 전환
# 점에서 방향으로 이동, 범위 내면 계속 이동,

print(mx+1)