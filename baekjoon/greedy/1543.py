#1543 문서 검색
fileName = input()
searchName = input()

cnt = 0

startIndex = 0
baseIndex = 1
lastIndex = len(fileName)

while fileName:
    if searchName in fileName[startIndex:baseIndex]:
        startIndex = baseIndex
        cnt += 1
    if baseIndex == lastIndex:
        break
    baseIndex += 1

print(cnt)
    
