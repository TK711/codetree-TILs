N = int(input())
lst = []

for _ in range(N):
    lst.append(list(map(int,input().split())))
leng = len(lst)
y, x = map(int, input().split())

y -= 1
x -= 1

rng = lst[y][x]

dlt = [[1,0],[-1,0],[0,1],[0,-1],[0,0]]

for i in dlt:
    for r in range(1,rng):
        n_y = y + i[0] * r
        n_x = x + i[1] * r
        if 0 <= n_y < leng and  0 <= n_x < leng:
            lst[n_y][n_x] = 0


for col in range(leng):
    lst_col = []
    for row in range(leng):
        if not lst[row][col] == 0:
            lst_col.append(lst[row][col])
    if leng != len(lst_col):
        for _ in range(leng - len(lst_col),0,-1):
            lst_col.insert(0,0)
    for rw in range(leng):
        lst[rw][col] = lst_col[rw]

for rows in lst:
    for it in rows:
        print(it,end = ' ')
    print()