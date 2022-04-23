#4963 섬의 개수
from collections import deque
resList = []
eVList = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
while True:
    cnt = 0
    colNum, rowNum = map(int, input().split())
    if colNum == 0 and rowNum == 0:
        break
    initList = []
    for r in range(rowNum):
        initList.append(list(map(int, input().split())))
    for r in range(rowNum):
        for c in range(colNum):
            if initList[r][c] == 1:
                cnt += 1
                initList[r][c] = 2
                bfsQueue = deque([[r, c]])
                while bfsQueue:
                    tr, tc = bfsQueue.popleft()
                    for v in eVList:
                        ar = tr + v[0]
                        ac = tc + v[1]
                        if ar < 0 or ar >= rowNum:
                            continue
                        if ac < 0 or ac >= colNum:
                            continue
                        if initList[ar][ac] == 1:
                            bfsQueue.append([ar, ac])
                            initList[ar][ac] = 2
    resList.append(cnt)
for r in resList:
    print(r)
                    