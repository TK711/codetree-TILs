# 각 구슬은 고유번호와 이동거리 및 방향이 있다.
# 각 초마다 구슬은 방향으로 이동한다 (벽 만나면 바로 반대방향으로 이동)
# 중복이 있을 경우 큰 순서대로 k개만 남기고 제외한다.

import heapq
dire =  {'U':[-1,0], 'D':[1,0],'L':[0,-1],'R':[0,1]}

# n : 맵 크기, m : 구슬 개수, t : 초, k : 중복가능 수
n, m, t, k = list(map(int,input().split()))
lst = []
mp1 = [[[] for _ in range(n) ] for _ in range(n)]
mp2 = [[[] for _ in range(n) ] for _ in range(n)]
marbles = {}

# for a in mp1:
#     print(a)

for i in range(1,m+1):
    r, c, d, v = list(input().split())
    r, c, v = int(r), int(c), int(v)
    mp1[r-1][c-1].append(i)
    marbles.update({i:[d,v]})

# print(marbles)
# # print(marbles[1][1])
# print()
# for a in mp1:
#     print(a)
# 각 초마다
for s in range(t):
    # 구슬 있는 곳 찾기
    for st_y in range(n):
        for st_x in range(n):
            if mp1[st_y][st_x]:
                # 한 지점 내 각 구슬별 이동
                for nums in mp1[st_y][st_x]:
                    # print("nums",nums, type(nums))
                    each_y, each_x = st_y, st_x
                    # print("marbles[nums]",marbles[nums])
                    direc, velocity = marbles[nums][0], marbles[nums][1]
                    # 매초 이동
                    for turns in range(velocity):

                        # 다음 이동지가 범위 밖이면
                        if 0 <= each_y + dire[direc][0] < n and 0 <= each_x + dire[direc][1] < n:
                            pass
                        else:
                            if direc == 'U':
                                direc = 'D'
                            elif direc == 'D':
                                direc = 'U'
                            elif direc == 'L':
                                direc = 'R'
                            elif direc == 'R':
                                direc = 'L'
                        # 맞는 방향으로 이동
                        each_y, each_x = each_y + dire[direc][0], each_x + dire[direc][1]

                    # 각 구슬 종료, 지도2에 기록
                    mp2[each_y][each_x].append(nums)
                    marbles[nums] = [direc, velocity]
    # print()
    # for ch in mp2:
    #     print(ch)

    # # 모든 지점 방문 완료
    # # 지도 2 중복 제거
    for ch_y in range(n):
        for ch_x in range(n):
            if len(mp2[ch_y][ch_x]) > k:
                comp = []
                for cp in mp2[ch_y][ch_x]:
                    heapq.heappush(comp, (marbles[cp][1], cp))
                for _ in range(len(mp2[ch_y][ch_x]) - k):
                    heapq.heappop(comp)
                new = []
                for ret in comp:
                    new.append(ret[1])
                mp2[ch_y][ch_x] = new
    # print()
    # for ch in mp2:
    #     print(ch)

    # 지도 교체
    for ch_y1 in range(n):
        for ch_x1 in range(n):
            mp1[ch_y1][ch_x1] = mp2[ch_y1][ch_x1]
    mp2 = [[[] for _ in range(n)] for _ in range(n)]

# fin
tot = 0
for ch_y2 in range(n):
    for ch_x2 in range(n):
        if mp1[ch_y2][ch_x2]:
            tot += len(mp1[ch_y2][ch_x2])
print(tot)