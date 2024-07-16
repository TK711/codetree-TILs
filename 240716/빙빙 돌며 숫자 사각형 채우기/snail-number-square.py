n,m = list(map(int,input().split()))

# lst = checker
lst = [[0] * m for _ in range(n)]
# show = actural list
show = [[0] * m for _ in range(n)]
# for direction, right, down, left, up
dir_x = [1,0,-1,0]
dir_y = [0,1,0,-1]

x, y = 0, 0
dire = 0
# initalizing first point
lst[y][x]=1
show[y][x] = 1
# from 2nd point to last point
for num in range(2,(n * m) +1):
    n_x = x + dir_x[dire]
    n_y = y + dir_y[dire]
    # check if in range or visited
    if 0 <= n_x < m and 0 <= n_y < n and lst[n_y][n_x] == 0:
        pass
    # else, turn by adding 1 and divide it by 4
    else:
        dire = (dire+1)%4

    x = x + dir_x[dire]
    y = y + dir_y[dire]
    # mark visited and get num in show
    lst[y][x] += 1
    show[y][x] = num

for rw in show:
    print(*rw)