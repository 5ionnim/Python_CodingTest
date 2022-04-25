#10026 적록색약
import copy
from collections import deque
iNum = int(input())
initList = [list(input()) for _ in range(iNum)]
fVList = [[-1, 0], [0, 1], [1, 0], [0, -1]]
listA = copy.deepcopy(initList)
cntA = 0
for r in range(iNum):
    for c in range(iNum):
        if listA[r][c] == 'B':
            cntA += 1
            bfsQueue = deque([[r, c]])
            listA[r][c] = 'C'
            while bfsQueue:
                tr, tc = bfsQueue.popleft()
                for v in fVList:
                    ar = tr + v[0]
                    ac = tc + v[1]
                    if ar < 0 or ar >= iNum:
                        continue
                    if ac < 0 or ac >= iNum:
                        continue
                    if listA[ar][ac] == 'B':
                        bfsQueue.append([ar, ac])
                        listA[ar][ac] = 'C'
            continue
        elif listA[r][c] in ['R', 'G']:
            cntA += 1
            bfsQueue = deque([[r, c]])
            listA[r][c] = 'C'
            while bfsQueue:
                tr, tc = bfsQueue.popleft()
                for v in fVList:
                    ar = tr + v[0]
                    ac = tc + v[1]
                    if ar < 0 or ar >= iNum:
                        continue
                    if ac < 0 or ac >= iNum:
                        continue
                    if listA[ar][ac] in ['R', 'G']:
                        bfsQueue.append([ar, ac])
                        listA[ar][ac] = 'C'

listB = copy.deepcopy(initList)
cntB = 0
for r in range(iNum):
    for c in range(iNum):
        if listB[r][c] != 'C':
            tAlpha = listB[r][c]
            cntB += 1
            bfsQueue = deque([[r, c]])
            listB[r][c] = 'C'
            while bfsQueue:
                tr, tc = bfsQueue.popleft()
                for v in fVList:
                    ar = tr + v[0]
                    ac = tc + v[1]
                    if ar < 0 or ar >= iNum:
                        continue
                    if ac < 0 or ac >= iNum:
                        continue
                    if listB[ar][ac] == tAlpha:
                        bfsQueue.append([ar, ac])
                        listB[ar][ac] = 'C'
print(cntB, cntA)
            
            
            



