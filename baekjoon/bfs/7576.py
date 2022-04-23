#7576 토마토
from collections import deque
colNum, rowNum = map(int, input().split())
initTable = []
fVList = [[-1, 0], [0, 1], [1, 0], [0, -1]]
bfsQueue = deque([])
for r in range(rowNum):
    initTable.append(list(map(int, input().split())))
for r in range(rowNum):
    for c in range(colNum):
        if initTable[r][c] == 1:
            bfsQueue.append([r, c])

while bfsQueue:
    tNodeRow, tNodeCol = bfsQueue.popleft()
    for v in fVList:
        tRow = tNodeRow + v[0]
        tCol = tNodeCol + v[1]
        if tRow < 0 or tRow >= rowNum:
            continue
        if tCol < 0 or tCol >= colNum:
            continue
        if initTable[tRow][tCol] == 0:
            initTable[tRow][tCol] = initTable[tNodeRow][tNodeCol] + 1
            bfsQueue.append([tRow, tCol])

res = 1
for r in range(rowNum):
    for c in range(colNum):
        if initTable[r][c] == 0:
            print(-1)
            exit(0)
        if initTable[r][c] > res:
            res = initTable[r][c]
print(res - 1)
        
            
                            