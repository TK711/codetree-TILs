# up right down left (clockwise)
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
            go_up = vertical.pop(0)
            vertical.append(go_up)
            horizontal[1] = vertical[1]
            curr_num = vertical[1]
            curr_y -= 1
        else:
            continue

    elif order == 'R':
        if 0 < curr_x + 1 < n + 1:
            go_right = horizontal.pop(0)
            horizontal.append(go_right)
            vertical[1] = horizontal[1]
            curr_num = horizontal[1]
            curr_x += 1

    elif order == 'D':
        if 0 < curr_y + 1 < n+1:
            go_down = vertical[-1]
            for i in range(3,0,-1):
                vertical[i] = vertical[i-1]
            vertical[0] = go_down
            horizontal[1] = vertical[1]
            curr_num = vertical[1]
            curr_y += 1
        else:
            continue

    elif order == 'L':
        if 0 < curr_x - 1 < n + 1:
            go_left = horizontal[-1]
            for i in range(3, 0, -1):
                horizontal[i] = horizontal[i - 1]
            horizontal[0] = go_left
            vertical[1] = horizontal[1]
            curr_num = horizontal[1]
            curr_x -= 1
        else:
            continue
    mp[curr_y][curr_x] = curr_num

tot = 0
for x in range(n+1):
    for y in range(n+1):
       tot += mp[x][y]
print(tot)