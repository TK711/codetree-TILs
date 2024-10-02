import heapq


def inside(in_y, in_x):
    return 0 <= nx_y and nx_y < 2002 and 0 <= nx_x and nx_x < 2002


def compare(ls1, ls2):
    comp = []
    heapq.heappush(comp, (ls1[0], ls1[1]))
    heapq.heappush(comp, (ls2[0], ls2[1]))
    rmv = heapq.heappop(comp)
    # print("comp, rmv",comp, rmv)
    return comp[-1], rmv

def srt(lst):
    leng = len(lst)
    for _ in range(leng-1):
        heapq.heappop(lst)
    return lst[0]

# 우선 각 판마다 설정
# 이후 특정 턴만큼 각 자리별로 이동 시작
# 이동시 이동할 위치의 mp1 확인(두 구슬 이동 중 충돌) => mp1의 구슬 삭제
# 이후 mp2 확인 (한 위치에서 충돌) => mp2의 구슬 삭제

direc = {'U': [1, 0], 'D': [-1, 0], 'L': [0, -1], 'R': [0, 1]}

t = int(input())
for _ in range(t):
    N = int(input())

    # 딕셔너리 지도 => 맵 너무 커서 사용
    mp1 = {}
    mp2 = {}
    # 구슬들
    marbles = {}

    for i in range(N):
        x, y, w, d = list(input().split())
        x, y, w = int(x), int(y), int(w)
        marbles.update({i + 1: [w, d]})
        # 지도 비었으면
        # if (y+1000,x+1000) not in mp1:
        # 딕셔너리 키로 추가
        mp1[(y + 1100, x + 1100)] = i + 1

    # print("marbles", marbles)
    # print("mp1", mp1)

    last_crash = 0

    for sec in range(1,N+1):  # unknown
        crash = False
        # 모든 y, x에 대해
        for st_y in range(2201):
            for st_x in range(2201):
                # 값 존재 시
                if (st_y, st_x) in mp1:
                    # 존재 값
                    num = mp1[(st_y, st_x)]
                    # print("num", num)
                    # 가중치, 방향
                    wei, drc = marbles[num]

                    # print("mp1[(st_y,st_x)]", num, marbles[num][0], marbles[num][1])
                    # 다음 이동 위치
                    nx_y, nx_x = st_y + direc[drc][0], st_x + direc[drc][1]
                    # print("nx_y, nx_x", nx_y, nx_x)
                    # 지도 위치 안이라면
                    # if inside(nx_y, nx_x):

                    # 지도 1의 이동위치에 있는지(이동 중 충돌 확인)
                    if (nx_y, nx_x) in mp1:
                        crash = True
                        # 두 값 중 가중치, 입력순(큰 순서)으로 생존
                        nx_num = mp1[(nx_y, nx_x)]
                        # 가중치, 입력순(큰 순서) 기준으로 큰값 보기 가중치 =
                        # print("marbles[nx_num]",marbles[nx_num])
                        nx_wei = marbles[nx_num][0]
                        # 실제 비교

                        lc, ln = [wei, num], [nx_wei, nx_num]
                        # print("lc, ln", lc, ln)
                        cmp = [[wei, num], [nx_wei, nx_num]]
                        ans = compare(lc,ln)
                        # print("sorted",ans)
                        # sorted(cmp, key=lambda x: (x[0], -x[1]))
                        # ans = cmp[0]
                        # 현재 위치 값이 더큼
                        if ans == [wei, num]:
                            del mp1[nx_y, nx_x]
                        # 이동 위치가 더 큼
                        else:
                            del mp1[st_y, st_x]
                            continue
                    #  지도1의 이동 위치 빔 > pass
                    else:
                        ans = [wei, num]
                    # 지도 밖 -> ?
                    # 지도 2 비교
                    # 지도 2에 있으면 추가 (힙큐)
                    # 없으면 생성 & 추가


                    # print("add to mp2")
                    if (nx_y, nx_x) in mp2:
                        crash = True
                        # mp2[(nx_y, nx_x)].append(ans)
                        # print("crash, ans non else",mp2[(nx_y, nx_x)],ans)
                        heapq.heappush(mp2[(nx_y, nx_x)], ans)
                    else:
                        mp2[(nx_y, nx_x)] = []
                        # mp2[(nx_y, nx_x)].append(ans)
                        # print("ans else",mp2[(nx_y, nx_x)],ans)
                        heapq.heappush(mp2[(nx_y, nx_x)], ans)

        # print()
        # print("mp1")
        # for k in mp1:
        #     print(k)
        # print()
        # print("mp2")
        # for k in mp2:
        #     print(k)

        if crash == True:
            # print("crash!",sec)
            last_crash = sec
        # 지도 교체
        mp1 = {}
        for crs in mp2:
            ls = mp2[crs]
            # print("ls",ls)
            lst = srt(ls)
            # sorted(ls, key=lambda x: (x[0], x[1]))
            # print("ls after", ls, lst)
            mp1[crs] = lst[1]
        #     print()
        # print("last_crash before", last_crash)
        # print("sorted mp2")
        # for k in mp2:
        #     print(k)
        mp2.clear()
        # print("last_crash after", last_crash)
    if last_crash ==0:
        print(-1)
    else:
        print(last_crash*2)
    # # 모든 이동 종료
    # mp1 = {}
    # for coors in mp2: