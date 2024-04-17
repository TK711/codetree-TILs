def dfs(lst):
    # print(lst)
    if len(lst) == m:
        print(*lst)

    else:
        if lst:
            for i in range(lst[-1]+1, n+1):
                lst.append(i)
                dfs(lst)
                lst.pop()
        else:
            for i in range(1,n+1):
                lst.append(i)
                dfs(lst)
                lst.pop()

n, m = map(int, input().split())
lst = []
dfs(lst)