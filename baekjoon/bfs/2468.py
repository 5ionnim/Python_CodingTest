#2468 안전 영역
from collections import deque
import copy

dNum = int(input())
initList = []
fVList = [[-1, 0], [0, 1], [1, 0], [0, -1]]
minNum = 100
maxNum = 1
for i in range(dNum):
    li = list(map(int, input().split()))
    if max(li) > maxNum:
        maxNum = max(li)
    if min(li) < minNum:
        minNum = min(li)
    initList.append(li)    
res = 1

def bfs(depth, mapList):
    cnt = 0
    for i in range(dNum):
        for j in range(dNum):
            if mapList[i][j] > depth:
                cnt += 1
                bfsQueue = deque([[i, j]])
                mapList[i][j] = -1
                while bfsQueue:
                    tr, tc = bfsQueue.popleft()
                    for v in fVList:
                        ar = tr + v[0]
                        ac = tc + v[1]
                        if ar < 0 or ar >= dNum:
                            continue
                        if ac < 0 or ac >= dNum:
                            continue
                        if mapList[ar][ac] > depth:
                            bfsQueue.append([ar, ac])
                            mapList[ar][ac] = -1
    return cnt
for t in range(minNum, maxNum):
    num = bfs(t, copy.deepcopy(initList))
    if num > res:
        res = num
print(res)
                