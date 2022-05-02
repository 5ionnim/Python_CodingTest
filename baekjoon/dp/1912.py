#1912 연속합
num = int(input())
initList = list(map(int, input().split()))
checkList = [0]*num
checkList[0] = initList[0]
for n in range(1, num):
    if checkList[n-1]+initList[n] >= initList[n]:
        checkList[n] = checkList[n-1]+initList[n]
    else :
        checkList[n] = initList[n]
print(max(checkList))
    
