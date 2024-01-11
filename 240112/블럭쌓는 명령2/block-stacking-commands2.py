num, rep =input().split()
num, rep = int(num),int(rep)

mx = 0
lst = [0] * (num+1)

for i in range(rep):
    a1, a2 = input().split()
    a1, a2 = int(a1), int(a2)
    for i in range(a1,a2+1):
        lst[i] += 1

for i in range(1,len(lst)):
    if mx < lst[i]:
        mx = lst[i]
print(mx)