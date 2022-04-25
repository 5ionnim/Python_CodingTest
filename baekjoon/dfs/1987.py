#1987 알파벳
rowNum, colNum = map(int, input().split())
initList = [list(input()) for _ in range(rowNum)]
fVList = [[-1, 0], [0, 1], [1, 0], [0, -1]]
maxLen = 1
checkList = [0] * 26
def search_root(startNode, visitedNum):
    global rowNum, colNum, initList, fVList, maxLen
    maxLen = max(maxLen, visitedNum)
    checkList[ord(initList[startNode[0]][startNode[1]])-65] = 1
    for v in fVList:
        tr = startNode[0] + v[0]
        tc = startNode[1] + v[1]
        if tr < 0 or tr >= rowNum:
            continue
        if tc < 0 or tc >= colNum:
            continue
        if checkList[ord(initList[tr][tc])-65]==0:
            search_root([tr, tc], visitedNum + 1)
            checkList[ord(initList[tr][tc])-65]=0
            
search_root([0, 0], 1)
print(maxLen)

            
        

