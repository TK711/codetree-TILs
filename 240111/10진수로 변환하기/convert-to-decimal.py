num = str(input())
dig = 0

for i in range(len(num)):
    dig = dig*2 + int(num[i])

print(dig)