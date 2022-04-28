#1463 1로 만들기
num = int(input())
testList = [0]*(num + 1)
for t in range(num, 0, -1):
    if t%2 == 0:
        if testList[t//2] == 0:
            testList[t//2] = testList[t] + 1
        else :
            testList[t//2] = min(testList[t] + 1, testList[t//2])
    if t%3 == 0:
        if testList[t//3] == 0:
            testList[t//3] = testList[t] + 1
        else :
            testList[t//3] = min(testList[t] + 1, testList[t//3])
    if testList[t-1] == 0:
        testList[t-1] = testList[t] + 1
    else :
        testList[t-1] = min(testList[t] + 1, testList[t-1])
print(testList[1])
    
    
    