lst = []
# t0 check 3 angle, to right, 45 right-down, down
dire_x = [1,1,0]
dire_y = [0,1,1]
comp_win = 0
loc_x = 0
loc_y = 0
for _ in range(19):
    lt = list(input().split())
    lst.append(lt)

# run every point of Omok plate
for y in range(19):
    for x in range(19):
        comp = 0
        if lst[y][x] != "0":
            comp = lst[y][x]
            # check 3 angle, to right, 45 right-down, down
            for dr in range(3):
                flg = True
                # check 4 positions of same direction
                for nxt in range(1,5):
                    new_x = x + dire_x[dr] * nxt
                    new_y = y + dire_y[dr] * nxt
                    # if in range and got same number
                    if new_x < 19 and new_y < 19 and lst[new_y][new_x]==comp:
                        continue
                    else:
                        flg = False
                        break
                # if got one
                if flg == True:
                    comp_win = comp
                    loc_x = x + dire_x[dr] * 2
                    loc_y = y + dire_y[dr] * 2
                    break
        else:
            continue
if comp_win == 0:
    print(comp_win)
else:
    print(comp_win)
    print(loc_y+1,loc_x+1)