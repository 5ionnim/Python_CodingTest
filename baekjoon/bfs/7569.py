#7569 토마토 //////////////////
from collections import deque
colNum, rowNum, heiNum = map(int, input().split())
initList = [[list(map(int, input().split())) for _ in range(rowNum)] for _ in range(heiNum)]
sVList = [[-1, 0, 0],[1, 0, 0],[0, -1, 0], [0, 0, 1], [0, 1, 0],[0, 0, -1]]
bfsQueue = deque([])
for h in range(heiNum):
    for r in range(rowNum):
        for c in range(colNum):
            if initList[h][r][c] == 1:
                bfsQueue.append([h, r, c])
while bfsQueue:
    th, tr, tc = bfsQueue.popleft()
    for v in sVList:
        ah = th + v[0]
        ar = tr + v[1]
        ac = tc + v[2]
        if ah < 0 or ah >= heiNum:
            continue
        if ar < 0 or ar >= rowNum:
            continue
        if ac < 0 or ac >= colNum:
            continue
        if initList[ah][ar][ac] == 0:
            bfsQueue.append([ah, ar, ac])
            initList[ah][ar][ac] = initList[th][tr][tc] + 1
maxTerm = 1
tag = False
for h in range(heiNum):
    for r in range(rowNum):
        for c in range(colNum):
            if initList[h][r][c] == 0:
                tag = True
            if initList[h][r][c] > maxTerm:
                maxTerm = initList[h][r][c]
            
print(-1 if tag else (maxTerm - 1))

