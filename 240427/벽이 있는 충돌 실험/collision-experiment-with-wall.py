for tc in range(1,int(input())+1):
    direc = {'U':[1,0],'D':[-1,0],'R':[0,1],'L':[0,-1]}
    n, m = map(int,input().split())

    mp = [[0] * (n+1) for _ in range(n+1)]

    # print(n,m)
    # print()
    # for k in mp:
    #     print(k)
    # print()
    lst = ['N']
    for k in range(1,m+1):
        # print(k)
        x, y, dr = list(input().split())
        x, y = int(x), int(y)
        # print(x,y,dr)
        mp[y][x] = k
        lst.append(dr)
    # for k in mp:
    #     print(k)

    for _ in range(2*m+1):
        new_mp = [[0] * (n+1) for _ in range(n+1)]
        for i in range(n + 1):
            for j in range(n + 1):
                if mp[i][j] > 0:
                    num = mp[i][j]
                    # dire = lst[num]
                    if lst[num]=='U':
                        new_y = i + direc['U'][0]
                        new_x = j + direc['U'][1]
                    if lst[num]=='D':
                        new_y = i + direc['D'][0]
                        new_x = j + direc['D'][1]
                    if lst[num]=='L':
                        new_y = i + direc['L'][0]
                        new_x = j + direc['L'][1]
                    if lst[num]=='R':
                        new_y = i + direc['R'][0]
                        new_x = j + direc['R'][1]

                    if 0 < new_x < n + 1 and 0 < new_y < n + 1:
                        if new_mp[new_y][new_x] == 0:
                            new_mp[new_y][new_x] = num
                        else:
                            new_mp[new_y][new_x] = 0
                    else:
                        new_mp[i][j] = num
                        if lst[num] == 'U':
                            lst[num] = 'D'
                        elif lst[num] == 'D':
                            lst[num] = 'U'
                        elif lst[num] == 'L':
                            lst[num] = 'R'
                        elif lst[num] == 'R':
                            lst[num] = 'L'
        for i in range(n+1):
            for j in range(n + 1):
                mp[i][j] = new_mp[i][j]
    #     print()
    #     for k in mp:
    #         print(k)
    # print()
    # print('fin')
    # for k in mp:
    #     print(k)

    cnt = 0

    for i in range(n + 1):
        for j in range(n + 1):
            if mp[i][j] != 0:
                cnt += 1
    print(cnt)