lst = list(input())
cnt = 0
for i in range(len(lst)):
    if lst[i] == "(":
        for j in range(i,len(lst)):
            if lst[j] == ")":
                cnt += 1
    else:
        continue
print(cnt)