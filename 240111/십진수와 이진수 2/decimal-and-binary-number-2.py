N = str(input())

bin_lst = []
dec = 0

for i in N:
    dec = dec * 2 + int(i)

dec = dec * 17

while True:
    if dec <= 1:
        bin_lst.append(dec)
        break
    bin_lst.append(dec%2)
    dec = dec//2

for i in bin_lst[::-1]:
    print(i, end="")