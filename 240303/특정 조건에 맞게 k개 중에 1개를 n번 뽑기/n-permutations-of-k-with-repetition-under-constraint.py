k, n = map(int,input().split())
ans = []

def print_ans():
    if len(ans) != 1:
        prev = ans[0]
        flag = True
        for i in ans:
            if not i == prev:
                flag = False
        if flag == False:
            for elem in ans:
                print(elem,end = " ")
            print()
    else:
        print(ans[0])
def choose(curr_num):
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