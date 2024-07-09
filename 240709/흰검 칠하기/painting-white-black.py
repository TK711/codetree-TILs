rnds = int(input())
rng = 200001
lst = [[0] for _ in range(rng)]
pivot = 100000
total_white = 0
total_black = 0
total_gray = 0
check = []
lst[pivot] = ["k"]

for _ in range(rnds):
    num, dire = input().split()
    num = int(num)
    # 방향따라 L 또는 R 더해준다.
    if num == 1:
        if dire == "L":
            lst[pivot].append("L")
        else:
            lst[pivot].append("R")
    elif dire == "L":
        lefty = pivot - num
        righty = pivot
        for pvt in range(lefty+1,righty+1):
            lst[pvt].append("L")
        pivot -= num-1
        check.append([pivot, lefty, righty])
    else:
        lefty = pivot
        righty = pivot + num
        for pvt in range(lefty, righty):
            lst[pvt].append("R")
        pivot += num-1
        check.append([pivot,lefty,righty])
for a in range(rng):
    L = 0
    R = 0
    for b in lst[a]:
        if b == "L":
            L += 1
        elif b == "R":
            R += 1
    if L > 1 and R > 1:
        total_gray += 1
    elif b == "L":
        total_white += 1
    elif b == "R":
        total_black += 1
lst[pivot].append("fin")

print(f"{total_white} {total_black} {total_gray}")


    # print(lst[a])
# for i in range(rng):
#     for a in lst[i]:
#         print(a)