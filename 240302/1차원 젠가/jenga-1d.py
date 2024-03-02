N = int(input())
lst = []

for _ in range(N):
    lst.append(int(input()))
# print(lst)
lst2 = []
for _ in range(2):
    st, end = map(int, input().split())
    st -= 1
    end -= 1
    # print(f'st {st} end {end}')
    for i in range(0,st):
        lst2.append(lst[i])
    # print('lst2',lst2)
    for j in range(end+1,len(lst)):
        lst2.append(lst[j])
    lst = lst2
    lst2 = []
    # print(lst)
print(len(lst))
for i in lst:
    print(i)