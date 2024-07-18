n = int(input())
lst = []

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def checker(x,y,dire):
    if lst[y][x] == "/":
        if dire == 0:
            dire = 3
        elif dire == 1:
            dire = 2
        elif dire == 2:
            dire = 1
        else:
            dire = 0
    else:
        if dire == 0:
            dire = 2
        elif dire == 1:
            dire = 3
        elif dire == 2:
            dire = 0
        else:
            dire = 1
    return dire


for _ in range(n):
    inp = list(input())
    lst.append(inp)

k = int(input())

if k-1 < n:
# down
    x = k-1
    y = 0
    dire = 2
elif k-1 < 2*n:
# left
    x = n-1
    y = k-n-1
    dire = 0
elif k-1 < 3*n:
# up
    x = 3*n - k
    y = n-1
    dire = 3
else:
# right
    x = 0
    y = 4*n - k
    dire = 1

cnt = 1
checking = [[0] * n for _ in range(n)]
checking[y][x] = 1
dire = checker(x,y,dire)

while True:
# for _ in range(4):
    new_x = x + dx[dire]
    new_y = y + dy[dire]

    if 0 <= new_x < n and 0 <= new_y < n:
        dire = checker(new_x,new_y,dire)
        checking[new_y][new_x] = 1
        cnt += 1
        x = new_x
        y = new_y
    else:
        break

print(cnt)