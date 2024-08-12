# box = [[0]*200001 for _ in range(200001)]
curr_x = 100000
curr_y = 100000

dir_x = [0,1,0,-1]
dir_y = [-1,0,1,0]
dire = 0

dire = 0
lst = input()
for idx, i in enumerate(lst):
    if i == "F":
        new_x = curr_x + dir_x[dire]
        new_y = curr_y + dir_y[dire]
        if 0 < new_x < 200002 and 0 < new_y < 200002:
            curr_x = new_x
            curr_y = new_y
            if curr_x == 100000 and curr_y == 100000:
                ans = idx
    elif i == 'L':
        dire = (dire - 1)%4
    elif i == 'R':
        dire = (dire + 1)%4

if  ans == 0:
    print(-1)
else:
    print(ans+1)