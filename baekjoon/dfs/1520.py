#1520 내리막 길
rowNum, colNum = map(int, input().split())
initList = [list(map(int, input().split())) for _ in range(rowNum)]
checkList = [[-1] * colNum for _ in range(rowNum)]
fVList = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def DFS(startNode):
    global initList, checkList, fVList, rowNum, colNum
    if startNode == [rowNum - 1, colNum - 1]:
        return 1 
    elif checkList[startNode[0]][startNode[1]] != -1:
        return checkList[startNode[0]][startNode[1]]
    else :
        cnt = 0
        for v in fVList:
            ar = startNode[0] + v[0]
            ac = startNode[1] + v[1]
            if ar < 0 or ar >= rowNum:
                continue
            if ac < 0 or ac >= colNum:
                continue
            if initList[startNode[0]][startNode[1]] > initList[ar][ac]:
                cnt += DFS([ar, ac])
        checkList[startNode[0]][startNode[1]] = cnt
        return cnt

print(DFS([0, 0]))
