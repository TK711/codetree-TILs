n = int(input())

lst = []
stk = []
ans = 0

for _ in range(n):
    inp = int(input())
    lst.append(inp)

# get first number and second number adn third number in order
# checker
for i1 in range(len(lst)):
    stk.append(lst[i1])
    for i2 in range(i1+1, len(lst)):

        # check process
        rng = min(len(str(lst[i1])), len(str(lst[i2])))
        flg = True
        for reverse_a in range(rng):
            a = -1 - reverse_a
            if int(str(lst[i1])[a]) + int(str(lst[i2])[a]) >= 10:
                flg = False
                break
            # else:
                # print("pass", str(lst[i1])[a], str(lst[i2])[a])
        if flg:
            stk.append(lst[i2])
            middle = sum(stk)
        else:
            continue
        for i3 in range(i2+1, len(lst)):
            flg2 = True
            # check process
            rng = min(len(str(middle)), len(str(lst[i3])))
            for reverse_a in range(rng):
                a = -1 - reverse_a
                if int(str(middle)[a]) + int(str(lst[i3])[a]) >= 10:
                    flg2 = False
                    break
                # else:
                #     print("pass", str(middle)[a], str(lst[i3])[a])

            if flg2 == True:
                stk.append(lst[i3])
                if sum(stk) > ans:
                    ans = sum(stk)
            else:
                continue



            stk.pop()
        stk.pop()
    stk.pop()
if ans == 0:
    print(-1)
else:
    print(ans)