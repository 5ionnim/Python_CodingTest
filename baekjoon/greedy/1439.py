#1439 뒤집기 
numStr = list(map(int, input()))
fCheck = numStr[0]
checkLi = [0,0]
checkLi[fCheck] += 1
for num in numStr:
    if (fCheck != num)&(num == 0):
        fCheck = num
        checkLi[0] += 1
    elif (fCheck != num)&(num == 1):
        fCheck = num
        checkLi[1] += 1

print(min(checkLi))
    