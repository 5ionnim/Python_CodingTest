#2810 컵홀더
lineNum = int(input())
lineList = list(input())
i = 0
hNum = 1
while i < lineNum:
    if lineList[i] == "S":
        i += 1
        hNum += 1
    elif lineList[i] == "L":
        i += 2
        hNum += 1
print(min(hNum, lineNum))