#3109 빵집
rowNum, colNum = map(int,input().split())
initList = [list(input()) for _ in range(rowNum)]
cnt = 0
def search(node):
    global rowNum, colNum, initList, cnt
    row, col = node
    if col == colNum - 1:
        cnt += 1
        return True
    for i in [-1, 0, 1]:
        trow = row + i
        tcol = col + 1
        if trow < 0 or trow >= rowNum:
            continue
        if initList[trow][tcol] == '.':
            if search([trow, tcol]):
                initList[trow][tcol]='x'
                return True
            initList[trow][tcol]='x'
    return False

for r in range(rowNum):
    search([r, 0])
print(cnt)      
