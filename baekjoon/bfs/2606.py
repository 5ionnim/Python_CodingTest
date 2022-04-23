#2606 바이러스  
nodeNum = int(input())
edgeNum = int(input())
bfsQueue = [1]
visitedNode = []
edgeInfo = dict()
for i in range(edgeNum):
    a, b = map(int, input().split())
    if a not in edgeInfo.keys():
        edgeInfo[a] = []
    edgeInfo[a].append(b)
    if b not in edgeInfo.keys():
        edgeInfo[b] = []
    edgeInfo[b].append(a)

while bfsQueue:
    targetNode = bfsQueue[0]
    del bfsQueue[0]
    visitedNode.append(targetNode)
    for n in edgeInfo[targetNode]:
        if n in bfsQueue:
            continue
        if n in visitedNode:
            continue
        bfsQueue.append(n)

print(len(visitedNode)-1)

        