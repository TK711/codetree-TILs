num = int(input())
lst = input().split()

num_to_rank = [0] * (num+1) # 5명이므로 
lst2 = []

class st:
    def __init__(self, numb, ind):
        self.N = numb
        self.I = ind

for idx, i in enumerate(lst, start = 1):
    lst2.append(st(int(i),idx))

lst2.sort(key = lambda x: (x.N, x.I))

# for j in lst2:
#     print(f"{j.N} ", end = "")

for rank, num in enumerate(lst2, start=1):
    num_to_rank[num.I] = rank

for k in num_to_rank:
    if k != 0:
        print(k,end = " ")