#9466 텀 프로젝트
caseNum = int(input())
res=[]
for _ in range(caseNum):
    num = int(input())
    initList = list(map(int, input().split()))
    checkList = [0]*num
    cnt = 0
    for n in range(num):
        if checkList[n]==0:
            checkList[n] = 1
            nextNode = initList[n]-1
            li = [n]
            while True:
                if checkList[nextNode]==0:
                    checkList[nextNode] = 1
                    li.append(nextNode)
                    nextNode = initList[nextNode]-1
                    continue
                elif checkList[nextNode]==1:
                    for i in range(0,li.index(nextNode)):
                        checkList[li[i]] = -1
                    for i in range(li.index(nextNode), len(li)):
                        checkList[li[i]] = 2
                    break
                else:
                    for i in range(len(li)):
                        checkList[li[i]] = -1
                    break
    for c in checkList:
        if c==-1:
            cnt+=1
    res.append(cnt)
for r in res:
    print(r)
    