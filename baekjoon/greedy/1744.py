#1744 수 묶기 
numNum = int(input())
res = 0
pList = []
mList = []
oList = []
for i in range(numNum):
    num = int(input())
    if (num > 1):
        pList.append(num)
    elif (num == 1):
        oList.append(num)
    else :
        mList.append(num)
pList.sort(reverse = True)
mList.sort()
while True:
    if (len(pList) > 2):
        first = pList[0]
        second = pList[1]
        res += first*second
        del pList[0]
        del pList[0]
    elif (len(pList) == 2):
        res += pList[0]*pList[1]
        break
    elif (len(pList) == 1):
        res += pList[0]
        break
    else :
        break

while True:
    if (len(mList) > 2):
        first = mList[0]
        second = mList[1]
        res += first*second
        del mList[0]
        del mList[0]
    elif (len(mList) == 2):
        res += mList[0]*mList[1]
        break
    elif (len(mList) == 1):
        res += mList[0]
        break
    else :
        break
print(res + len(oList))
    
