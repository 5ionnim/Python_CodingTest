#2156 포도주 시식
num = int(input())
initList = [int(input()) for _ in range(num)]
checkList = [[0, 0] for _ in range(num)]
maxP = 0
checkList[0] = [initList[0],initList[0]]
for i in range(1, num):
    checkList[i][0] = initList[i] + checkList[i-1][1]
    checkList[i][1] = initList[i] + maxP
    maxP = max(maxP, checkList[i-1][0], checkList[i-1][1])
print(max(map(max, checkList)))
        