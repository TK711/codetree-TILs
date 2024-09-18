# 1. 각 자리마다 찾아서 바꾸기
# 2. 각 숫자별로 위치 지정하고 그 두개만 바꾸기

n, m = list(map(int,input().split()))

# 지도
mp = []

# 방향 [y, x]
dire = [[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1]]

for _ in range(n):
    lst = list(map(int,input().split()))
    mp.append(lst)

# 매 턴마다
for turn in range(m):
    # 모든 숫자 찾기
    for num in range(1,n*n+1):
        # 각 num의 x, y 위치
        loc_y, loc_x = 0, 0
        # 2차원에서 num 찾기
        # 맞으면 break 아니면 pass
        for i in range(n):
            for j in range(n):
                if mp[i][j] == num:
                    loc_y, loc_x = i, j
                    break
                else:
                    continue
        # print(f'num {num} loc_y {loc_y} loc_x {loc_x}')
        # 8방향 탐색
        # 가장 큰 값 위치 확인
        comp, change_y, change_x = 0, 0,0
        for snr in range(8):
            check_y = loc_y + dire[snr][0]
            check_x = loc_x + dire[snr][1]
            if 0 <= check_y < n and 0 <= check_x < n:
                # 주변 수 중 가장 큰 수랑 교체
                if mp[check_y][check_x] > comp:
                    comp = mp[check_y][check_x]
                    change_y, change_x = check_y, check_x
        # if 큰 수 존재 시, 교체한다.
        # if comp != 0:
        mp[change_y][change_x] = num
        mp[loc_y][loc_x] = comp
    for ch in range(n):
        print(*mp[ch])