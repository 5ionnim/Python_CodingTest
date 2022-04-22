#1260 DFS와 BFS
nodeNum, edgeNum, startNode = map(int, input().split())
edgeInfo = dict()

bfsVisited = []
bfsQueue = [startNode]

dfsVisited = [startNode]
dfsStack = [startNode]

for e in range(edgeNum):
    a, b = map(int, input().split())
    if a in edgeInfo.keys():
        edgeInfo[a].append(b)
    else :
        edgeInfo[a] = [b]
        
    if b in edgeInfo.keys():
        edgeInfo[b].append(a)
    else :
        edgeInfo[b] = [a]
        
for k in edgeInfo.keys():
    edgeInfo[k].sort()


if startNode not in edgeInfo.keys():
    bfsVisited = [startNode]
else :
    #DFS
    while dfsStack:
        li = edgeInfo[dfsStack[-1]]
        flag = False
        for l in li:
            if l not in dfsVisited:
                flag = True
                dfsStack.append(l)
                dfsVisited.append(l)
                break
        if not flag:
            del dfsStack[-1]


        
    #BFS
    while bfsQueue:
        bfsVisited.append(bfsQueue[0])
        li = edgeInfo[bfsQueue[0]]
        del bfsQueue[0]
        for l in li:
            if (l not in bfsVisited) and (l not in bfsQueue):
                bfsQueue.append(l)
            
print(' '.join(list(map(str, dfsVisited))))
print(' '.join(list(map(str, bfsVisited))))