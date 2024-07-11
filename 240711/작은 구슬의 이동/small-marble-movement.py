n, t = list(map(int, input().split()))
r, c, d = input().split()
r = int(r) - 1
c = int(c) - 1

lst = [[0 for _ in range(n)] for _ in range(n) ]

dx = [0,1,-1,0]
dy = [1,0,0,-1]
dire = {'D':0,'L':1,'R':2,'U':3}
direction = dire[d]
for _ in range(t):    
    nc, nr = c + dx[direction], r + dy[direction]
    if nr < 0 or nr >= n:
        direction = abs(3-direction)
    elif nc < 0 or nc >= n:
        direction = abs(3-direction)
    else:
        r, c = nr,nc
    # print(r,c)
print(r+1,c+1)