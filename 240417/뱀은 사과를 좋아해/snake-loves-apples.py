n, m, k = map(int, input().split())

mp = [[0] * (n + 1) for _ in range(n + 1)]
dire = {'U': [-1, 0], 'D': [1, 0], 'L': [0, -1], 'R': [0, 1]}
snake_len = 0

# snake moves with it's length
# mark with it's length and subtract 1 before move
# move and mark it's length
# if meet apple, +1 on every mark on map

for _ in range(m):
    y, x = map(int, input().split())
    mp[y][x] = -1

orders = list(input().split() for _ in range(k))
flag = True
mv_y,mv_x = 1, 1
cnt = 0
mp[mv_y][mv_x] = 0


for idx, order in enumerate(orders):
    # print(order[0])
    dr = dire[order[0]]
    for _ in range(int(order[1])):
        cnt += 1
        mv_y += dr[0]
        mv_x += dr[1]

        # print(f'x {mv_x} y {mv_y}')
        if 0 < mv_x < (n + 1) and 0 < mv_y < (n + 1):
            # print(f'passed x {mv_x} y {mv_y}')
            if mp[mv_y][mv_x] == 0:
                for y in range(n+1):
                    for x in range(n+1):
                        if mp[y][x] != 0 and mp[y][x] != -1:
                            mp[y][x] -= 1
                mp[mv_y][mv_x] = snake_len

            elif mp[mv_y][mv_x] == -1:
                snake_len += 1
                mp[mv_y][mv_x] = snake_len
            else:
                flag = False
                # print('break!')
                break
        else:
            flag = False
            # print('break!')
            break
        # print()
        # for k in mp:
            # print(k)
    if flag == False:
        break

print(cnt)