#1700 멀티탭 스케줄링
from collections import deque
holeNum, orderNum = map(int, input().split())
checkDict = dict()
orderList = deque([])
holeSet = set()
cnt = 0
for o in list(map(int, input().split())):
    if o in list(checkDict.keys()):
        checkDict[o][1] += 1
    else :
        checkDict[o] = [False, 1]
    orderList.append(o)
while len(holeSet) < holeNum:
    o = orderList.popleft()
    checkDict[o][0] = True
    checkDict[o][1] -= 1
    holeSet.add(o)
    
while orderList:
    o = orderList.popleft()
    if checkDict[o][0]:
        checkDict[o][1] -= 1
        continue
    t = -1
    maxt = -1
    for s in list(holeSet):
        if checkDict[s][1] == 0:
            t = s
            break
        if maxt < orderList.index(s):
            maxt = orderList.index(s)
            t = s
    checkDict[t][0] = False
    holeSet.remove(t)
    checkDict[o][0] = True
    checkDict[o][1] -= 1
    holeSet.add(o)
    cnt += 1
print(cnt)