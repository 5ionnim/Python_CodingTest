#1012 유기농 배추  
caseNum = int(input())
resList = []
fVList = [[-1, 0], [0, 1], [1, 0], [0, -1]]
for i in range(caseNum):
    cnt = 0
    colNum, rowNum, bNum = map(int, input().split())
    initTable = [[0 for j in range(colNum)] for k in range(rowNum)]
    for j in range(bNum):
        col, row = map(int, input().split())
        initTable[row][col] = 1
    
    for j in range(rowNum):
        for k in range(colNum):
            if initTable[j][k] == 1:
                cnt += 1
                bfsQueue = [[j, k]]
                initTable[j][k] = 2
                visitedNode = []
                while bfsQueue:
                    tNode = bfsQueue[0]
                    del bfsQueue[0]
                    visitedNode.append(tNode)
                    for v in fVList:
                        tRow = tNode[0] + v[0]
                        tCol = tNode[1] + v[1]
                        if tRow < 0 or tRow >= rowNum:
                            continue
                        if tCol < 0 or tCol >= colNum:
                            continue
                        if initTable[tRow][tCol] == 1:
                            bfsQueue.append([tRow, tCol])
                            initTable[tRow][tCol] = 2
    resList.append(cnt)

for r in resList:
    print(r)
                    
                
            
    
    
    
