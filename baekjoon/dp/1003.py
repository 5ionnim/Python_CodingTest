#1003 피보나치 함수
caseNum = int(input())
cases = [int(input()) for _ in range(caseNum)]
for c in cases:
    if c == 0:
        print("1 0")
    elif c == 1:
        print("0 1")
    else:
        testList = [[0,0] for _ in range(c+1)]
        testList[0][0] += 1
        testList[1][1] += 1
        for i in range(2, c+1):
            testList[i][0] = testList[i-1][0] + testList[i-2][0]
            testList[i][1] = testList[i-1][1] + testList[i-2][1]
        print(testList[c][0],testList[c][1])

    
    