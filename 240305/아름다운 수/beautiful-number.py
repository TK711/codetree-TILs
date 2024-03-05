N = int(input().strip())
ans = []
count = 0

def subset(lv):
    global count
    # 배열 완성 시
    if lv == N:
        # 연속된 수 개수 확인
        # 각 연속된 수의 개수를 cnt로 세어 숫자가 바뀌거나 마지막에 해당 연속된 수로 나누어 나누어 떨어지면 ok
        prev = ans[0]
        cnt = 0
        flag = True

        for i in range(len(ans)):
            # 연속이면 cnt += 1
            if prev == ans[i]:
                cnt += 1
            else:
            # 연속 아니면
                # 해당 수로 나누어 떨어지지 않으면 False
                if cnt % prev != 0:
                    flag = False
                # 통과시 다음을위해 초기화
                cnt = 1
                prev = ans[i]
        # 마지막에 수가 안바뀌고 끝나는 경우 대비 마지막 검사
        if cnt % prev != 0:
            flag = False
        # 아름다운수 전체 개수 += 1
        if flag == True:
            count += 1
        return
    
    # 각 수열 만드는 재귀
    for i in range(1, 5):
        ans.append(i)
        subset(lv + 1)
        ans.pop()
    return
# 재귀 함수 호출
subset(0)
print(count)