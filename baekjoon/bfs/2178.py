#2178 미로 탐색 
rNum, cNum = map(int, input().split())
changeList = [[-1,0], [0,1], [1,0], [0,-1]]
bfsQueue = [[0,0]]
mapList = []
for r in range(rNum):
    mapList.append(list(map(int,list(input()))))

mapList[0][0] = 0   

while bfsQueue:
    baseR, baseC = bfsQueue[0]
    del bfsQueue[0]

    for c in changeList:
        cr = baseR+c[0]
        cc = baseC+c[1]
        if (cr < 0 or cr >= rNum)or(cc < 0 or cc >= cNum):
            continue
        if mapList[cr][cc]==1:
            bfsQueue.append([cr, cc])
            mapList[cr][cc] = mapList[baseR][baseC] + 1

print(mapList[rNum-1][cNum-1]+1)

    

