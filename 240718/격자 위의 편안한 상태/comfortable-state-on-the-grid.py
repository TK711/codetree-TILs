n, m = list(map(int,input().split()))
lst = [[0] * n for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

for _ in range(m):
    tot = 0
    r, c = list(map(int,input().split()))
    r -= 1
    c -= 1
    lst[r][c] = 1
    for i in range(4):
        check_r = r + dy[i]
        check_c = c + dx[i]
        if 0 <= check_c < n and 0 <= check_r < n and lst[check_r][check_c] == 1:
            tot += 1
    if tot >= 3:
        print(1)
    else:
        print(0)