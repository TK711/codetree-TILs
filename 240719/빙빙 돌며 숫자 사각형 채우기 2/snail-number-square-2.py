n, m = list(map(int,input().split()))

dx = [0,1,0,-1]
dy = [1,0,-1,0]
dire = 0

lst = [[0] * m for _ in range(n)]
visted = [[0] * m for _ in range(n)]

x, y = 0, 0
visted[y][x] = 1

num = 1
lst[y][x] = num
mul = n * m

for _ in range(mul-1):
    new_x = x + dx[dire]
    new_y = y + dy[dire]
    if 0 <= new_x < m and 0 <= new_y < n and visted[new_y][new_x] == 0:
        pass
    else:
        dire = (dire + 1)%4
    x = x + dx[dire]
    y = y + dy[dire]
    visted[y][x] = 1
    num += 1
    lst[y][x] = num

for k in lst:
    print(*k)