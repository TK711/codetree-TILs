num = int(input())

lst = [0] * 200
lst2 = []
offset = 0
mx = 0

for i in range(num):
    a1,a2 = input().split()
    a1,a2 = int(a1),int(a2)
    if a1 <0:
        if abs(a1)>offset:
            offset = abs(a1)

    lst2.append([a1,a2])
    if a1 == a2:
        lst2.append([a1,a1+1])

# 각 리스트내 범위 돌며 체크
# 오프셋 절댓값을 추가한다

for i in lst2:
    for j in range(offset+int(i[0]),offset+int(i[1])):
        lst[j] += 1

for i in range(1,len(lst)):
    if mx < lst[i]:
        mx = lst[i]
print(mx)