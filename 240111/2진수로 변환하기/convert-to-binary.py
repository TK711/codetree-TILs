num = int(input())

bin_ = []

while True:
    if num <= 1:
        bin_.append(num)
        break
    bin_.append(num%2)
    num = num//2
    
for i in bin_[::-1]:
    print(i, end="")