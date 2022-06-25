#20040 사이클 게임
import sys 
sys.setrecursionlimit(10**5)
def search(node):
    global nList
    if node == nList[node]:
        return node
    nList[node] = search(nList[node])
    return nList[node]
    
n, m = map(int, input().split())
nList = [x for x in range(n)]
res = 0
exList = [map(int, input().split()) for _ in range(m)]

for i in range(m):
    s, e = exList[i]
    st = search(s)
    et = search(e)
    if st==et:
        res = i+1
        break
    nList[st] = min(st, et)
    nList[et] = min(st, et)
print(res)
