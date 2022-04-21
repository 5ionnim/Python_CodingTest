#1946 신입 사원 
caseNum = int(input())
result = []
for num in range(caseNum):
    pNum = int(input())
    pList = []
    reNum = 1
    for p in range(pNum):
        pList.append(list(map(int, input().split())))
    pList.sort(key = lambda x: x[0])
    
    maxP = pList[0][1]
    for pn in range(1, pNum):
        if maxP > pList[pn][1]:
            reNum += 1
            maxP = pList[pn][1]
    result.append(reNum)

print('\n'.join(map(str,result)))
        
    