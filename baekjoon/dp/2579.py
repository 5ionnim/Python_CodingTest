#2579 계단 오르기
num = int(input())
initList = [int(input()) for _ in range(num)]
checkList = [[0,0] for _ in range(num)]
checkList[0] = [initList[0], 0]
if num > 1:
    checkList[1] = [initList[1]+initList[0], initList[1]]
    for i in range(2, num):
        checkList[i][0] = checkList[i-1][1] + initList[i]
        checkList[i][1] = max(checkList[i-2][0], checkList[i-2][1]) + initList[i]
print(max(checkList[num -1]))
