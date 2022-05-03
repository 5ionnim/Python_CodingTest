#1010 다리놓기
caseNum = int(input())
cases = [list(map(int, input().split())) for _ in range(caseNum)]
res = []
for c in cases:
    minNum = min(c)
    maxNum = max(c)
    checkList = [[0]*(maxNum-minNum+1) for _ in range(minNum)]
    checkList[0] = [1]*(maxNum-minNum+1)
    for i in range(1, minNum):
        for j in range(maxNum-minNum+1):
            checkList[i][j] = sum(checkList[i-1][j:])
    res.append(sum(checkList[minNum-1]))
for r in res:
    print(r)