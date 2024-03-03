import copy
N = int(input())
tst = []
cpy = list([0] * N for _ in range(N))
dlt = [[1,0],[-1,0],[0,1],[0,-1],[0,0]]
mx = 0
for _ in range(N):
    tst.append(list(map(int,input().split())))
# print(tst)
vis = list([0] * N for _ in range(N))
# 각 점
for i in range(N):
    for j in range(N):
        lst = copy.deepcopy(tst)
        for a in range(N):
            for b in range(N):
                cpy[a][b] = tst[a][b]
        # print('tst',tst)
        # print('lst',lst)
        # 각 점별 폭파 & 결과
        rng = lst[i][j]
        # print('rng',rng)
        for k in dlt:
            for rn in range(0,rng):
                n_y = i + k[0]*(rn)
                n_x = j + k[1] * (rn)
                # print('n_y, n_x',n_y, n_x)
                if 0 <= n_y < N and 0 <= n_x < N:
                    lst[n_y][n_x] = 0
        for col in range(N):
            new_col = [0] * N

            n_rw = 0
            for row in range(N-1,-1,-1):
                if lst[row][col] != 0:
                    new_col[n_rw] = lst[row][col]
                    n_rw += 1
            # print('new_coln',new_col)
            for nrow in range(N-1,-1,-1):
                lst[nrow][col] = new_col[N - 1 - nrow]
            # print('after')
            # print('fin')
        cnt = 0
        for l in range(N):
            for m in range(N):
                if lst[l][m] == 0:
                    continue
                if 0 <= l + dlt[0][0] < N and 0 <= m + dlt[0][1] < N:
                    if lst[l][m] == lst[l + dlt[0][0]][m + dlt[0][1]]:
                        cnt += 1
                        # print('l,m',l,m, lst[l][m],lst[l + dlt[0][0]][m + dlt[0][1]])
                if 0 <= l + dlt[2][0] < N and 0 <= m + dlt[2][1] < N:
                    if lst[l][m] == lst[l + dlt[2][0]][m + dlt[2][1]]:
                        cnt += 1
                        # print('l,m 2',l,m,lst[l][m], lst[l + dlt[2][0]][m + dlt[2][1]])
        # print('cnt',cnt)
        if cnt > mx:
            mx = cnt

print(mx)