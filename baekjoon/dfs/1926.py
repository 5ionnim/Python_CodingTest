#1926 그림
from collections import deque
rowNum, colNum = map(int, input().split())
initList = [list(map(int, input().split())) for _ in range(rowNum)]
fVList = [[-1, 0], [0, 1], [1, 0], [0, -1]]
maxNum = 0
paintNum = 0
for r in range(rowNum):
    for c in range(colNum):
        if initList[r][c] == 1:
            paintNum += 1
            initList[r][c] = 2
            cnt = 0
            dfsStack = deque([[r, c]])
            while dfsStack:
                tr, tc = dfsStack.pop()
                cnt += 1
                for v in fVList:
                    ar = tr + v[0]
                    ac = tc + v[1]
                    if ar < 0 or ar >= rowNum:
                        continue
                    if ac < 0 or ac >= colNum:
                        continue
                    if initList[ar][ac]==1:
                        dfsStack.append([ar, ac])
                        initList[ar][ac] = 2
            if maxNum < cnt:
                maxNum = cnt
print(paintNum)
print(maxNum)

                
            
        