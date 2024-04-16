n,m,r,c = map(int,input().split())
lst = list([0] * (n+1) for _ in range(n+1))
new_lst = list([0] * (n + 1) for _ in range(n+1))
dire = [[1,0],[-1,0],[0,1],[0,-1]]

lst[r][c] = 1

for t in range(m):
    for x in range(n+1):
        for y in range(n+1):
            if lst[y][x] == 1:
                for dr in dire:
                    nx = x + dr[0] * (2 ** t)
                    ny = y + dr[1] * (2 ** t)
                    if 0 < nx < n + 1 and 0 < ny < n + 1:
                        new_lst[ny][nx] = 1
    for x in range(n+1):
        for y in range(n+1):
            if lst[x][y] == 0:
                lst[x][y] = new_lst[x][y]

cnt = 0
for x in range(n+1):
    for y in range(n+1):
        if lst[y][x] == 1:
            cnt += 1

print(cnt)