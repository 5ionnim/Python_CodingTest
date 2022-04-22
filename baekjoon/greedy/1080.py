#1080 행렬
row, column = map(int, input().split())
strProcession = []
resProcession = []
cnt = 0

def changeList(r,c):
    global strProcession
    for i in range(3):
        for j in range(3):
            resProcession[r+i][c+j] = 1 - resProcession[r+i][c+j]
    
for r in range(row):
    strProcession.append(list(map(int, list(input()))))
for r in range(row):
    resProcession.append(list(map(int, list(input()))))


for r in range(row-2):
    for c in range(column-2):
        if resProcession[r][c] != strProcession[r][c]:
            changeList(r,c)
            cnt += 1

flag = True
for r in range(row):
    for c in range(column):
        if resProcession[r][c] != strProcession[r][c]:
            flag = False

print(cnt if flag else -1)
        

        
    