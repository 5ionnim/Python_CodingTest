#10775 공항
gateNum = int(input())
airNum = int(input())
airs = [int(input()) for _ in range(airNum)]
cList = [x for x in range(gateNum+1)]
res = 0
def find(n):
    global cList
    if n==cList[n]:
        return n
    cList[n]=find(cList[n])
    return cList[n]
for a in airs:
    i = find(a)
    if i==0:
        break
    cList[i] = cList[i-1]
    res+=1
print(res)