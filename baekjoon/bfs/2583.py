#2583 영역 구하기
from collections import deque

rowNum, colNum, rectNum = map(int, input().split())
initList = [[0 for _ in range(colNum)] for _ in range(rowNum)]
fVList = [[-1, 0], [0, 1], [1, 0], [0, -1]]
resultList = []

for _ in range(rectNum):
    left, top, right, bottom = map(int, input().split())
    for r in range(top, bottom):
        for c in range(left, right):
            initList[r][c] = 1
for r in range(rowNum):
    for c in range(colNum):
        if initList[r][c] == 0:
            cnt = 0
            initList[r][c] = 1
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
                    if initList[ar][ac] == 0:
                        dfsStack.append([ar, ac])
                        initList[ar][ac] = 1
            resultList.append(cnt)
resultList.sort()
print(len(resultList))
print(' '.join(map(str, resultList)))


    