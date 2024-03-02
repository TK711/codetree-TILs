# 변수 선언 및 입력:

N, M = map(int,input().split())
lst = []
for i in range(N):
    lst.append(int(input()))
while True:
    prev = -1
    cnt = 1
    lst2 = []
    flag = True
    if M == 1:
        lst = []
        break
    for idx, i in enumerate(lst):
        print(lst2)
        if not i == prev:
            if cnt >= M:
                flag = False
                for _ in range(cnt):
                    lst2.pop()
            cnt = 1
            prev = i
        else:
            cnt += 1
        lst2.append(i)
    if cnt >= M:
        flag = False
        for _ in range(cnt):
            lst2.pop()
    lst = lst2
    if flag == True:
        break


if lst:
    print(len(lst))
    for i in lst:
        print(i)
else:
    print(0)