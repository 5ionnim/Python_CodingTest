#9461 파도반 수열
caseNum = int(input())
initList = [1,1,1,2,2]
res=[]
for c in range(caseNum):
    num = int(input())
    l = len(initList)
    for n in range(l,num):
        p = initList[n-1] + initList[n-5]
        initList.append(p)
    res.append(initList[num-1])
for r in res:
    print(r)
        
