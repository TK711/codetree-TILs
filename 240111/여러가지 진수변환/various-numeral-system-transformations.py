inte, div  = input().split()

inte, div = int(inte),int(div)

num = 0
bin_ = []

while True:
    if inte <= (div-1):
        bin_.append(inte)
        break
    bin_.append(inte%div)
    inte = inte//div
    
for i in bin_[::-1]:
    print(i, end="")