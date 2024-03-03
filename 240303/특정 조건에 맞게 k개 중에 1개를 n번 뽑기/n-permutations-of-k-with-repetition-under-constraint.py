k, n = map(int,input().split())
ans = []

def print_ans():
    flag = True
    for i in range(len(ans)):
        if i + 2 < len(ans):
            if ans[i] == ans[i+1] == ans[i+2]:
                flag = False
    if flag == True:
        for elem in ans:
            print(elem,end = " ")
        print()

def choose(curr_num):
    # print(curr_num,ans,n)
    if curr_num == n + 1:
        print_ans()
        return
    if not k == 1:
        for i in range(1,k+1):
            ans.append(i)
            choose(curr_num+1)
            ans.pop()
    else:
        ans.append(1)
        choose(curr_num+1)
        ans.pop()

choose(1)