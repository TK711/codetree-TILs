n = int(input())
ls = list(map(int,input().split()))
minimum = 100 * 100 * 100

for i in range(n):
    total = 0
    for k in range(n):
        if i == k:
            continue
        else:
            total += ls[k] * abs(k-i)
    if total < minimum:
        minimum = total
print(minimum)