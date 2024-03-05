K, N = map(int, input().split())

ans = []

def subset(lv):
    if lv == N:
        for j in ans:
            print(j, end = ' ')
        print()

        return

    for i in range(1, K + 1):
        ans.append(i)
        subset(lv + 1)
        ans.pop()
    return

subset(0)