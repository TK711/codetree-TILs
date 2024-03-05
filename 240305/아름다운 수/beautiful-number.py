N = int(input().strip())
ans = []
count = 0

def subset(lv):
    global count

    if lv == N:

        prev = ans[0]
        cnt = 0
        flag = True

        for i in range(len(ans)):
            if prev == ans[i]:
                cnt += 1
            else:
                if cnt % prev != 0:
                    flag = False
                cnt = 1
                prev = ans[i]

        if cnt % prev != 0:
            flag = False

        if flag == True:
            count += 1
        return

    for i in range(1, 5):
        ans.append(i)
        subset(lv + 1)
        ans.pop()
    return

subset(0)
print(count)