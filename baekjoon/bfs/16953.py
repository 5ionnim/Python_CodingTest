#16953 A->B
inputList = input().split()
startNum, destNum = inputList[0], inputList[1]

output = -1
cnt = 0
while int(destNum) > int(startNum):
    if destNum[-1]=="1":
        destNum = destNum[0:-1]
        cnt+=1
    elif int(destNum)%2==0:
        destNum = str(int(destNum)//2)
        cnt+=1
    else:
        break
    
    if destNum == startNum:
        output = cnt + 1
        break
print(output)
    