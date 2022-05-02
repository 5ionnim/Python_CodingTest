#10844 쉬운 계단 수
num = int(input())
initList = [[0]*10 for _ in range(num)]
initList[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
if num > 1:
    initList[1] = [0, 2, 2, 2, 2, 2, 2, 2, 2, 1]
    for i in range(2, num):
        initList[i][1] = initList[i-1][2] + initList[i-2][1]
        for j in range(2,9):
            initList[i][j] = initList[i-1][j-1] + initList[i-1][j+1]
        initList[i][9] = initList[i-1][8]
print(sum(initList[num-1])%1000000000)