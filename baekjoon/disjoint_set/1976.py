#1976 여행 가자
import sys
from collections import deque
sys.setrecursionlimit(10**5)
def find(a):
    global nList
    if a == nList[a]:
        return a
    nList[a] = find(nList[a])
    return nList[a]
    
N = int(input())
M = int(input())
nList = [x for x in range(N+1)]
for i in range(1,N+1):
    l = list(map(int, input().split()))
    for j in range(1,N+1):
        if l[j-1]==1:
            fi = find(i)
            fj = find(j)
            k = min(fi, fj)
            nList[fi] = k
            nList[fj] = k
pList = deque(list(map(int, input().split())))
b = find(pList.popleft())
res = 'YES'
while pList:
    if b != find(pList.popleft()):
        res = 'NO'
        break
print(res)