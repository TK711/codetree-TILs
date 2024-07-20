n, t = list(map(int,input().split()))
wrd = input()
# lst = [[0] * n for _ in range(n)]
lst = []
for _ in range(n):
    lt = list(map(int,input().split()))
    lst.append(lt)


# down, right, up, left
dx = [0,1,0,-1]
dy = [-1,0,1,0]

# get middle
if n%2 == 1:
    mid = (n//2) 
else:
    mid = n//2

# move from middle
# face down at first
dire, tot = 0, 0
x, y = mid, mid

tot += lst[y][x]
for order in wrd:
    if order == "F":
        # forward
        new_x = x + dx[dire]
        new_y = y + dy[dire]
        if 0 <= new_x < n and 0 <= new_y < n:
            x = new_x
            y = new_y
            tot += lst[y][x]
        else:
            pass
    elif order == "L":
        # left
        dire = (dire - 1 )%4
    elif order == "R":
        #right
        dire = (dire + 1 )%4
print(tot)