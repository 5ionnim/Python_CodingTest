#1783 병든 나이트
nNum, mNum = map(int, input().split())
moveCnt = 1
xP = 1
yP = 1
if (nNum < 2) or (mNum < 2):
    print(moveCnt)
elif mNum < 7:
    if nNum == 2:
        while xP <= mNum - 2:
            xP += 2
            moveCnt += 1
    elif nNum > 2:
        while xP < mNum:
            xP += 1
            moveCnt += 1
        moveCnt = 4 if moveCnt > 4 else moveCnt
    print(moveCnt)
elif mNum >= 7:
    if nNum == 2:
        while xP <= mNum - 2:
            xP += 2
            moveCnt += 1
        moveCnt = 4 if moveCnt > 4 else moveCnt
    elif nNum > 2:
        xP = 7
        moveCnt = 5
        while xP < mNum:
            xP += 1
            moveCnt += 1
    print(moveCnt)
        
        