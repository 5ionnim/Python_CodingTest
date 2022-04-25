#2573 빙산
from collections import deque
import copy
rowNum, colNum = map(int, input().split())
initList = [list(map(int, input().split())) for _ in range(rowNum)]
fVList = [[-1, 0], [0, 1], [1, 0], [0, -1]]
year = 0
while True:
    year += 1
    exList = copy.deepcopy(initList)
    cnt = 0
    tag = True
    for r in range(rowNum):
        for c in range(colNum):
            if exList[r][c] == 0:
                continue
            tag = False
            for v in fVList:
                ar = r + v[0]
                ac = c + v[1]
                if ar < 0 or ar >= rowNum:
                    continue
                if ac < 0 or ac >= colNum:
                    continue
                if exList[ar][ac] == 0:
                    if initList[r][c] > 0:
                        initList[r][c] -= 1
    if tag:
        print(0)
        break
    exList = copy.deepcopy(initList)
    for r in range(rowNum):
        for c in range(colNum):
            if exList[r][c] > 0:
                cnt += 1
                dfsStack = deque([[r, c]])
                exList[r][c] = 0
                while dfsStack:
                    tr, tc = dfsStack.pop()
                    for v in fVList:
                        ar = tr + v[0]
                        ac = tc + v[1]
                        if ar < 0 or ar >= rowNum:
                            continue
                        if ac < 0 or ac >= colNum:
                            continue
                        if exList[ar][ac] != 0:
                            exList[ar][ac] = 0
                            dfsStack.append([ar, ac])
    if cnt >= 2:
        print(year)
        break
                
    
            
    
    