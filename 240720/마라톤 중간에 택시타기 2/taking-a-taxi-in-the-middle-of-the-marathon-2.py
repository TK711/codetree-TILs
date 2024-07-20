n = int(input())
lst = [[0] * 2001 for _ in range(2001)]
ord_lst = []

for _ in range(n):
    inp_x, inp_y = list(map(int,input().split()))
    ord_lst.append([inp_x+1000,inp_y+1000])

# no first and last skip
# skip one point

# make new list
# do indexing
# if certain index, -2?

shortest = 200001
for k in range(1,n-1):
    tot = 0

    for cal in range(1,n):
        # cal is ahead
        if cal != k:
            tot += abs(ord_lst[cal][0] - ord_lst[cal-1][0]) + abs(ord_lst[cal][1] - ord_lst[cal-1][1])
        # skip point +1
        # connect skip point -1 and skip point +1
        elif cal != k+1:
            tot += abs(ord_lst[cal][0] - ord_lst[cal-2][0]) + abs(ord_lst[cal][1] - ord_lst[cal-2][1])
        # skip point
        else:
            pass
    if shortest > tot:
        shortest = tot
print(shortest)