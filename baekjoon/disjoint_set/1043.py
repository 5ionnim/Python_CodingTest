#1043 
import sys
sys.setrecursionlimit(10**5)
def search(n):
    global nList
    if nList[n]==n:
        return n
    nList[n]=search(nList[n])
    return nList[n]
N, M = map(int, input().split())
nList = [x for x in range(N+1)]
exList = list(map(int, input().split()))[1:]
pList = []
res = 0
for m in range(M):
    li = list(map(int, input().split()))[1:]
    mi = N+1
    for l in li:
        if search(l)<mi:
            mi=search(l)
    for l in li:
        nList[search(l)]=mi
    pList.append(mi)

tSet = set()
for e in exList:
    tSet.add(search(e))
for p in pList:
    if search(p) in tSet:
        continue
    res+=1
print(res)
    