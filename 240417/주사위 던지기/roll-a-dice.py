# up right down left (clockwise)
dice = [[0,5,0],
        [4,6,3],
        [0,2,0]]


vertical = [2,6,5,1] # down => [1,2,6,5], up => [6,5,1,2]
horizontal = [4,6,3,1] # left => [1,4,6,3], right => [6,3,1,4]

n, m, r, c = map(int,input().split())
orders = list(input().split())

mp = list([0] * (n+1) for _ in range(n+1))
mp[r][c] = 6
curr_num = 6
curr_y = r
curr_x = c
for order in orders:
    if order == 'U':
        if 0 < curr_y -1 < n+1:
            dice[2][1] = dice[1][1]
            dice[1][1] = dice[0][1]
            dice[0][1] = 7 - dice[2][1]
            curr_num = dice[1][1]
            curr_y -= 1
        else:
            continue

    elif order == 'R':
        if 0 < curr_x + 1 < n + 1:
            dice[1][0] = dice[1][1]
            dice[1][1] = dice[1][2]
            dice[1][2] = 7 - dice[1][0]
            curr_num = dice[1][1]
            curr_x += 1
        else:
            continue


    elif order == 'D':
        if 0 < curr_y + 1 < n+1:
            dice[0][1] = dice[1][1]
            dice[1][1] = dice[2][1]
            dice[2][1] = 7 - dice[0][1]
            curr_num = dice[1][1]
            curr_y += 1
        else:
            continue

    elif order == 'L':
        if 0 < curr_x - 1 < n + 1:
            dice[1][2] = dice[1][1]
            dice[1][1] = dice[1][0]
            dice[1][0] = 7 - dice[1][2]
            curr_num = dice[1][1]
            curr_x -= 1
        else:
            continue

    mp[curr_y][curr_x] = curr_num

tot = 0
for x in range(n+1):
    for y in range(n+1):
       tot += mp[x][y]
print(tot)