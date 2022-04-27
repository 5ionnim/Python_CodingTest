#1068 트리
from collections import deque
nodeNum = int(input())
initList = list(map(int, input().split()))
sNode = 0
cnt = 0
reverseList = [[] for _ in range(nodeNum)]
for i in range(nodeNum):
    if initList[i] == -1:
        sNode = i
        continue
    reverseList[initList[i]].append(i)
delNode = int(input())
dfsStack = deque([sNode])
while dfsStack:
    tNode = dfsStack.pop()
    if tNode == delNode:
        continue
    elif len(reverseList[tNode]) == 0:
        cnt+=1
        continue
    elif len(reverseList[tNode]) == 1 and reverseList[tNode][0] == delNode:
        cnt+=1
        continue
    for r in reverseList[tNode]:
        dfsStack.append(r)
print(cnt)
