#1149 RGB 거리
num = int(input())
initList = [list(map(int, input().split())) for _ in range(num)]
checkList = [[0]*3 for _ in range(num)]
checkList[0] = initList[0]
for i in range(1, num):
    checkList[i][0] = min(checkList[i-1][1], checkList[i-1][2]) + initList[i][0]
    checkList[i][1] = min(checkList[i-1][0], checkList[i-1][2]) + initList[i][1]
    checkList[i][2] = min(checkList[i-1][0], checkList[i-1][1]) + initList[i][2]
print(min(checkList[num-1]))
            
    
