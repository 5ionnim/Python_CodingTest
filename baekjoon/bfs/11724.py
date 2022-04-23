#11724 연결 요소의 개수
from collections import deque

nodes, edges = map(int, input().split())
initTable = [[0 for _ in range(nodes)] for _ in range(nodes)]
cnt = 0
for i in range(edges):
    s, e = map(int, input().split())
    initTable[s-1][e-1] = 1
    initTable[e-1][s-1] = 1

for n in range(nodes):
    if 1 in initTable[n]:
        cnt += 1
        bfsQueue = deque([n])
        while bfsQueue:
            t = bfsQueue.popleft()
            for e in range(nodes):
                if initTable[t][e] == 1:
                    initTable[t][e] = 2
                    initTable[e][t] = 2
                    bfsQueue.append(e)
        continue
    
    if sum(initTable[n]) == 0:
        cnt += 1
print(cnt)

            
