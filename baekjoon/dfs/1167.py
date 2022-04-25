#1167 트리의 지름
from collections import deque

nodeNum = int(input())
edgeList = [[] for _ in range(nodeNum)]

for i in range(nodeNum):
    aList = list(map(int, input().split()))
    s = aList[0]
    aList = aList[1:-1]
    for j in range(0, len(aList), 2):
        edgeList[s-1].append([aList[j]-1, aList[j+1]])

dfsStack = deque([0])
visitedNode = [-1]*nodeNum
visitedNode[0] = 0
while dfsStack:
    tNode = dfsStack.pop()
    for n in edgeList[tNode]:
        a, b = n
        if visitedNode[a] == -1:
            dfsStack.append(a)
            visitedNode[a] = visitedNode[tNode] + b
maxN = visitedNode.index(max(visitedNode))

dfsStack = deque([maxN])
visitedNode = [-1]*nodeNum
visitedNode[maxN] = 0
while dfsStack:
    tNode = dfsStack.pop()
    for n in edgeList[tNode]:
        a, b = n
        if visitedNode[a] == -1:
            dfsStack.append(a)
            visitedNode[a] = visitedNode[tNode] + b
print(max(visitedNode))

    
    
    
    