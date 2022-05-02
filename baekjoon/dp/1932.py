#1932 정수 삼각형 
num = int(input())
initList = [list(map(int, input().split())) for _ in range(num)]
checkList = [[0]*i for i in range(1,num+1)]
checkList[num-1] = initList[num-1]
for r in range(num-2, -1, -1):
    for c in range(r+1):
        checkList[r][c] = initList[r][c] + max(checkList[r+1][c], checkList[r+1][c+1])
print(checkList[0][0])