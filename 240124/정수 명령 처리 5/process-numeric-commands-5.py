num = int(input())

lst = []
lst2 = [0]

for i in range(num):
    lst.append(input())

for j in lst:
    if 'push' in j:
        _, numb = j.split()
        lst2.append(int(numb))
    elif 'get' in j:
        _, numb = j.split()
        print(lst2[int(numb)])
    elif 'size' in j:
        print(len(lst2)-1)
    else:
        lst2.pop()