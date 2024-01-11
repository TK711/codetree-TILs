a, b = input().split()
b = int(b)
n = input()

dec = 0
#print(len(str(n)))
for i in range(len(n)):
    dec = dec * int(a) + int(n[i])

lst = []

while True:
    if dec <= b-1:
        lst.append(dec)
        break

    lst.append(dec % b)
    dec = dec//b

for s in lst[::-1]:
    print(s,end ="")