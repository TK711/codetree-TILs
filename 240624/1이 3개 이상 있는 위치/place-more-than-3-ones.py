n = int(input())

lst = []
for i in range(n):
    lt = list(input().split())
    lst.append(lt)

dxs = [0,1,0,-1]
dys = [1,0,-1,0]
tot = 0

for k1 in range(n):
    for k2 in range(n):
        cnt = 0
        for dx, dy in zip(dxs,dys):
            if n > k1 + dx >= 0 and n > k2 + dy >= 0:
                if lst[k1 + dx][k2 + dy] == '1':
                    cnt += 1
        if cnt >= 3:
            tot += 1
print(tot)