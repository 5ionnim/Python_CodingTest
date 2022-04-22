#1449 수리공 항승
holeNum, tapeCM = map(int, input().split())
holeList = list(map(int, input().split()))
holeList.sort()

tapeNum = 1
tapeR = holeList[0] + tapeCM - 1
while holeList:
    if holeList[0] <= tapeR:
        del holeList[0]
    elif holeList[0] > tapeR:
        tapeNum += 1
        tapeR = holeList[0] + tapeCM - 1
print(tapeNum)