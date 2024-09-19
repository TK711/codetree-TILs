# T 턴 동안
# 각 구슬마다 시작방향을 판에 기록, 바뀌면 변경
# 새로 판 하나 더 작성
# 만약 같은 지점에 만나면 삭제(0으로)

t = int(input())

# U, R, D, L
dire = [[-1,0], [0,1],  [1,0], [0,-1] ]
ans = []

for turns in range(t):
    cnt = 0
    n, m = list(map(int, input().split()))
    mp1 = [[0] * n for _ in range(n)]
    mp2 = [[0] * n for _ in range(n)]

    # for k in range(n):
    #     print(mp1[k])
    # print()

    for _ in range(m):
        y, x, d = list(input().split())
        y, x = int(y)-1, int(x)-1
        if d == 'U':
            mp1[y][x] = 1
        elif d == 'R':
            mp1[y][x] = 2
        elif d == 'D':
            mp1[y][x] = 3
        elif d == 'L':
            mp1[y][x] = 4

    # print("start")
    # for k in range(n):
    #     print(mp1[k])

    # n^2 번만큼 실행
    for _ in range(n**2):
        for y1 in range(n):
            for x1 in range(n):
                # 0이면 바로 다음으로
                if mp1[y1][x1] == 0:
                    continue
                # 방향으로 1칸 이동
                else:
                    pos = mp1[y1][x1]
                    n_y1 = y1 + dire[pos-1][0]
                    n_x1 = x1 + dire[pos-1][1]

                    # 범위 밖으로 가면 반대 방향으로
                    if 0 <= n_y1 < n and 0 <= n_x1 < n:
                        # 겹치면 0으로
                        if mp2[n_y1][n_x1] == 0:
                            mp2[n_y1][n_x1] = pos
                        else:
                            mp2[n_y1][n_x1] = 99
                    else:
                        mp2[y1][x1] =(pos + 1)%4 +1
                        
        # 중복 제거
        for y2 in range(n):
            for x2 in range(n):
                if mp2[y2][x2] == 99:
                    mp2[y2][x2] = 0
        # print()
        # for k in range(n):
        #    print(mp2[k])
        
        # 지도 교체
        for y3 in range(n):
            for x3 in range(n):
                mp1[y3][x3] = mp2[y3][x3]
                mp2[y3][x3] = 0

    # print()
    # print("finished")
    # for k in range(n):
    #     print(mp2[k])
    # print()
    for y3 in range(n):
        for x3 in range(n):
            if mp1[y3][x3] != 0:
                cnt += 1
    ans.append(cnt)
for count in ans:
    print(count)