# 각 구슬 하나 > v만큼 이동해야함, 
# 벽이면 방향전환하고 이동
# 충돌시 개수 확인 후 작은 값부터 삭제
# 각 지도에 idx 입력 후 중복시 일단 입력, 역정렬 후 뒤에서부터 pop
# => 매번 삭제 확인 및 인덱스 값 비교하면 어려움

# marbles에 딕셔너리로 하나씩 넣기(방향 & 거리)
# 인덱스인 idx는 지도 위 & 딕셔너리의 key 값으로
n, m, t, k = list(map(int,input().split()))
mp1 = [[[0] for _ in range(n)] for _ in range(n)]
mp2 = [[[0] for _ in range(n)] for _ in range(n)]
# for a in mp1:
#     print(a)
# print()

marbles = {}
dire = {'U':[-1, 0],
        'D':[ 1, 0],
        'L':[ 0, 1],
        'R':[ 0,-1]}

# 판에는 idx 기록, 딕셔너리는 idx를 key, 방향, 속력은 value로
for idx in range(m):
    # r, c, d, v => 행, 열, 방향, 속도
    r, c, d, v = list(input().split())
    r,c = int(r),int(c)
    mp1[r-1][c-1].append(idx+1)
    marbles.update({idx+1:[d,int(v)]})

# for a in mp1:
#     print(a)
# print()
# print(marbles)

for ch in range(t):
    # print("marbles",marbles)

    # print()
    # print("mp1")
    # for tst in mp1:
    #     print(tst)
    # print()

    # print("t",t)
    # 이전처럼 지도 2개 사용
    # 각 mp1의 값들 하나씩 이동하여 mp2에 기록
    for st_y in range(n):
        for st_x in range(n):
            # 0 아니면(다른 수 있으면)
            # print("mp1[st_y][st_x]",mp1[st_y][st_x])
            if mp1[st_y][st_x][-1] != 0:
                # print("mp1[st_y][st_x][-1]",mp1[st_y][st_x][-1])
                # 0 전까지 역순으로
                # print("mp1[st_y][st_x]",mp1[st_y][st_x][1::]) 
                for num in mp1[st_y][st_x][1::]:
                    
                    # print("st_y, st_x, num",st_y, st_x, num)
                    # 각 거리만큼 이동(방향 주의)
                    d, v = marbles[num]
                    # print("d, v",d, v)
                    
                    in_y, in_x = st_y, st_x
                    for _ in range(v):
                        # print("st_y, st_x, d",st_y, st_x, d)
                        # 한 칸 이동 가능시 이동, 아니면 방향 반대 후 이동
                        mv =  dire[d]
                        
                        nxt_y, nxt_x = in_y + mv[0], in_x + mv[1]
                        if 0 <= nxt_y < n and 0 <= nxt_x < n:
                            # print("mv",mv)
                            pass
                        else:
                            if d == 'U':
                                d = 'D'
                            elif d == 'D':
                                d = 'U'
                            elif d == 'L':
                                d = 'R'
                            elif d == 'R':
                                d = 'L'
                            
                            mv =  dire[d]
                            marbles[num][0] = d
                            # print("mv",mv)
                            nxt_y, nxt_x = in_y + mv[0], in_x + mv[1]
                        in_y, in_x = nxt_y, nxt_x
                    mp2[in_y][in_x].append(num)
    # print()
    # for b in mp2:
    #     print(b)
    # print()
    # mp2의 중복 제거
    for y1 in range(n):
        for x1 in range(n):
            if len(mp2[y1][x1]) > k:
                # 작은순으로 정렬해서 0 제외 작은 값부터 제거
                target = mp2[y1][x1]
                target.sort(reverse=True)
                # print("target",target)
                for _ in range(len(target)-k):
                    target.pop()
                target.append(0)
                # print("target after",target)
                target.sort()
                mp2[y1][x1] = target
    
    # print()
    # for tst2 in mp2:
    #     print(tst2)

    # mp2에서 mp1으로
    for y2 in range(n):
        for x2 in range(n):
            mp1[y2][x2] = mp2[y2][x2]
    mp2 = [[[0] for _ in range(n)] for _ in range(n)]

# print("mp1")
# for tst in mp1:
#     print(tst)
# print()
tot = 0
for y3 in range(n):
    for x3 in range(n):
        # print("mp1[y3][x3]",mp1[y3][x3])
        # print(type(mp1[y3][x3]))
        tot += (len(mp1[y3][x3])-1)
print(tot)