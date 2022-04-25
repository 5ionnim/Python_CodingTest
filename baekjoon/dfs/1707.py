#1707 이분 그래프
from collections import deque
caseNum = int(input())
res = []
for n in range(caseNum):
    nodeNum, edgeNum = map(int, input().split())
    colorList = [-1]*nodeNum
    edgeInfo = [[] for _ in range(nodeNum)]
    tag = True
    for e in range(edgeNum):
        s, d = map(int, input().split())
        edgeInfo[s - 1].append(d - 1)
        edgeInfo[d - 1].append(s - 1)
    for node in range(nodeNum):
        if colorList[node] != -1:
            continue
        dfsStack = deque([node])
        colorList[node] = 0
        while dfsStack and tag:
            t = dfsStack.pop()
            for e in edgeInfo[t]:
                if colorList[e] == -1:
                    colorList[e] = (colorList[t] + 1)%2
                    dfsStack.append(e)
                    continue
                if (colorList[t] + 1)%2 != colorList[e]:
                    tag = False
                    break
        if not tag:
            res.append("NO")
            break
    if tag:
        res.append("YES")
for r in res:
    print(r)
                    
            