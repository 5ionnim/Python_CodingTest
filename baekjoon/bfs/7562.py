#7562 나이트의 이동
from collections import deque
eVList = [[-2, 1], [-1, 2], [1, 2], [2, 1], [1, -2], [2, -1], [-2, -1], [-1, -2]]
caseNum = int(input())
res = []
for i in range(caseNum):
    lNum = int(input())
    visitedList = [[-1]*lNum for _ in range(lNum)]
    sRow, sCol = map(int, input().split())
    dRow, dCol = map(int, input().split())
    visitedList[sRow][sCol] = 0
    bfsQueue = deque([[sRow, sCol]])
    while bfsQueue:
        tRow, tCol = bfsQueue.popleft()
        for e in eVList:
            aRow = tRow + e[0]
            aCol = tCol + e[1]
            if aRow < 0 or aRow >= lNum:
                continue
            if aCol < 0 or aCol >= lNum:
                continue
            if visitedList[aRow][aCol] == -1:
                bfsQueue.append([aRow, aCol])
                visitedList[aRow][aCol] = visitedList[tRow][tCol] + 1
    res.append(visitedList[dRow][dCol])

for r in res:
    print(r)

        