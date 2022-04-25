#1697 숨바꼭질
from collections import deque
startNum, destNum = map(int, input().split())
initList = [0 for _ in range(100001)]
bfsQueue = deque([startNum])
while bfsQueue:
    t = bfsQueue.popleft()
    if t == destNum:
        break
    for x in [t - 1, t + 1, t * 2]:
        if x >= 0 and x <= 100000 and not initList[x]:
            bfsQueue.append(x)
            initList[x] = initList[t] + 1
print(initList[destNum])
            