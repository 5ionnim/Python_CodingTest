#14502 연구소  
from collections import deque
import copy
rowNum, colNum = map(int, input().split())
cntList = []
initList = []
virusList = []
wallList = []
fVList = [[-1, 0], [0, 1], [1, 0], [0, -1]]
for r in range(rowNum):
    initList.append(list(map(int, input().split())))
    
for r in range(rowNum):
    for c in range(colNum):
        if initList[r][c] == 2:
            virusList.append([r, c])

def bfsW(mapList, startNode):
    global fVList, rowNum, colNum
    resList = []
    bfsQueue = deque([tuple(startNode)])
    while bfsQueue:
        tr, tc = bfsQueue.popleft()
        for v in fVList:
            ar = tr + v[0]
            ac = tc + v[1]
            if ar < 0 or ar >= rowNum:
                continue
            if ac < 0 or ac >= colNum:
                continue
            if mapList[ar][ac] == 0:
                mapList[ar][ac] = 2
                bfsQueue.append((ar, ac))
                
        if len(bfsQueue) <= 3:
            resList += bfsQueue
    return list(set(resList))

for v in virusList:
    wallList += bfsW(copy.deepcopy(initList), v)

wallLen = len(wallList)
for fir in range(0, wallLen - 2):
    for sec in range(fir + 1, wallLen - 1):
        for thr in range(sec + 1, wallLen):
            cnt = 0
            copyList = copy.deepcopy(initList)
            copyList[wallList[fir][0]][wallList[fir][1]] = 1
            copyList[wallList[sec][0]][wallList[sec][1]] = 1
            copyList[wallList[thr][0]][wallList[thr][1]] = 1
            bfsQueue = deque([] + virusList)
            while bfsQueue:
                tr, tc = bfsQueue.popleft()
                for v in fVList:
                    ar = tr + v[0]
                    ac = tc + v[1]
                    if ar < 0 or ar >= rowNum:
                        continue
                    if ac < 0 or ac >= colNum:
                        continue
                    if copyList[ar][ac] == 0:
                        copyList[ar][ac] = 2
                        bfsQueue.append([ar, ac])
            
            for r in range(rowNum):
                for c in range(colNum):
                    if copyList[r][c] == 0:
                        cnt += 1
            cntList.append(cnt)
print(max(cntList))