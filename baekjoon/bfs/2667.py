#2667 단지번호붙이기
num = int(input())
cnt = 1
resList = []
mapList = []
for i in range(num):
    mapList.append(list(map(int ,list(input()))))

def bfs(li):
    global mapList
    global cnt
    global num
    visitedNode = []
    fVlist = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    bfsQueue = [li]
    
    cnt+=1
    mapList[li[0]][li[1]] = cnt
    while bfsQueue:
        tRow, tCol = bfsQueue[0] 
        del bfsQueue[0]
        visitedNode.append([tRow, tCol])
        
        for v in fVlist:
            bRow = tRow + v[0]
            bCol = tCol + v[1]
            if (bRow < 0 or bRow >= num) or (bCol < 0 or bCol >= num):
                continue
            if (mapList[bRow][bCol]==1):
                bfsQueue.append([bRow, bCol])
                mapList[bRow][bCol] = cnt
                
    return len(visitedNode)

for i in range(num):
    for j in range(num):
        if (mapList[i][j] != 1):
            continue
        resList.append(bfs([i,j]))
    
resList.sort()
print(len(resList))
for r in resList:
    print(r)