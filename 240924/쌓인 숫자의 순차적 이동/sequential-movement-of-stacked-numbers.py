# 지도의 각 자리는 리스트로 만든다
# 8 방향 탐사 숫자 없으면 패쓰
# 만약 있으면 옮긴 자리 리스트 가장 뒤로 이동
# 다음 이동시대상 숫자부터 가장 위 숫자까지 모두 이동

n, m = list(map(int,input().split()))
mp = [[[0] for _ in range(n)] for _ in range(n)]

for rw in range(n):
    lst = list(map(int,input().split()))
    for idx, num in enumerate(lst):
        mp[rw][idx].append(num)
order = list(map(int,input().split()))

# direction cloclkwise from +1, 0
dire = [[1,0],[1,1],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1]]

for each in order:
    # print("each",each)
    # 각 숫자 있는 위치 찾기
    for i in range(n):
        for j in range(n):
            if each in mp[i][j]:
                st_x, st_y = j, i
                break
            else:
                continue
    # print("st_x, st_y",st_x, st_y)
    # print()

    # 8방향 탐색
    comp, comp_y, comp_x = 0, 0, 0
    for dr in dire:
        # print(dr,dr)
        new_y, new_x = st_y + dr[0], st_x + dr[1]
        # 범위 내일 때
        if 0 <= new_y < n and 0 <= new_x < n:
            # print("new_y, new_x, mp[new_y][new_x]",new_y, new_x, mp[new_y][new_x])
            # 안 비었으면
            if mp[new_y][new_x][-1] != 0:
                # print("mp[new_y][new_x]",mp[new_y][new_x])
                # 8방향중 가장 큰 수인지 확인
                if comp < max(mp[new_y][new_x]):
                    # print(max(mp[new_y][new_x]))
                    comp_y, comp_x = new_y, new_x
                    comp = max(mp[new_y][new_x])
            # 비었으면 다음으로
            else:
                continue

    # # 만약 옆에 숫자가 없으면 다음 숫자로 패쓰
    if comp == 0:
        continue
        
    # print("comp_y, comp_x", comp_y, comp_x, max(mp[comp_y][comp_x]))
    # 현재 위치(st_x,st_y)의 리스트 값들의 끝에서 현재 지정 값(each)까지 리스트 이동
    move = []
    # print("st_y,st_x",st_y,st_x,mp[st_y][st_x])
    # 현재위치의 값 리스트를 역순으로 보면서 하나씩 pop,
    # pop한 값은 move 리스트에 넣고 목표지점에 역순으로 붙인다.
    for pos in range(len(mp[st_y][st_x])-1,-1,-1):
        # print("pos",pos)
        # print("mp[st_y][st_x][pos]",mp[st_y][st_x][pos], pos)
        if each == mp[st_y][st_x][pos]:
            move.append(mp[st_y][st_x].pop())
            break
        else:
            move.append(mp[st_y][st_x].pop())

    # 역순으로 더해준다.
    # print("move[::-1]",move[::-1])
    # for ad in move[::-1]:
    mp[comp_y][comp_x]+=move[::-1]

    

for indx_y in range(n):
    for indx_x in range(n):
        if mp[indx_y][indx_x][-1] == 0:
            print("None")
        else:
            print(*mp[indx_y][indx_x][:0:-1])