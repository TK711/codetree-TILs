n = int(input())
leng = 1
mx = 0
prev = -1
for _ in range(n):
    new = int(input())
    if prev == new:
        leng += 1
    else:
        prev = new
        if mx < leng:
            mx = leng
        leng = 1
print(mx)